import requests
import time
from lxml import etree
from models import Book, BookChapters, BookCategory, BookChapterContent
import re
from utils.function import chinese2digits
import random


class LiteratureCrawler():
    def __init__(self):
        self.start_url = 'https://www.biquge.info'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}

    def crawling_book_category(self):
        print("开始爬取数据")
        html = requests.get(self.start_url, headers=self.headers)
        res = etree.HTML(html.content.decode())
        categories = res.xpath('//div[@class="nav"]/ul/li[position()>3 and position()<9]')
        for category in categories:
            category_name = category.xpath('./a/text()')[0]
            books_url = category.xpath('./a/@href')[0]
            # category_db = BookCategory(cate_name=category_name)
            response = requests.post('http://127.0.0.1:5000/category/add', data={
                'cate_name': category_name
            })
            response = response.json()
            if response.get('code') == 0:
                data = response.get('data')
                category_db = BookCategory(cate_name=data.get('cate_name'),cate_id=data.get('cate_id'))
                self.crawling_book_info(books_url, category_db.cate_id, category_db.cate_name)
            else:
                print("请求失败:", response)

    def crawling_book_info(self, books_url, cate_id, cate_name):
        html = requests.get(books_url, headers=self.headers)
        res = etree.HTML(html.content.decode())
        items = res.xpath('//div[@class="r"]/ul/li')
        for item in items:
            book_name = item.xpath('./span[@class="s2"]/a/text()')[0]
            book_url = item.xpath('./span[@class="s2"]/a/@href')[0]
            book_author = item.xpath('./span[@class="s5"]/text()')[0]
            book_category = item.xpath('./span[@class="s1"]/text()')[0]
            self.crawling_book_content(book_name, book_url, book_author, book_category, cate_id, cate_name)

    def crawling_book_content(self, book_name, book_url, book_author, book_category, cate_id, cate_name):
        html = requests.get(book_url, headers=self.headers)
        res = etree.HTML(html.content.decode())
        chapters = res.xpath('//div[@class="box_con"]/div[@id="list"]/dl/dd/a')
        intro = res.xpath('//div[@id="intro"]/p/text()')[0]
        book_db = Book({
            'book_name': book_name,
            'cate_id': cate_id,
            'cate_name': cate_name,
            'author_name': book_author,
            'chapter_num': len(chapters),
            'channel_name': '笔趣阁',
            'channel_url': book_url,
            'intro': intro
        })
        response = requests.post('http://127.0.0.1:5000/book/add', data={
            'book_name': book_name,
            'cate_id': cate_id,
            'cate_name': cate_name,
            'author_name': book_author,
            'chapter_num': len(chapters),
            'channel_name': '笔趣阁',
            'channel_url': book_url,
            'intro': intro
        })
        response = response.json()
        if response.get('code') == 0:
            data = response.get('data')
            book_db = Book({'book_id': data.get('book_id')})
            print("开始爬取小说---{}".format(book_name))
            response = requests.get('http://127.0.0.1:5000/chapter/last', params={
                'book_id': book_db.book_id
            })
            response = response.json()
            last = 0
            if response.get('code') == 0:
                data = response.get('data')
                if data and data.get('chapter_id'):
                    last = int(data.get('chapter_id'))
                    print("获取最后章节={}".format(last))
                    index = len(chapters)-1
                    newId = -1
                    while index > 0:
                        lastChapter = chapters[index]
                        lastUrl = book_url + lastChapter.xpath('./@href')[0]
                        newId = self.getNewChapterId(lastUrl)
                        if newId > 0:
                            break
                        index -= 1
                    if last >= newId:
                        return
            for i, chapter in enumerate(chapters):
                if i + 1 <= last:
                    continue
                chapter_url = book_url + chapter.xpath('./@href')[0]
                self.crawling_book_chapter(chapter_url, book_db.book_id, last)
            print("爬取小说结束，小说名={}".format(book_name))
        else:
            print("请求失败:", response)

    def crawling_book_chapter(self, chapter_url, book_id, last):
        html = requests.get(chapter_url, headers=self.headers)
        html = html.content.decode()
        res = etree.HTML(html)
        chapter_name = res.xpath('//div[@class="bookname"]/h1/text()')[0]
        if not chapter_name.startswith('第'):
            return
        p1 = re.compile(r'第(.*?)章', re.S)
        chapter_id = re.findall(p1, chapter_name)
        if len(chapter_id) <= 0:
            return
        chapter_id = chapter_id[0]
        chapter_id = self.getChapterId(chapter_id)
        chapter_id = chinese2digits(chapter_id)
        if chapter_id <= last and chapter_id != -1:
            return
        # content = res.xpath('//div[@id="content"]')[0].xpath('string(.)')
        content = re.findall(r'<div id="content"><!--go-->(.*?)<!--over-->\s+</div>', html, re.S)
        if len(content) > 0:
            content = content[0]
            content = re.sub("<br/>+", "\n", content)
            content = re.sub("\n+", "\n", content)
            content = re.sub("\r+", "", content)
            content = re.sub("&nbsp;", " ", content)
        else:
            content = ""
        response = requests.post('http://127.0.0.1:5000/chapter/add/{}'.format(book_id), data={
            'chapter_id': chapter_id,
            'chapter_name': chapter_name,
            'chapter_content': content
        })
        response = response.json()
        if response.get('code') == 0:
            print("爬取成功,名称:{},第{}章".format(book_id, chapter_id))
            # time_stamp = random.randrange(5, 10, 1)
            time.sleep(2)
        else:
            print("爬取失败,名称:{},第{}章".format(book_id, chapter_id))

    @staticmethod
    def getChapterId(text):
        cop = re.compile("[^\u4e00-\u9fa5^0-9^-]")
        return cop.sub('', text)

    def getNewChapterId(self, last_url):
        html = requests.get(last_url, headers=self.headers)
        html = html.content.decode()
        res = etree.HTML(html)
        chapter_name = res.xpath('//div[@class="bookname"]/h1/text()')[0]
        p1 = re.compile(r'第(.*?)章', re.S)
        chapter_id = re.findall(p1, chapter_name)
        if len(chapter_id) <= 0:
            return -1
        chapter_id = chapter_id[0]
        chapter_id = self.getChapterId(chapter_id)
        chapter_id = chinese2digits(chapter_id)
        return chapter_id


if __name__ == '__main__':
    crawler = LiteratureCrawler()
    crawler.crawling_book_category()

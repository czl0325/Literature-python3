import requests
import re


class LiteratureCrawler():
    def __init__(self):
        self.start_url = 'https://www.biquge.info/list/1_1.html'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}

    def run(self):
        html = requests.get(self.start_url, headers=self.headers)
        html = html.content.decode()
        content = re.findall('<div id="nr1">(.*?)</div>', html, re.S)
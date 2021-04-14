import {http1} from "@/http/http";
import {BookModel, ChapterModel} from "@/models/models";

export const registerUser = (userName: string, password: string, gender: number, location: string, avatar: File) => {
  return http1.upload('/user/register', avatar, {
    userName,
    password,
    gender,
    location
  })
}

export const getCategoryList = () => {
  return http1.get('/category/list')
}

export const getBookList = (pageNum: number=1, cates: string='', refresh: boolean = true, state: {  refreshing: boolean, loading: boolean, finished: boolean }) => {
  return http1.getWithPaging<BookModel>('/book/list', {
    cates,
    pageNum
  }, refresh, state)
}

export const getBookDetail = (book_id: number) => {
  return http1.get(`/book/detail/${book_id}`)
}

export const getChapterList = (book_id: number, pageNum: number=1, refresh: boolean, state: {  refreshing: boolean, loading: boolean, finished: boolean }) => {
  return http1.getWithPaging<ChapterModel>(`/chapter/list/${book_id}`, {
    pageNum
  }, refresh, state)
}

export const getChapterDetail1 = (id: number) => {
  return http1.get(`/chapter/content`, {
    id
  })
}

export const getChapterDetail2 = (chapter_id: number, book_id: number) => {
  return http1.get(`/chapter/content`, {
    chapter_id,
    book_id
  })
}

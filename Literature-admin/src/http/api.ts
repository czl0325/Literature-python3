import {http1} from "@/http/http";
import {FileModel} from '@/http/myAxios'
import {BookModel} from "@/models/models";

export const getCategoryList = () => {
  return http1.get('/category/list')
}

export const addCategory = (file: FileModel, cate_name: string) => {
  return http1.upload('/category/add', file, {
    cate_name
  })
}

export const deleteCategory = (id:number) => {
  return http1.get(`/category/delete/${id}`)
}

export const getBookList = (cates: string='') => {
  return http1.get('/book/list', {
    cates
  })
}

export const addBook = (book: BookModel) => {
  return http1.post('/book/add', {
    ...book
  })
}

export const getBookDetail = (book_id: number) => {
  return http1.get(`/book/detail/${book_id}`)
}

export const getChapterList = (book_id: number) => {
  return http1.get(`/chapter/list/${book_id}`)
}

export const addChapter = (book_id: number, chapter_id: number, chapter_name: string, chapter_content?: string) => {
  return http1.post(`/chapter/add/${book_id}`, {
    chapter_id,
    chapter_name,
    chapter_content
  })
}

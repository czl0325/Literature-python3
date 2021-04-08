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

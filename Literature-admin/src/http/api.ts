import {http1} from "@/http/http";

export const getCategoryList = () => {
  return http1.get('/category/list')
}

export const deleteCategory = (id:string) => {
  return http1.get(`/category/delete/${id}`)
}

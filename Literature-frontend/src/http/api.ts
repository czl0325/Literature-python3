import {http1} from "@/http/http";

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

export const getBookList = (cates: string='') => {
  return http1.get('/book/list', {
    cates
  })
}

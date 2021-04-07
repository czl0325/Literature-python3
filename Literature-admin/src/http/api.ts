import {http1} from "@/http/http";

export const getCategoryList = () => {
  return http1.get('/category/list')
}

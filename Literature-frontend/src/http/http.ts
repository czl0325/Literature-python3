import {Toast} from "vant";
import {MyAxios, BaseResponseData} from "@/http/myAxios";
import qs from 'qs';
import {AxiosInstance} from "axios";
import {PageModel} from "@/models/models";
import router from "@/router/router";
import store from "@/store/index";

export class HttpService {
  myAxios: AxiosInstance;

  constructor(url:string) {
    // 获取axios实例
    this.myAxios = new MyAxios(url).getInterceptors();
  }

  get(url: string, params: object = {}) {
    return new Promise((resolve, reject) => {
      this.myAxios.get(url, {
        params: params
        // @ts-ignore
      }).then((res: BaseResponseData) => {
        this.resultHandle(res, resolve);
      }).catch((err: { message: any; }) => {
        reject(err.message);
      });
    });
  }

  async getWithPaging<T>(url: string, params: object = {}, refresh: boolean = true, state: {  refreshing: boolean, loading: boolean, finished: boolean }) {
    if (refresh) {
      state.refreshing = true
    } else {
      state.loading = true
    }
    let result = await this.myAxios.get(url, {params})
    // @ts-ignore
    if (result.code === 0) {
      // @ts-ignore
      const page = result.data as PageModel<T>;
      const list = page.items
      // @ts-ignore
      if (list.length > 0) {
        if (refresh) {
          state.refreshing = false
        } else {
          state.loading = false
        }
        state.finished = (page.page_num === page.total_page);
      } else {
        state.refreshing = false
        state.loading = false
        state.finished = true
      }
      return Promise.resolve(list)
    } else {
      // @ts-ignore
      Toast.fail(result.message)
      state.refreshing = false
      state.loading = false
      state.finished = false
      return Promise.reject(result)
    }
  }

  post(url: string, params: object) {
    return new Promise((resolve, reject) => {
      // @ts-ignore
      this.myAxios.post(url, qs.stringify(params)).then((res:BaseResponseData) => {
        this.resultHandle(res, resolve);
      }).catch((err: { message: any; }) => {
        reject(err.message);
      });
    });
  }

  upload(url: string, file: File, params: object) {
    let formData = new FormData()
    let configs = {
      headers: {'Content-Type':'multipart/form-data'}
    };
    formData.append('file', file)
    Object.keys(params).map((key) => {
      // @ts-ignore
      formData.append(key, params[key])
    })
    return new Promise((resolve, reject) => {
      // @ts-ignore
      this.myAxios.post(url, formData, configs).then((res:BaseResponseData) => {
        this.resultHandle(res, resolve);
      }).catch((err: { message: any; }) => {
        reject(err.message);
      });
    })
  }

  resultHandle(res: BaseResponseData, resolve: { (value?: unknown): void; (arg0: any): void; }) {
    if (res.code === 0) {
      resolve(res.data);
    } else if (res.code === 4100) {
      Toast.fail('登录过期，请重新登录！')
      store.commit('updateUserInfo', {})
      localStorage.removeItem('userInfo')
      router.push('login')
    } else {
      Toast.fail(res.message || '未知错误')
    }
  }
}

export const http1 = new HttpService('/api')




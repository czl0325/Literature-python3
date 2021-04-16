// 首先引入axios和上一步封装的cookie方法
import axios, { AxiosInstance } from 'axios';
import {Toast} from "vant";
import store from "@/store";

export interface BaseResponseData {
  code: number;
  message?: string;
  data?: any;
}

export interface FileModel {
  content: string;
  file: File;
  message: string;
  status: string;
}

export class MyAxios {
  instance: AxiosInstance;

  constructor(url:string) {
    this.instance = axios.create({
      baseURL: url || '',
      timeout: 10000
    })
    this.init()
  }

  getInterceptors() {
    return this.instance;
  }

  // 初始化拦截器
  init() {
    // 请求接口拦截器
    this.instance.interceptors.request.use(
      config => {
        // @ts-ignore
        if (store.state.userInfo.token) {
          // @ts-ignore
          config.headers.token = store.state.userInfo.token;
        }
        return config
      },
      err => {
        console.error(err)
      }
    )

    // 响应拦截器
    this.instance.interceptors.response.use(
      response => {
        if (response.status === 200) {
          Toast.clear();
          return Promise.resolve(response.data);
        } else {
          Toast.fail(`错误：${response.status}`)
          return Promise.reject(response.data);
        }
      },
      err => {
        const {response} = err;
        if (response) {
          Toast.fail(err.message);
          return Promise.reject(err);
        } else {
          Toast.fail('网络连接异常,请稍后再试!');
        }
      });
  }
}

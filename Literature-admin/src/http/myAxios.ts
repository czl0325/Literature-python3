// 首先引入axios和上一步封装的cookie方法
import axios, { AxiosInstance } from 'axios';
import {ElMessage} from "element-plus";

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
          ElMessage.closeAll();
          return Promise.resolve(response.data);
        } else {
          ElMessage.error(`错误：${response.status}`)
          return Promise.reject(response.data);
        }
      },
      err => {
        const {response} = err;
        if (response) {
          ElMessage.error(err.message);
          return Promise.reject(err);
        } else {
          ElMessage.error('网络连接异常,请稍后再试!');
        }
      });
  }
}

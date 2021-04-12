// 首先引入axios和上一步封装的cookie方法
import axios, { AxiosInstance } from 'axios';
import {ElMessage, ElLoading} from "element-plus";
import {ILoadingInstance} from "element-plus/lib/el-loading/src/loading.type";

export interface BaseResponseData {
  code: number;
  message?: string;
  data?: any;
}

export interface FileModel {
  lastModified: number;
  lastModifiedDate: Date;
  name: string;
  size: number;
  type: string;
  uid: number;
  webkitRelativePath: string;
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

  loading: ILoadingInstance | undefined

  // 初始化拦截器
  init() {
    // 请求接口拦截器
    this.instance.interceptors.request.use(
      config => {
        this.loading = ElLoading.service({})
        return config
      },
      err => {
        console.error(err)
      }
    )

    // 响应拦截器
    this.instance.interceptors.response.use(
      response => {
        if (this.loading) {
          this.loading.close()
        }
        if (response.status === 200) {
          ElMessage.closeAll();
          return Promise.resolve(response.data);
        } else {
          ElMessage.error(`错误：${response.status}`)
          return Promise.reject(response.data);
        }
      },
      err => {
        if (this.loading) {
          this.loading.close()
        }
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

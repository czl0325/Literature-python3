import { ElMessage } from 'element-plus'
import {MyAxios, BaseResponseData, FileModel} from "@/http/myAxios";
import qs from 'qs';
import {AxiosInstance} from "axios";

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

  upload(url: string, file: FileModel, params: object) {
    let formData = new FormData()
    let configs = {
      headers: {'Content-Type':'multipart/form-data'}
    };
    // @ts-ignore
    formData.append('file', file)
    Object.keys(params).map((key) => {
      // @ts-ignore
      formData.append(key, params[key])
    })
    debugger;
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
    } else {
      ElMessage.error(res.message || '未知错误');
    }
  }
}

export const http1 = new HttpService('/api')




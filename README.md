# Literature-python3
我写的小说电子书网站。前后端分离，前端采用vue3+typescript+vant-ui开发，后端采用python3.9+flask开发。后台管理系统采用vue3+typescript+elementui-plus开发


#### 介绍

* Literature-frontend ： 手机端页面代码
* Literature-backend ： 服务端代码
* Literature-admin ： 后台管理系统代码

#### 部分截图

<img src="https://github.com/czl0325/Literature-python3/blob/main/screenshots/front-1.png" width="200" /> <img src="https://github.com/czl0325/Literature-python3/blob/main/screenshots/front-2.png" width="200" /> <img src="https://github.com/czl0325/Literature-python3/blob/main/screenshots/front-3.png" width="200" />

#### 运行

* 1.服务端运行

  * 自行创建python虚拟环境，或者用pycharm直接打开Literature-backend文件夹，会自动安装虚拟环境并且下载所需要的库
  * 在Literature-backend目录下创建一个logs文件夹。
  * 自行安装mysql，并且创建一个叫Literature的数据库。根据Migrate命令生成表。详见Literature-backend内的文档
  * 启动服务器后，运行crawler.py文件开始爬取笔趣阁的小说。


* 2.vue3代码运行

  * 进入目录后先npm install
  * 在运行npm run serve

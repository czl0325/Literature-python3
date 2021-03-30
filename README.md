# Literature-python3
小陈文学。采用python3+flask开发，前后端分离


### 1. 创建虚拟环境

首先安装虚拟环境
```
pip3 install virtualenv
pip3 install virtualenvwrapper
```

在~目录下创建.bashrc文件
```
export WORKON_HOME=~/.environments
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

需要重新刷新下
```
source ~/.bashrc
```

* mkvirtualenv -p python3 literature
* workon literature
* pip install -r requirments.txt  (项目运行所用到的包)


### 2. 数据库迁移

* 需要用到两个库
    * Flask-Script
    * Flask-Migrate
    * mysqlclient

* 迁移步骤
    * 生成迁移文件夹 `python3 manage.py db init`
    * 生成迁移脚本 `python3 manage.py db migrate -m '描述信息'`
    * 执行迁移脚本 `python3 manage.py db upgrade`
  
* 遇到错误

  * sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (2003, "Can't connect to MySQL server on 'localhost' ([Errno 61] Connection refused)")

    因为连接的是mysql8，mysql8改变了密码的加密方式，你在安装mysql8的时候设置的密码在这里输入是没用的，请重新设置密码，加密方式改为mysql_native_password。
```
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '111111';
```

  * `ERROR 1290 (HY000): The MySQL server is running with the --skip-grant-tables option so it cannot execute this statement`

修改/private/etc/my.cnf文件注释掉--skip-grant-tables

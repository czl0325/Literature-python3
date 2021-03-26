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



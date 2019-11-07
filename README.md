# Django Blog 源代码使用方法
首先请先将本项目下载到自己的计算机中
若装有Git可直接使用以下指令:
git clone https://github.com/LiusCraft/djangoblog.git
若没有安装可直接下载成zip文件

# 安装模块
安装Django (最新版本)

```pip3 install django```

安装mysqlclient (最新版本)

```pip3 install mysqlclient```

# 数据库配置

我们在项目的 settings.py 文件中找到 DATABASES 配置项，将其信息修改为：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 或者使用 mysql.connector.django
        'NAME': '数据库名',
        'USER': 'mysql用户名',
        'PASSWORD': '密码',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
```

上面包含数据库名称和用户的信息，它们与 MySQL 中对应数据库和用户的设置相同。Django 根据这一设置，与 MySQL 中相应的数据库和用户连接起来。

# 构建表结构

```
$ python manage.py migrate   # 创建表结构
$ python manage.py makemigrations  # 让 Django 知道我们在我们的模型有一些变更
$ python manage.py migrate   # 创建表结构
```

# 运行Django项目

```python3 manage.py runserver 0.0.0.0:80```

这里注意要进入放有manage.py的文件夹下，然后运行上面这条指令，后面跟上的 IP:PORT 可自己根据实际情况来定

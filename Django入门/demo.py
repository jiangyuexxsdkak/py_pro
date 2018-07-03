#pip3 install django

# 在命令行输入
django-admin #可用命令

#新建一个项目mysite
django-admin startproject mysite

#进入mysite目录执行manage.py文件,查看可执行的命令
python manage.py

#启动开发服务(要访问django必须要保持启动)
python manage.py runserver
python manage.py runserver 192.168.19.168：8000

#创建应用
python manage.py startapp app1

#配置settings.py文件，并建立数据库

#migrate(创建相关表)
python manage.py migrate

#创建超级用户
python manage.py createsuperuser

#编写models.py

#编写之后重新makemigrations(记录变化)
python manage.py makemigrations

# makemigrations之后执行migrate，写入数据库（应用变化）
python manage.py migrate
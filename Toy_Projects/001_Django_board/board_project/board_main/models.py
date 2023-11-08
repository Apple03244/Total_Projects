from django.db import models
from datetime import datetime

# Create your models here.
# models.py의 클래스와 DBd의 table과 sync를 맞춰 테이블 자동생성


#클래스 명=테이블 명, 변수=컬럼명
class test(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    #varchar255가 default
    password=models.CharField(max_length=20)

class Author(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=40,null=True, unique=True)
    password=models.CharField(max_length=30)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(null=True)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    
    #fk를 설정한 변수명에 _id를 붙여 자동 생성됨
    #on_update=models.CASCADE, on_delete=mo~~
    author=models.ForeignKey(Author,null=True,on_delete=models.SET_NULL,related_name='posts')

    #python manage.py makemigrations
    #python manage.py migrate


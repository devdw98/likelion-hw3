from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = 'images/') #pip install pillow :db에 이미지를 넣고싶을 때
    description = models.CharField(max_length=500)

    def __str__(self): #admin에 타이틀이 뜨길 원하니까 이걸로 정의
        return self.title
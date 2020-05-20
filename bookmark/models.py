from django.db import models
from django.urls import reverse
"""
 models : 데이터 베이스 구조 
"""
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        # 객체 출력 시 나태내는 값
        return "이름: "+self.site_name + ", 주소: " + self.url

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])



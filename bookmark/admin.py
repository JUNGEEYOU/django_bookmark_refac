from django.contrib import admin

from .models import Bookmark

"""
    관리자 페이지에 미리 모델을 관리할 수 있도록 등록 
"""

admin.site.register(Bookmark)  # 해당 모델을 관리자 페이지에서 관리 가능하도록 등록

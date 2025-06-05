from django.contrib import admin
from django.urls import path
from myapp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # 기본 페이지로 home 뷰 연결
]

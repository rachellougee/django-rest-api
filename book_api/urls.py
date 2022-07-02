from django.contrib import admin
from django.urls import path
#from book_api import views
from rest_framework.urlpatterns import format_suffix_patterns
from book_api.views import BookList, BookDetail

urlpatterns = [
    # path('', views.book_list),
    # path('<int:id>', views.book_detail),
    path('', BookList.as_view()),
    path('<int:id>', BookDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='index' ),
    path('author/<name>',getauthor,name='author'),
    path('article/<int:id>',getsingle,name='single'),
    path('topic/<name>',gettopic,name='topic'),

]
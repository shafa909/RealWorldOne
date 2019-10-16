
from django.contrib import admin
from django.urls import path

from . import api 

urlpatterns = [
    path('chats/', api.ChatSessionView.as_view()),
    path('chats/<uri>/', api.ChatSessionView.as_view()),
    path('chats/<uri>/messages/', api.ChatSessionMessageView.as_view()),
]

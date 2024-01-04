from django.urls import path
from app1 import views

urlpatterns=[
    path('message/',views.MessageListView.as_view(), name='message-list'),
    path('messages/create/',views.MessageCreateView.as_view(), name='message-create'),
]
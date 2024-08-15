from django.urls import path
from . import views

app_name = 'notesApp'

urlpatterns = [
    path('', views.all_notes, name='all_notes'),
    path('add/', views.note_add, name='add'),
    path('<slug:slug>/', views.detail, name='detail'),
    
]

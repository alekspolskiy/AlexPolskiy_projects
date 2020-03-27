from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    #path('', views.home, name='home'),
    #path('detail/<int:id>', views.detail_page, name='detail_page')
	path('', views.HomeListView.as_view(), name='home'),
	path('detail/<int:pk>', views.HomeDetailView.as_view(), name='detail_page'),
	path('edit/', views.edit_page, name='edit_page'),
	path('update/<int:pk>', views.update_page, name='update_page'),
	path('delete/<int:pk>', views.delete_page, name='delete_page')
]

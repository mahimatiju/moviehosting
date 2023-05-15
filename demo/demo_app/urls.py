from django.urls import path

from . import views

app_name='demo_app'

urlpatterns = [
    path('', views.add, name='mem'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('w', views.add_movies, name='members'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    
    
    
    path('cbvhome', views.MOVIEListView.as_view(), name='cbvhome'),
    
    path('cd/<int:pk>/', views.MOVIEdetailView.as_view(), name='cd'),
    
    path('cu/<int:pk>/', views.MOVIEupdatelView.as_view(), name='cu'), 
    
    path('cdd/<int:pk>/', views.MOVIEdeleteView.as_view(), name='cdd'), 

]

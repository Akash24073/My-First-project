from django.urls import path
from.import views

urlpatterns = [
    path('', views.index,name='index'),
    path('corlo/', views.corlo,name='corlo'),
    path('insert', views.insertData,name="insertData"),
    path('update/<id>', views.updateData,name="insertData"),
    path('delete/<id>', views.deleteData,name="deletetData"),
]

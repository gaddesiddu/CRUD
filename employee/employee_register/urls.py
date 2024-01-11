from django.contrib import admin
from django.urls import path,include
from employee_register import views
urlpatterns = [
    path('',views.index,name="index"),
    path('insert',views.insertData,name="insertData"),
    path('update/<id>',views.updateData,name="updateData"),
    path('delete/<id>',views.deleteData,name="deleteData"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('registro/',views.registro, name='registro'),
    path('actualizar/<int:id>',views.actualizar,name='actualizar'),
    path('eliminar/<int:id>',views.eliminar,name='eliminar')
]
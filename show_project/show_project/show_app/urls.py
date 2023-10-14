from django.urls import path
from . import views
app_name = 'show_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('show/<int:show_id>/',views.detail,name='detail'),
    path('add/',views.add_show,name='add_show'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),



]
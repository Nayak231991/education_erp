from django.urls import path,include
from .import views
urlpatterns = [
    path('', views.home,name='home'),
    path('addtrainer', views.addtrainer,name='addtrainer'),
    path('showtrainers', views.showtrainers,name='showtrainers'),
    path('addcourse', views.addcourse,name='addcourse'),
    path('showcourse', views.showcourse,name='showcourse'),
    path('addstudent', views.addstudent,name='addstudent'),
    path('searchstudent', views.searchstudent,name='searchstudent'),
    path('searchenquiry', views.searchenquiry,name='searchenquiry'),    
    path('createbatch', views.createbatch,name='createbatch'),
    path('feepay', views.feepay,name='feepay'),
    path('showtrans', views.showtrans,name='showtrans'),
]

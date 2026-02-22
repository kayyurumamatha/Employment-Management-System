from django.contrib import admin
from App  import views
from django.urls import path
urlpatterns=[
    path('admin/',admin.site.urls),
    path('',views.home,),
    path('newstaff/',views.newstaff,name='Newemployee'),
    path('search/',views.search,name='Searchemployee'),
]
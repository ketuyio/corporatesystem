from django.contrib import admin
from django.urls import path
from corporateapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.index,name='index'),
    path('blog/', views.blog,name='blog'),
    path('blog-details/', views.blogdetails,name='details'),
    path('portfolio-details/', views.portfolio,name='portfolio'),
    path('sample-inner-page/', views.sampleinner,name='inner-page'),
]

from django.urls import path
from kunapp import views

urlpatterns = [
      path('',views.index, name='my_home'),
      path('about/',views.about, name='my_about'),
      path('blog/',views.blog, name='my_blog'),
      path('classy/',views.classy, name='my_classy')
]

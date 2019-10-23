
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.getpage),
    path('output',views.output,name='last.html'),
    path('outputa',views.outputa,name='avgg.html'),
    path('outputtr',views.outputtr,name='travg.html'),
    path('output1', views.output1, name='trr.html'),
    path('outputv', views.outputv,name='amodu.html'),
    path('output2', views.output2,name='modu.html'),

]

from text1 import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()

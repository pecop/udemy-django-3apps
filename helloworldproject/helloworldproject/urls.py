from django.contrib import admin
from django.urls import path, include
from .views import HelloWorldClass, helloworldfunction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', helloworldfunction),
    # path('helloworld2/', admin.site.urls),
    path('helloworld2/', HelloWorldClass.as_view()),
    path('appp/', include('helloworldapp.urls')),
]

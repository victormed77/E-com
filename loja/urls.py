from django.contrib import admin
from django.urls import path
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),


    # TODO: Remover debug toolbar
    path('__debug__/', include('debug_toolbar.urls')),
]

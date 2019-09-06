"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

import core.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/',include(core.urls)),
]
from django.views.generic import RedirectView
'''
The following lines are written below in order to,
redirect our ip 'localhost:8000/' to 'localhost:8000/core'
this makes the IP's with path core to be our default path
It acts like our index page in case of a PHP structure
'''
urlpatterns += [
    path('', RedirectView.as_view(url='/core/', permanent=True)),
]
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

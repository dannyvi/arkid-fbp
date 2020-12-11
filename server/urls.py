"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import os

from common.django.drf.meta_config import MetaConfigs
#from common.django.app.automation.flows.core import MetaConfigs
from django.contrib import admin
from django.urls import path, include


# file_dir = os.path.join(os.getcwd(), 'account/api_config')
apps = ['account']

urlpatterns = [
    path('admin/', admin.site.urls),
    path('arkfbp-admin/', include(MetaConfigs(apps=apps).get_urls()))

]

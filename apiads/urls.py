"""apiads URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include, url
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static

API_TITLE = 'API Python Django - Grupo 03'
API_DESCRIPTION = 'A Web API for creating and viewing schemas.'
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    url(r'^api/', include('authorization.urls')),
    url(r'^api/', include('commerce.urls')),
    url(r'^api/', include('account.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^schema/$', schema_view),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    url(r'^api/auth/', include('djoser.urls')),
    url(r'^api/auth/', include('djoser.urls.authtoken'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""
URL configuration for myportfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.index.urls')),
    path('portfolio/', include('applications.portfolio.urls')),
    path('sobre-mi/', include('applications.sobremi.urls')),
    path('curriculum/', include('applications.curriculum.urls')),
    path('blog/', include(('applications.blog.urls', 'blog'), namespace='blog')),
    path('contacto/', include('applications.contacto.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    re_path(r'^favicon\.ico$', lambda request: HttpResponse(status=204)),
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

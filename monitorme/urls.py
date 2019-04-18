"""monitorme URL Configuration

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
from django.urls import path, include
from django.views.generic import RedirectView
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    # path('core/', include('core.urls')),
    path('', core_views.index, name='index'),
    path('profile/<username>', core_views.user_profile, name="user_profile"),
    path('landing_page/<username>', core_views.landing_page, name="landing_page"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# team has agreed to only use one urls.py file

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
       path('__debug__/', include(debug_toolbar.urls)),
   ] + urlpatterns

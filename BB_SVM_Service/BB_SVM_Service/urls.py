from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/', include('website.urls')),
    path('admin/', admin.site.urls),
    url(r'^', TemplateView.as_view(template_name='index.html')),
]

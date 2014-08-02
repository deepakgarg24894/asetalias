from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
url(r'^$', 'frontpage.views.register'),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

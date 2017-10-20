from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('social_django.urls', namespace='social')),

    # TODO replace with s3
    url(r'^static/(?P<path>.*)$', serve, dict(insecure=True)),
    url('', RedirectView.as_view(url='/admin/')),
]

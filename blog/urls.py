from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^redactor/', include('redactor.urls')),

    url(r'^$', 'sitio.views.index', name='index'),
    url(r'^entrada/(?P<slug>[-\w]+)/$', 'sitio.views.EntradaDetalles', name='vista_post'),
    url(r'^categoria/(?P<slug>[-\w]+)/$', 'sitio.views.CategoriaPaginacion', name='vista_categoria'),
]

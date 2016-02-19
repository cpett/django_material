from django.conf.urls import include, url
from django.contrib import admin
from material.frontend import urls as frontend_urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Examples:
    # url(r'^$', 'django_material.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^frontend/', include(frontend_urls)),
    url(r'', include('djmaterial.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

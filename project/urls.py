from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    re_path(r'^rosetta/', include('rosetta.urls'))
]

urlpatterns += i18n_patterns (
    path('', include('main.urls', namespace='main'))
)
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.conf.urls import handler404
urlpatterns = [
    path("", include('main.urls', namespace='land')),
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns (
    path("", include('main.urls', namespace='land')),
)
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = "main.views.page_not_found_view"


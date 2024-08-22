from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from core.views import redirect_root_to_language  # Importa la vista que creaste

urlpatterns = [
    path("admin/", admin.site.urls),
    path('set-language/', include('django.conf.urls.i18n')),  # Ruta funcional para cambiar el idioma
    path('', redirect_root_to_language),  # Redirigir la raíz al idioma predeterminado
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path("", include('core.urls')),  # Internacionaliza las rutas de la aplicación principal
    # Otras rutas que deberían estar internacionalizadas...
)
from django.urls import get_resolver

for url_pattern in get_resolver().url_patterns:
    print(url_pattern)


# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from django.conf.urls.i18n import i18n_patterns

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path('set-language/', include('django.conf.urls.i18n')),  
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += i18n_patterns(
#     path("", include('core.urls')),  

# )

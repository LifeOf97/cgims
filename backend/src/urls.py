from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='api/')),
    path('api/', include('careerguide.urls', namespace='careerguide')),

    # api documentation urls
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name="schema"), name="schema-redoc"),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name="schema"), name="schema-swagger"),

]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

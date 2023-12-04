

from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('gestor/', admin.site.urls),
    path('contas/', include('contasapp.urls')),
    path('', include('agendamentoapp.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler403 = 'agendamentoapp.views.error_403'
handler404 = 'agendamentoapp.views.error_404'
handler500 = 'agendamentoapp.views.error_500'

handler403 = 'contasapp.views.error_403'
handler404 = 'contasapp.views.error_404'
handler500 = 'contasapp.views.error_500'
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('',RedirectView.as_view(url="/main/",permanent=True)),
    path('quiz/', include('quiz.urls')),
    path('guestbook/', include('guestbook.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

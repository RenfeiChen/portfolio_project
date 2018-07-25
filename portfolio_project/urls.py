from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import cover.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cover.views.cover, name='cover'),
    path('home/', jobs.views.home, name='home'),
    path('blog/', include('blog.urls'), name='blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

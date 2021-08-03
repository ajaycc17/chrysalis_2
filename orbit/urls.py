from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "OrbitGadget"
admin.site.site_title = "OrbitGadget Admin"
admin.site.index_title = "Welcome to OrbitGadget Admin"

urlpatterns = [
    path('pikachoo-admin/', admin.site.urls),
    path('', include(('home.urls', 'home'), namespace='home')),
    path('blog/', include('blog.urls')),
    path('projects/', include('project.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

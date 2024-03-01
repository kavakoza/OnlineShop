from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('categories.urls', namespace='categories')),
    path('product/', include('products.urls', namespace='products')),
    path('user/', include('users.urls', namespace='users')),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

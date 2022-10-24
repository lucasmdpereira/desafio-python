
from django.urls import path, include
from apihandler.views import index, websites, detail, users

urlpatterns = [
    path('', index),
    path('users/websites', websites, name='websites'),
    path('users/detail', detail, name='detail'),
    path('users', users, name='users'),
    path('accounts/', include('django.contrib.auth.urls')),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

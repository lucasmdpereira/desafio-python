
from django.urls import path, include
from apihandler.views import all_data, websites, detail, users, raw_data, raw_websites, raw_detail, raw_users

urlpatterns = [
    path('', all_data),
    path('users/websites', websites, name='websites'),
    path('users/detail', detail, name='detail'),
    path('users', users, name='users'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('raw', raw_data, name='raw_data'),
    path('raw_users/websites', raw_websites, name='raw_websites'),
    path('raw_users/detail', raw_detail, name='raw_detail'),
    path('raw_users', raw_users, name='raw_users'),
    
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

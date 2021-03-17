from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('__debug__/', include(debug_toolbar.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('app.urls')),
    path('api/', include('api.urls')),
    path('account/', include('account.urls')),
]

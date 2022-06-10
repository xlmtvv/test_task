from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from rest_framework.routers import SimpleRouter
from catalog.views import EmployeeViewSet, EmployeeTreeViewSet

from .yasg import urlpatterns as doc_urls

router = SimpleRouter()
router.register(r'api/employees', EmployeeViewSet)
router.register(r'api/tree/employees', EmployeeTreeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drf-auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

urlpatterns += doc_urls

urlpatterns += router.urls

if settings.DEBUG:
    import debug_toolbar
    urlpatterns =[
        path('__debug__/', include('debug_toolbar.urls'))
        ] + urlpatterns
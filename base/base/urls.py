from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from rest_framework.routers import SimpleRouter
from catalog.views import EmployeeViewtSet

router = SimpleRouter()
router.register(r'employee', EmployeeViewtSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('catalog.urls')),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += router.urls

if settings.DEBUG:
    import debug_toolbar
    urlpatterns =[
        path('__debug__/', include('debug_toolbar.urls'))
    ] + urlpatterns
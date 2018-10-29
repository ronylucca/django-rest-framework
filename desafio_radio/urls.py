from django.contrib import admin
from django.urls import path, include
from core.views import ProgramaViewSet, RadioViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'programas', ProgramaViewSet)
router.register(r'radios', RadioViewSet)


urlpatterns = [
    path(r'', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('<str:radio>/programacao', RadioViewSet.obtem_programacao_radio)
]

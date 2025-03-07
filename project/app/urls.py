from .views import reverse_view
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,top_expensive_products

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('api/', include(router.urls)),
    path('reverse/', reverse_view, name='reverse_view'),
    path('api/top-products/', top_expensive_products, name='top-products'),

]

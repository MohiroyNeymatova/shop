from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()


router.register('client', ClientView)
router.register('product', ProductView)
router.register('payment', PaymentView)
router.register('order', OrderView)
router.register('order_item', OrderItemView)

from django.urls import path
from .views import RegisterViewSet, EventViewSet, PurchaseTicketView, top_events
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create a router object
router = DefaultRouter()
router.register(r'register', RegisterViewSet)
router.register(r'events', EventViewSet)

# Define the URL patterns for the application
urlpatterns = [
    path('events/<int:event_id>/purchase/', PurchaseTicketView.as_view(), name='purchase-ticket'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('top-events/', top_events, name='top-events'),
] + router.urls
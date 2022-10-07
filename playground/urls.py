from django.urls import path, include
from playground.views import EventList, EventView, TicketList, CompanyList, CompanyView, EventViewSet, show_ping
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('event/', EventList.as_view()),
    path('event/<int:pk>', EventView.as_view()),
    path('ticket/<int:pk>', TicketList.as_view()),
    path('company/', CompanyList.as_view()),
    path('company/<int:pk>', CompanyView.as_view()),
    path('ping/', show_ping),

]



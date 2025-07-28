from django.urls import path
from .views import ContactMessageView

urlpatterns = [
    path('send/', ContactMessageView.as_view(), name='contact_send'),
]

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .models import ContactMessage
from .serializers import ContactMessageSerializer
from django.conf import settings

class ContactMessageView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            message = serializer.validated_data['message']

            # Email sending
            send_mail(
                subject=f"New Contact Message from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            return Response({'message': 'Message sent successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

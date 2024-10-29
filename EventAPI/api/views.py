from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from .models import User, Event, Ticket
from .serializers import UserSerializer, EventSerializer, TicketSerializer
from .permissions import IsAdminUser, IsRegularUser
from rest_framework.permissions import AllowAny

from django.db import connection
from rest_framework.decorators import api_view

class RegisterViewSet(viewsets.ModelViewSet):
    """
        ViewSet for user registration.
        Allows any user to register.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class EventViewSet(viewsets.ModelViewSet):
    """
        ViewSet for managing events.
        Admins can create new events; others can view them.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        """
        Override the get_permissions method to restrict POST requests to admins
        """
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [AllowAny()]

class PurchaseTicketView(APIView):
    """
        View for purchasing tickets for an event.
        Regular users can purchase tickets.
    """
    permission_classes = [IsRegularUser]

    def post(self, request, event_id):
        """
        Handle ticket purchase.
        Validates the quantity and updates the event and ticket records.
        """
        try:
            event = Event.objects.get(id=event_id)
            quantity = request.data.get('quantity')
            if quantity <= 0 or event.tickets_sold + quantity > event.total_tickets:
                return Response(
                    {'error': 'Invalid quantity or tickets sold out'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            ticket = Ticket.objects.create(user=request.user, event=event, quantity=quantity)
            event.tickets_sold += quantity
            event.save()
            return Response(TicketSerializer(ticket).data, status=status.HTTP_201_CREATED)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def top_events(request):
    """
    Function-based view to fetch the top 3 events by tickets sold.
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, name, date, total_tickets, tickets_sold
            FROM api_event
            ORDER BY tickets_sold DESC
            LIMIT 3;
        """)
        rows = cursor.fetchall()
        events = [{'id': row[0], 'name': row[1], 'date': row[2], 'total_tickets': row[3], 'tickets_sold': row[4]} for row in rows]

    return Response(events)
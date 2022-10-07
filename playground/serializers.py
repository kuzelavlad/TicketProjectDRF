from rest_framework import serializers
from .models import Event, Ticket, Company


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ["id", "title", "date"]
        read_only_fields = ["id",]

    def create(self, validated_data):
        validated_data["ticket_count"] = validated_data.get("ticket_count", 20)
        return super().create(validated_data)


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["id", "price", "number", "vip"]


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["title",]
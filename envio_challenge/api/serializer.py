from rest_framework import serializers

from .models import Reading


class ReadingSerializer(serializers.ModelSerializer):

    timestamp = serializers.DateTimeField(source='time')
    reading = serializers.FloatField()
    device_id = serializers.UUIDField()
    customer_id = serializers.UUIDField()

    class Meta:
        model = Reading
        fields = ('timestamp', 'reading', 'device_id', 'customer_id')


class ReadingListSerializer(serializers.ListSerializer):

    child = ReadingSerializer()

    def create(self, validated_data):
        readings = [Reading(**item) for item in validated_data]
        return Reading.objects.bulk_create(readings)


class ReadingAggrInputSerializer(serializers.Serializer):

    vars()['from'] = serializers.DateTimeField(required=False)
    to = serializers.DateTimeField(required=False)
    device_id = serializers.UUIDField(required=False)
    customer_id = serializers.UUIDField(required=False)
    aggr_size_min = serializers.IntegerField(required=False)

from rest_framework import serializers
from checkins.models import Checkin


class CheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkin
        fields = [
            'id',
            'employee_id',
            'timestamp',
        ]
        read_only_fields = ['id, timestamp']

        def create(self, validated_data: dict) -> Checkin:
            return Checkin.objects.create(**validated_data['employee_id'])

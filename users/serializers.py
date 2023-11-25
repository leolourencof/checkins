from rest_framework import serializers, validators
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model= User
        depth = 1
        fields= [
            'id',
            'username',
            'email',
            'password',
            'phone_number',
            'is_superuser',
            'checkins',
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'username': {
                'max_length': 255,
                'validators': [
                    validators.UniqueValidator(
                        queryset= User.objects.all(),
                        message='A user with that name already exists.',
                    )
                ]
            },
            'email': {
                'required': True,
                'max_length': 127,
                'validators': [
                    validators.UniqueValidator(
                        queryset= User.objects.all(),
                          message='A user with that email already exists.',
                    ),
                ],
            },
            'password': { 
                'min_length': 8,
                'max_length': 80,
                'write_only': True
            },
            'phone_number': {
                'max_digits': 11,
                'validators': [
                    validators.UniqueValidator(
                        queryset = User.objects.all(),
                        message ='A user with that phone number already exists.',
                    )
                ],
            },
        }

    def create(self, validated_data: dict) -> User:
        if validated_data['is_superuser']:
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)
    
    def update(self,  instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
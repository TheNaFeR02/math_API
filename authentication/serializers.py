from rest_framework import serializers
from .models import User, OperationLevel

class OperationLevelSerializer(serializers.ModelSerializer):
    # get user id
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = OperationLevel
        fields = ('name', 'level', 'user')


class UserSerializer(serializers.ModelSerializer):
    operation_level = OperationLevelSerializer(many=True, source='operationlevel_set')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'operation_level')

    def update(self, instance, validated_data):
        # Extract the operation_level data from validated_data
        operation_levels_data = validated_data.pop('operation_level', [])

        # Update the User model fields (e.g., username and email)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update the operationlevel_set using set()
        instance.operationlevel_set.set([])  # Clear existing related objects

        for operation_level_data in operation_levels_data:
            name = operation_level_data.get('name')
            level = operation_level_data.get('level')

            # Assuming OperationLevel has a unique identifier like 'name'
            operation_level, created = OperationLevel.objects.get_or_create(name=name, user=instance)
            operation_level.level = level
            operation_level.save()

        return instance
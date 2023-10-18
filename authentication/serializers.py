from rest_framework import serializers
from .models import User, OperationLevel, Session

class OperationLevelSerializer(serializers.ModelSerializer):
    # get user id
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = OperationLevel
        fields = ('name', 'level', 'user')


class UserSerializer(serializers.ModelSerializer):
    operation_level = OperationLevelSerializer(many=True, source='operationlevel_set', required=False)

    class Meta:
        model = User
        fields = ('username', 'email','operation_level', 'first_time_user', 'grade', 'school', 'datebirth')

   
    def update(self, instance, validated_data):
        if 'operation_level' in validated_data:
            operation_level_data = validated_data.pop('operation_level')
            for data in operation_level_data:
                OperationLevel.objects.update_or_create(
                    user=instance,
                    name=data.get('name'),
                    defaults={'level': data.get('level')}
                )
        return super(UserSerializer, self).update(instance, validated_data)
    

class SessionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    date = serializers.ReadOnlyField()
    queryset= Session.objects.all()

    class Meta:
        model = Session
        fields = ('user', 'time', 'new_level', 'old_level', 'operation', 'score', 'date')
'''module for user serializers'''

from rest_framework import serializers

from .models import MyUser

class UserCreateSerializer(serializers.ModelSerializer):
    '''
    This class is for creating the user with provided details in the request data
    '''
    class Meta:
        '''
        This is the meta class to pick the model and fields
        '''
        model = MyUser
        fields = ['username', 'email', 'gender', 'password']

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')

        user = MyUser.objects.create_user(username = username, email = email, password = password)
        if user:
            user.is_active = False
            user.gender =  validated_data.get('gender') if validated_data.get('gender') else ""
            user.save()

        return user

class UserListSerializer(serializers.ModelSerializer):
    '''
    This class is for getting the list of users.
    '''
    class Meta:
        '''
        This class is to pick the model and fields.
        '''
        model = MyUser
        fields = ['username', 'email', 'gender']
        exclude = []
        read_only_fields = []
        depth = 1

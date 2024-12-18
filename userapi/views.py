'''
This is user api class based views module.
'''

from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.urls import reverse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from .models import MyUser
from . import serializers
from .utils import token_generator
from .celery_async_tasks import account_activate_send_mail

class UserCreate(APIView):
    '''
    This class view is for creating the new user account.
    '''

    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        '''
        This function is used to create the new user account.
        Args:
            self : NA
            request(obj) : request object
            format : NA
        Returns:
            response (obj) : response object
        '''
        serialized_data = serializers.UserCreateSerializer(data = request.data)
        if serialized_data.is_valid(raise_exception = True):
            print(f"serialized data : {serialized_data.validated_data}")
            user = serialized_data.save()
            print(f"user {user.username} created successfully...")

            domain = get_current_site(request).domain   # get domain
            token = token_generator.make_token(user)    # genarate token
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))    # encode user id

            # construct activation link with uidb64, token
            link = reverse('user_activate', kwargs={'uidb64': uidb64, 'token': token})
            activation_link = 'http://'+domain+link
            task =  account_activate_send_mail.delay(user.email, user.username, activation_link)
            print('Task ID is: ',task.task_id)
        return Response({"msg":"user created successfully"},status=status.HTTP_201_CREATED)

class UserActivate(APIView):
    '''
    This class view is for activating the new user account.
    '''

    authentication_classes = []
    permission_classes = []

    def get(self, request, uidb64, token, format=None):
        '''
        This method is for activating the user account.
        Args:
            self : NA
            request(obj) : request object
            uid64 (int) : encoded user id
            token : user activation token
            format : NA
        Returns:
            response (obj) : response object
        '''

        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(MyUser, uid=uid)

        if not token_generator.check_token(user, token):
            return Response(
                {"msg":"invalid token...!"},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )

        if user.is_active:
            return Response(
                {"msg":'Account already activated, please login'},
                status=status.HTTP_200_OK
            )

        user.is_active = True
        user.email_verified = True
        user.save()

        return Response(
            {"msg": 'Account activated successfully'},
            status=status.HTTP_200_OK
        )

class UserList(APIView):
    '''
    This class is to get the list of users.
    '''

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, format=None):
        '''
        This function is used to get the list of users.
        Args:
            self : NA
            request(obj) : request object
            format : NA
        Returns:
            list : users list
        '''
        user_li = MyUser.objects.all()
        user_serialized = serializers.UserListSerializer(user_li, many = True)
        return Response(
            {"data" : user_serialized.data},
            status = status.HTTP_200_OK
        )

class UserLogout(APIView):
    '''
    This class is to balcklist refresh token to logout the user.
    '''

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        '''
        This function is used to logout the user.
        Args:
            self : NA
            request(obj) : request object
            format : NA
        Returns:
            None
        '''
        refresh_token = request.data.get("refresh")
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(
            {"msg":"user logged out successfully..!"},
            status=status.HTTP_200_OK
        )

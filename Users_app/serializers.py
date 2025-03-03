from rest_framework import serializers
from .models import Users
import sys
from django.core import exceptions
import django.contrib.auth.password_validation as validators


class  UserRegistrationSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(max_length=20, required=True)
    last_name = serializers.CharField(max_length=20, required=True)
    Date_of_birth = serializers.DateField(required=True)
    user_role = serializers.CharField(max_length=1, required=True)
    
    class Meta:

        model = Users
        fields = ['first_name', 'last_name', 'email', 'phone_no', 'Date_of_birth', 'state', 'city', 'username', 'password', 'user_role']

    def validate(self, data):
         
         user = Users(**data)
         password = data.get('password')
         
         errors = dict() 
         
         try:
             validators.validate_password(password=password, user=user)
         
         except exceptions.ValidationError as e:
             errors['password'] = list(e.messages)
         
         if errors:
             raise serializers.ValidationError(errors)
          
         return super(UserRegistrationSerializer, self).validate(data)

class  UserRegistrByPMSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(max_length=20, required=True)
    last_name = serializers.CharField(max_length=20, required=True)
    Date_of_birth = serializers.DateField(required=True)
    user_role = serializers.CharField(max_length=1, required=True)
    
    class Meta:

        model = Users
        fields = ['first_name', 'last_name', 'email', 'phone_no', 'Date_of_birth', 'state', 'city', 'username', 'user_role']

class UsersLoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=False)
    phone_no = serializers.CharField(required=False)
    username = serializers.CharField(required=False)

    class Meta:

        model = Users
        fields = ['email', 'password', 'phone_no', 'username']

    def validate(self, attrs):

        email = attrs.get('email')
        phone_no = attrs.get('phone_no')
        username = attrs.get('username')

        if email==None and phone_no==None and username==None:
            raise serializers.ValidationError("Please Enter Email or Phone_no or Username")
    
        return attrs


class UserForgotPasswordSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=False)
    phone_no = serializers.CharField(required=False)
    username = serializers.CharField(required=False)

    class Meta:
        model = Users
        fields = ['email', 'phone_no', 'username']

    def validate(self, attrs):

        email = attrs.get('email')
        phone_no = attrs.get('phone_no')
        username = attrs.get('username')

        if email == None and phone_no == None and username == None:
            raise serializers.ValidationError("Please Enter Email or Phone_no or Username")

        return attrs
    
class UserForgotPasswordChangeSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=False)
    phone_no = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=True)

    class Meta:

        model = Users
        fields = ['email', 'password', 'phone_no', 'username']

    def validate(self, attrs):

        email = attrs.get('email')
        phone_no = attrs.get('phone_no')
        username = attrs.get('username')

        if email==None and phone_no==None and username==None:
            raise serializers.ValidationError("Please Enter Email or Phone_no or Username")
    
        return attrs
    
class UsersUpdateSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=False)
    phone_no = serializers.CharField(required=False)

    class Meta:
        model = Users
        fields = ['first_name', 'last_name','Date_of_birth','image','email','phone_no']

class UserAllDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['date_joined' , 'first_name', 'last_name','username', 'email', 'phone_no', 'Date_of_birth', 'state', 'city', 'image', 'is_email_verified', 'is_phno_verified', 'user_account_status', 'user_status']

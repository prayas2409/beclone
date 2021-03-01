from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from online_assessment.settings import EMAIL_HOST_USER
import random

# Create your views here.
class Login(APIView):

    def post(self,request):
        email = request.data.get('email')
        name = request.data.get('name')
        otp = random.randint(100000,999999)
        print(otp)
        send_mail(
        'Account verification',
        '{} is your otp for verification of your account'.format(otp),
        EMAIL_HOST_USER,
        [email],
        fail_silently=False,
        )
        response = "Email with OTP has been sent to you on {}".format(name,email)

        return Response(response)   
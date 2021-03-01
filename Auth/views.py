from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from online_assessment.settings import EMAIL_HOST_USER
from rest_framework import status
from django.utils.datastructures import MultiValueDictKeyError
import random

# Create your views here.
class Login(APIView):

    def post(self,request):
        """[Post API to get user details and send otp via email]

        Args:
            request ([Request]): [Request body should contain EmailId and Name of user]

        Returns:
            [Response]: [Send meesage for confirmation or error while registering]
        """
        try:
            email = request.data['email']
            name = request.data['name']
            otp = random.randint(100000,999999)
            send_mail(
            'Account verification',
            '{} is your otp for verification of your account'.format(otp),
            EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            )
            response = "Email with OTP has been sent to you on {}".format(name,email)

            return Response(response,status=status.HTTP_202_ACCEPTED)
        except MultiValueDictKeyError as e:
            Response("Please enter email and name",status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(type(e))
            Response("Something went wrong please try again later",status=status.HTTP_400_BAD_REQUEST)
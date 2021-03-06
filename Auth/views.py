from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from online_assessment.settings import EMAIL_HOST_USER
from rest_framework import status
from django.utils.datastructures import MultiValueDictKeyError
import random
from online_assessment.settings import REDIS_HOST,REDIS_PASSWORD,REDIS_PORT
import redis
from online_assessment.project_cache import Cache

# Create your views here.
cache=Cache(redis.Redis(host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD))

class Login(APIView):
    
    def post(self, request):
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
            data = {"otp_{}".format(email):otp}
            cache.set(data)
            send_mail(
                'Account verification',
                '{} is your otp for verification of your account'.format(otp),
                EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            response = "Email with OTP has been sent to you on {}".format(name,email)
            print(cache.get("otp_{}".format(email)))
            return Response(response, status=status.HTTP_202_ACCEPTED)
        except MultiValueDictKeyError as e:
            return Response("Please enter both email and name", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response("Something went wrong please try again later",
                            status=status.HTTP_400_BAD_REQUEST)


class VerifyUser(APIView):

    def post(self, request):
        """[Post API to verify the OTP sent via email]

        Args:
            request ([Request]): [Request body should contain EmailId and the OTP]

        Returns:
            [Response]: [Send message whether the otp was successfully verified ]
        """

        try:
            email = request.data["email"]
            otp = request.data["otp"]
            key = "otp_{}".format(email)
            # get the actual otp from redis
            if otp == cache.get(key).decode():
                # save it in the db
                return Response("Login was Successful",
                                status=status.HTTP_202_ACCEPTED)
            else:
                return Response("OTP's don't match",
                                status=status.HTTP_400_BAD_REQUEST)
        except MultiValueDictKeyError as e:
            return Response("Please enter both email and OTP",
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response("Something went wrong please try again",
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

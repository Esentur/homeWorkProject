from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.account.serializers import *


class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        serializers = RegisterSerializer(data=data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return (Response('Вы успешно зареганы и вам отправлен email c активационным кодом', status=201))

class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'Аккаунт успешно активирован, т.к. перешел по ссылке и сделал GET запрос'}, status=200)
        except User.DoesNotExist:
            return Response({'msg': 'Неверный активационный код!'}, status=400)

class LoginApiView(ObtainAuthToken):
    serializer_class = LoginSerializer

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializers = ChangePasswordSerializer(data=request.data,
                                                   context={'request': request})

        serializers.is_valid(raise_exception=True)
        serializers.set_new_password()
        return Response('Пароль успешно изменен!')


# class ForgotPasswordView(APIView):
#     def post(self, request):
#         serializers = ForgotPasswordSerializer(data=request.data,
#                                                context={'request': request})
#
#         if serializers.is_valid(raise_exception=True):
#             serializers.save()
#             return Response('Пароль отправлен вам на почту !')
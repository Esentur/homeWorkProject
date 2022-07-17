from django.urls import path
from apps.account.views import *

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationView.as_view()),
    path('login/', LoginApiView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    # path('forgot_password/', ForgotPasswordView.as_view()),

]

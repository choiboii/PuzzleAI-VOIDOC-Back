from django.urls import path

from users.views import ActivateUserView, ForgotPasswordView, PasswordChangeView, SignUpView, LoginView, CheckDuplicateEmailView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/login', LoginView.as_view()),
    path('/check_duplicate', CheckDuplicateEmailView.as_view()),
    path('/change_password/<uid>/<token>', PasswordChangeView.as_view(), name='change'),
    path('/activate/<uid>/<token>', ActivateUserView.as_view(), name='activate'),
    path('/forgot_password', ForgotPasswordView.as_view())
]
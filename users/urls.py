from django.urls import path

from users.views import ActivateUserView, PasswordChangeView, SignUpView, LoginView, CheckDuplicateEmailView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/login', LoginView.as_view()),
    path('/check_duplicate', CheckDuplicateEmailView.as_view()),
    path('/password_change', PasswordChangeView.as_view()),
    path('/activate/<uid>/<token>', ActivateUserView.as_view(), name='activate')  
]
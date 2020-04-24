from django.urls import path

from EUIVUserManagement.rest.views import EuIVUserProfileList, ResetEuUserPassword, EuIVSimpleUsersList

urlpatterns = [
    path('users/', EuIVUserProfileList.as_view(), name='list_users'),
    path('platform_users/', EuIVSimpleUsersList.as_view(), name='list_platform_users'),
    path('reset_password/<int:pk>/', ResetEuUserPassword.as_view(), name='reset_password'),
]

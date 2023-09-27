# authentication/urls.py

from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView
from django.urls import include, path
from rest_framework.routers import DefaultRouter
# from .views import UserDetailsView
from .views import UserViewSet, OperationLevelViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet,basename="user_details")
router.register(r'operation_level', OperationLevelViewSet,basename="user_level")


urlpatterns = [
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path('dj-rest-auth/', include('dj_rest_auth.urls')), # include other dj_rest_auth urls
    # path('api-auth/', include('rest_framework.urls')),
    # path("user/", UserDetailsView.as_view(), name="rest_user_details"),
    path('', include(router.urls)),
]
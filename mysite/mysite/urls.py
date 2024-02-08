from django.contrib import admin
from django.urls import path, include
from user_reg.views import *
from main.views import *
from django.contrib import admin
from main.views import*
from django.urls import path,include
from rest_framework import routers
from user_reg.models import *
router = routers.DefaultRouter()
router.register(r'Clients', ClientsViewSet)
router.register(r'RoomsCategory', RoomsCategoryViewSet)
router.register(r'RoomsCondition', RoomsConditionViewSet)
router.register(r'Post', PostViewSet)
router.register(r'Employess', EmployessViewSet)
router.register(r'Payment', PaymentViewSet)


zxc = [
    path('project/', include(router.urls))
]

admin.autodiscover()


urlpatterns=[
    path('admin/', admin.site.urls),
    path('', include(zxc)),
    path('login/', AuthorizationUserView.as_view(), name='login'),
    path('registr/', RegistrationUserView.as_view(), name='registr'),
]   

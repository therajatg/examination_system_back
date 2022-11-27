from django.contrib import admin
from django.urls import path,include
from . import views
from .views import StudentViewSet
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'student', StudentViewSet)
urlpatterns = [    
    path('',include(router.urls)),
]


# Here since in path we gave empty and included router.urls, the router will automaticaly set student since we registered student and finally we'll have this path: url/student/
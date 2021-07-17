"""studentmanagementdjangobackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import views
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    # path('', views.apiOverview,name="apiOverview"),
    path('list/', views.getUsers,name="list"),
    path('get-by-id/<int:id>',views.getById,name='get-by-id'),
    path('add-new/',views.addNewUser,name="add-new"),
    path('update-user/<int:id>',views.updateUser,name="update-user"),
    path('delete-user/<int:id>',views.deleteById,name="delete-user"),
    path('sign-in/',views.signIn,name="sign-in"),
    path('user-sign-in/',views.signIn1,name="sign-in")
]

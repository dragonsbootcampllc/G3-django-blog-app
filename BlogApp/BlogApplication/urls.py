from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('login', views.loginView, name='login'),
    path('', views.welcome, name='welcome'),
    path('showPosts', views.index, name='posts'),
    path('addaPost/', views.addPost, name='addPost'),
    path('editPost/<int:pk>', views.editPost, name='edit'),
    path('delete/<int:pk>', views.deletePost, name='delete'),
    path('postDetails/<int:pk>', views.postDetails, name='details'),
    path('publishPost/<int:pk>', views.publishPost, name='publishPost'),
    path('ShowCategories', views.showCategories, name='categories'),
    path('addaComment/<int:pk>', views.addComment, name='addComment'),
    path('addaCategory/', views.addCategory, name='addCategory'),
    path('editaCategory/<int:pk>', views.editCategory, name='editCategory'),
    path('deleteaCategory/<int:pk>', views.deleteCategory, name='deleteCategory'),
    path('chooseCategory/', views.chooseCategory, name='chooseCategory'),
    path('createCompany/', views.createCompany, name='createCompany'),
    path('ShowCompanies', views.showCompanies, name='companies'),
    path('companyDetails/<int:pk>', views.companyDetails, name='CompanyDetails'),
]

from django.urls import path
from .views import listing_list, add_listing, register, profile
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', listing_list, name='listing_list'),
    path('add/', add_listing, name='add_listing'),  # 新しいURLパターンを追加
    path('login/', auth_views.LoginView.as_view(template_name='listings/register.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # ログアウトビューを追加
    path('profile/', profile, name='profile'),  # プロファイルページのURLパターンを追加
]
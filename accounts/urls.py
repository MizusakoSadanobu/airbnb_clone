from django.urls import path
from .views import register, login_view, guest_profile, owner_profile

app_name = 'accounts'  # 名前空間を設定

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),  # ログインビューの名前を定義
    path('guest_profile/', guest_profile, name='guest_profile'),
    path('owner_profile/', owner_profile, name='owner_profile'),
]

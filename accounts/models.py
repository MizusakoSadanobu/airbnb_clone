from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('guest', 'Guest'),
        ('owner', 'Owner'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    is_owner = models.BooleanField(default=False)  # 宿オーナーかどうかを示すフィールド
        # 他のフィールドも追加できます

    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"


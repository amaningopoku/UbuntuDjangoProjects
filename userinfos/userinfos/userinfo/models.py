from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class ProfilePicture(models.Model):
    img = models.ImageField(upload_to='user_profile')
    pic_name = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.pic_name.username
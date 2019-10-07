from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()

class Message(models.Model):
    auther = models.ForeignKey(User,related_name='auther_message', on_delete= models.CASCADE)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add= True) 

    def __str__(self):
        return auther.username

    def last_10_Msg(self):
        return Message.objects.order_by('-timestamp').all()[:10]    






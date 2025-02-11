from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class CustomUser(User):
    image=models.ImageField(upload_to='static/imgs/',null=True,blank=True)
    phone=models.IntegerField(null=True)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):       
        # xoa file hinh khi update
        if self.image:
            try:
                this = CustomUser.objects.get(id=self.id)
                if this.image != self.image:
                    if os.path.isfile(this.image.path):
                        os.remove(this.image.path)
            except:
                pass
        return super().save(*args, **kwargs)        

        super().save(*args, **kwargs)
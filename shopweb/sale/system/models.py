from django.db import models
from django.utils import timezone
import os
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=90)
    keywords = models.CharField(max_length=160)
    desc = models.CharField(max_length=160)
    slug = models.SlugField(max_length=160)
    parent=models.ForeignKey('self',null=True,blank=True,related_name='children',on_delete=models.SET_NULL)
    image=models.ImageField(null=True,blank=True,upload_to='static/imgs/')
    status=models.IntegerField()
    created=models.DateField(null=True)
    updated=models.DateField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        # xoa file hinh khi update
        if self.image:
            try:
                this = Category.objects.get(id=self.id)
                if this.image != self.image:
                    if os.path.isfile(this.image.path):
                        os.remove(this.image.path)
            except:
                pass
        return super().save(*args, **kwargs)        

        super().save(*args, **kwargs)


    def __str__(self):
        return self.title
    

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)


# model san pham
class Product(models.Model):
    name=models.CharField(max_length=100)
    keyword=models.CharField(max_length=150)
    # decription=models.CharField(max_length=256)
    decription=RichTextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    image=models.ImageField(upload_to='static/imgs/',null=True,blank=True)
    status=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        # xoa file hinh khi update
        if self.image:
            try:
                this = Product.objects.get(id=self.id)
                if this.image != self.image:
                    if os.path.isfile(this.image.path):
                        os.remove(this.image.path)
            except:
                pass
        return super().save(*args, **kwargs)        

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

class Config(models.Model):
    name=models.CharField(max_length=100)
    keyword=models.CharField(max_length=150)
    decription=models.CharField(max_length=256)
    domain=models.CharField(max_length=256)
    email=models.CharField(max_length=256)
    past_mail=models.CharField(max_length=256)
    host_mail=models.CharField(max_length=256)
    active=models.BooleanField(default=False)
    note=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='static/imgs/',null=True,blank=True)


    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        # xoa file hinh khi update
        if self.image:
            try:
                this = Config.objects.get(id=self.id)
                if this.image != self.image:
                    if os.path.isfile(this.image.path):
                        os.remove(this.image.path)
            except:
                pass
        return super().save(*args, **kwargs)        

        super().save(*args, **kwargs)

# model cartitem
class CartItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    
    def get_total_price(self):
        return self.quantity * float(self.product.price)
from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0.00) # Nuevo campo para el precio
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name
   
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email_del_cliente = models.EmailField()
    nombre_del_cliente = models.CharField(max_length=64)
    mensaje = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_del_cliente    
    
    
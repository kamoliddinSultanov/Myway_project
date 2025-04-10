from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Car(models.Model):
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return self.title

@receiver(post_save, sender=Car)
def update_car_in_es(sender, instance, **kwargs):
    doc = {
        "id": instance.id,
        "title": instance.title,
        "brand": instance.brand,
        "model": instance.model,
        "price": float(instance.price),
        "description": instance.description,
        "image": instance.image.url if instance.image else None
    }
    es.index(index="cars", id=instance.id, document=doc)

@receiver(post_delete, sender=Car)
def delete_car_from_es(sender, instance, **kwargs):
    es.delete(index="cars", id=instance.id)
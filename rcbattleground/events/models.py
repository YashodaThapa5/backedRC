from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Create your models here.
class Category(models.Model):
  name=models.CharField(max_length=100 , unique=True) 
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.name
  
# events model
class Event(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')
  name=models.CharField(max_length=200 , unique=True)
  description=models.TextField()
  price=models.DecimalField(max_digits=10, decimal_places=2)
  event_date=models.DateTimeField()
  event_start_time = models.DateTimeField()
  event_end_time = models.DateTimeField(null=True, blank=True)
  event_seats=models.IntegerField(default=0)
  image=models.ImageField(upload_to='event_images/')
  video=models.FileField(upload_to='event_videos/ ', null=True, blank=True)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)
  
  
  def __str__(self):
    return self.name
  
  # delete event video and image when event is deleted
@receiver(post_save, sender=Event)
def delete_event_end_time(sender, instance, created, **kwargs):
     if instance.image:
        instance.image.delete(save=False)
     if instance.video:
        instance.video.delete(save=False)
  
# delete old image when product image changes
@receiver(pre_save, sender=Event)
def delete_old_image_on_change(sender, instance, **kwargs):
    """
    pre_save → runs before saving a Product instance.
    Used to remove old image when a new image is uploaded.
    """

    if not instance.pk:
        # Skip if this is a new product (no previous image)
        return

    try:
        # Get the old image before update
        old_image = Event.objects.get(pk=instance.pk).image
    except Event.DoesNotExist:
        return

    new_image = instance.image

    # Compare old and new images — if different, delete the old one
    if old_image and old_image != new_image:
        old_image.delete(False)  
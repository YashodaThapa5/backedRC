from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='events',
        null=True,
        blank=True
    )
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    event_date = models.DateTimeField()
    event_start_time = models.DateTimeField()
    event_end_time = models.DateTimeField(null=True, blank=True)
    event_seats = models.IntegerField(default=0)
    image = models.ImageField(upload_to='event_images/')
    video = models.FileField(upload_to='event_videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Slot(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='slots',
        null=True,
        blank=True
    )
    slotTitle = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    maximumseats = models.IntegerField()
    times = models.JSONField()
    image = models.ImageField(upload_to='slot_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slotTitle


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_bookings')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField()
    booking_time = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['event', 'booking_date', 'booking_time', 'user'],
                name='unique_event_booking'
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.event.name} - {self.booking_date} {self.booking_time}"


class SlotBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default="pending")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['slot', 'booking_date', 'booking_time', 'user'],
                name='unique_slot_booking'
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.slot.slotTitle} - {self.booking_date} {self.booking_time}"


@receiver(post_delete, sender=Event)
def delete_event_files(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)
    if instance.video:
        instance.video.delete(save=False)


@receiver(pre_save, sender=Event)
def delete_old_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_image = Event.objects.get(pk=instance.pk).image
    except Event.DoesNotExist:
        return

    new_image = instance.image

    if old_image and old_image != new_image:
        old_image.delete(False)


@receiver(post_delete, sender=Slot)
def delete_slot_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)


@receiver(pre_save, sender=Slot)
def delete_old_slot_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_image = Slot.objects.get(pk=instance.pk).image
    except Slot.DoesNotExist:
        return

    new_image = instance.image

    if old_image and old_image != new_image:
        old_image.delete(False)
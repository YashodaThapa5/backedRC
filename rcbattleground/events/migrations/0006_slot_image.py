# Generated manually for adding image field to Slot model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_slot_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='slot_images/'),
        ),
    ]
# Generated manually for adding category to Slot model

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_slot_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='events.category'),
        ),
    ]
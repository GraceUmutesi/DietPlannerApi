# Generated by Django 4.0.5 on 2022-07-19 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meal_plan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryList',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('foods', models.JSONField(blank=True, default=list)),
                ('estimated_total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('meal_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal_plan.mealplan')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

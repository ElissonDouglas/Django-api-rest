# Generated by Django 4.1.6 on 2023-02-03 14:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id_album', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255)),
                ('release_year', models.IntegerField()),
                ('info', models.TextField(blank=True, max_length=500)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

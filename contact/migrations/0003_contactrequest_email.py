# Generated by Django 3.0.5 on 2020-05-02 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20200502_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactrequest',
            name='email',
            field=models.EmailField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
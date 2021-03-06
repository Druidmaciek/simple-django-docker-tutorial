# Generated by Django 3.0.5 on 2020-05-02 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactrequest',
            name='answer',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default=('yes', 'Yes'), max_length=3),
        ),
        migrations.AlterField(
            model_name='contactrequest',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contactrequest',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]

# Generated by Django 3.0.5 on 2020-05-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.IntegerField()),
                ('last_name', models.IntegerField()),
                ('answer', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('message', models.CharField(max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 2.2.1 on 2019-10-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0024_verifyworkflow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifyworkflow',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
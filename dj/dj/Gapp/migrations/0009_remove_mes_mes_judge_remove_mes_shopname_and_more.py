# Generated by Django 4.2.1 on 2023-07-21 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gapp', '0008_mes_shopname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mes',
            name='Mes_judge',
        ),
        migrations.RemoveField(
            model_name='mes',
            name='ShopName',
        ),
        migrations.AddField(
            model_name='mes',
            name='Shop_Name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='mes',
            name='Mes_Suspicious',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='shopinformation',
            name='ShopInformation_Name',
            field=models.CharField(default='', max_length=500),
        ),
    ]
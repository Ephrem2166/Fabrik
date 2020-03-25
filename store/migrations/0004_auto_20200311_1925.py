# Generated by Django 2.1.5 on 2020-03-11 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('XS', 'X-Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X-Large')], max_length=1),
        ),
    ]

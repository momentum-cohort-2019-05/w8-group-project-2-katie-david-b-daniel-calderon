# Generated by Django 2.2.3 on 2019-07-23 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190723_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(null=True),
        ),
    ]

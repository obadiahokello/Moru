# Generated by Django 4.2.4 on 2024-02-14 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moru', '0003_rename_footercontact_footer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='content',
            field=models.CharField(max_length=1000),
        ),
    ]

# Generated by Django 4.0.10 on 2023-10-02 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApplication', '0004_blogcategory_blogpost_draft_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

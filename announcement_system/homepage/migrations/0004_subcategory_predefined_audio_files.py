# Generated by Django 5.0.4 on 2024-05-03 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_rename_template_es_subcategory_template_kg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='predefined_audio_files',
            field=models.JSONField(default=list),
        ),
    ]
# Generated by Django 5.0.6 on 2024-05-18 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phishing', '0005_alter_phishing_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phishing',
            name='html',
            field=models.FileField(blank=True, upload_to='baliqchi/attacks/phishing/templates/phishing/d8a31dba-0251-4e91-a864-511527934ae1/'),
        ),
        migrations.AlterField(
            model_name='phishing',
            name='url',
            field=models.CharField(max_length=255),
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-18 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phishing', '0003_alter_phishing_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phishing',
            name='html',
            field=models.FileField(blank=True, upload_to='baliqchi/staticfiles/phishing_pages/cfd7a9d0-00b4-443c-9322-2b9917d498c7/'),
        ),
    ]
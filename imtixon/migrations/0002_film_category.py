# Generated by Django 4.2.1 on 2023-08-23 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imtixon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imtixon.category'),
        ),
    ]

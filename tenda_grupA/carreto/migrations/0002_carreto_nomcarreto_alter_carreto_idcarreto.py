# Generated by Django 4.2 on 2023-05-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carreto',
            name='nomCarreto',
            field=models.CharField(default=None, max_length=50, verbose_name='nomCarreto'),
        ),
        migrations.AlterField(
            model_name='carreto',
            name='idCarreto',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]

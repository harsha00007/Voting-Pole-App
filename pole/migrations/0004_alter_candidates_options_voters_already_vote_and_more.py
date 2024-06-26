# Generated by Django 5.0.6 on 2024-06-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pole', '0003_alter_voters_card_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidates',
            options={'verbose_name_plural': 'Candidates'},
        ),
        migrations.AddField(
            model_name='voters',
            name='already_vote',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='voters',
            name='card_number',
            field=models.CharField(default='TTX6192713', max_length=10, unique=True),
        ),
    ]

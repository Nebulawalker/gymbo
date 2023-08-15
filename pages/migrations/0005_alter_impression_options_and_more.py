# Generated by Django 4.2.4 on 2023-08-15 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_impression_content_block_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='impression',
            options={'verbose_name': 'Показ', 'verbose_name_plural': 'Показы'},
        ),
        migrations.RemoveField(
            model_name='impression',
            name='impressions_quantity',
        ),
        migrations.AddField(
            model_name='impression',
            name='quantity',
            field=models.IntegerField(default=0, editable=False, verbose_name='Количество показов на конкретной странице'),
        ),
    ]

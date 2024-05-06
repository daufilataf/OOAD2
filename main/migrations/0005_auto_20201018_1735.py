# Generated by Django 3.0.7 on 2020-10-18 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_item_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='tag',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], max_length=1, null=True),
        ),
    ]
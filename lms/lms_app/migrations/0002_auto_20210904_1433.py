# Generated by Django 3.1.3 on 2021-09-04 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_rental',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

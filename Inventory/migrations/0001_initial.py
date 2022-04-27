# Generated by Django 3.2.13 on 2022-04-26 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('book_name_to_be_issued', models.CharField(max_length=200)),
                ('book_rental', models.IntegerField()),
                ('date_issued', models.DateField()),
                ('no_of_books_issued', models.IntegerField()),
            ],
        ),
    ]

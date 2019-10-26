# Generated by Django 2.2.6 on 2019-10-25 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('price', models.CharField(max_length=100)),
                ('date_begin', models.DateField()),
                ('date_end', models.DateField()),
                ('pays', models.CharField(max_length=10)),
                ('ville', models.CharField(max_length=10)),
                ('adress', models.TextField()),
                ('phone', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='templates/images')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('pays', models.CharField(max_length=10)),
                ('ville', models.CharField(max_length=10)),
                ('adress', models.TextField()),
                ('image', models.ImageField(upload_to='templates/images')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('type_food', models.CharField(max_length=100)),
                ('rate', models.IntegerField()),
                ('pays', models.CharField(max_length=10)),
                ('ville', models.CharField(max_length=10)),
                ('adress', models.TextField()),
                ('phone', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='templates/images')),
            ],
        ),
    ]
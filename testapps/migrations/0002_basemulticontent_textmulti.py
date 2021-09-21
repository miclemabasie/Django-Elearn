# Generated by Django 3.0 on 2021-09-21 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasemultiContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TextMulti',
            fields=[
                ('basemulticontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapps.BasemultiContent')),
                ('body', models.TextField()),
            ],
            bases=('testapps.basemulticontent',),
        ),
    ]

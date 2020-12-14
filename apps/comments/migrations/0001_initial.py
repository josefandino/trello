# Generated by Django 3.1.4 on 2020-12-12 22:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('list', '0001_initial'),
        ('cards', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=150)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha registro')),
                ('card', models.ManyToManyField(related_name='comments', to='cards.Card')),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='list.list')),
                ('members', models.ManyToManyField(related_name='comments', to='users.User')),
            ],
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispensary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=30)),
                ('studentnumber', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
                ('reisterdate', models.DateField(auto_now_add=True)),
                ('reason_for_visit', models.TextField(default='', null=True)),
                ('studentstatus', models.CharField(choices=[('registered', 'Registered'), ('not_registered', 'Not Registered')], max_length=20)),
                ('password', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]

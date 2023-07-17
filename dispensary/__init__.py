from django.db import migrations, models

def set_default_studentstatus(apps, schema_editor):
    Student = apps.get_model('your_app_name', 'Student')
    Student.objects.filter(studentstatus=None).update(studentstatus='registered')

class Migration(migrations.Migration):

    dependencies = [
        ('dispensary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='studentstatus',
            field=models.CharField(default='', max_length=255),  # Update max_length as per your requirements
            preserve_default=False,
        ),
        migrations.RunPython(set_default_studentstatus),
    ]

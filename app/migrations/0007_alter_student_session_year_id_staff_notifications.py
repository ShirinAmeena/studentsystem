# Generated by Django 5.1.2 on 2024-11-13 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_session_year_session_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='session_year_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.session_year'),
        ),
        migrations.CreateModel(
            name='Staff_Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.staff')),
            ],
        ),
    ]

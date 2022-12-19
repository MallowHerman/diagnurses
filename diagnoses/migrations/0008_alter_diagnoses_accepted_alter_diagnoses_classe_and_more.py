# Generated by Django 4.1.4 on 2022-12-17 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diagnoses', '0007_alter_classes_id_alter_diagnoses_id_alter_domains_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnoses',
            name='accepted',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='diagnoses',
            name='classe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diagnoses.classes'),
        ),
        migrations.AlterField(
            model_name='diagnoses',
            name='definition',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='diagnoses',
            name='diagnosis_code',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='diagnoses',
            name='domain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diagnoses.domains'),
        ),
        migrations.AlterField(
            model_name='diagnoses',
            name='slug',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
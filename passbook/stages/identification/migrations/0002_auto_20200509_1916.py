# Generated by Django 3.0.3 on 2020-05-09 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("passbook_stages_identification", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="identificationstage",
            name="template",
            field=models.TextField(choices=[("login/form.html", "Default Login")]),
        ),
    ]

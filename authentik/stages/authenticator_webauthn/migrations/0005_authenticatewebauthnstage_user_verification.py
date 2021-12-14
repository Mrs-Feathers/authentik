# Generated by Django 4.0 on 2021-12-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_stages_authenticator_webauthn", "0004_auto_20210304_1850"),
    ]

    operations = [
        migrations.AddField(
            model_name="authenticatewebauthnstage",
            name="user_verification",
            field=models.TextField(
                choices=[
                    ("required", "Required"),
                    ("preferred", "Preferred"),
                    ("discouraged", "Discouraged"),
                ],
                default="preferred",
            ),
        ),
    ]

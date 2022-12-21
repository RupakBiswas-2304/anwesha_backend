# Generated by Django 4.1.2 on 2022-12-21 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "0001_initial"),
        ("event", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "team_id",
                    models.CharField(
                        max_length=10, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("team_name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "event_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="event.events"
                    ),
                ),
                (
                    "leader_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Payer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "payment_status",
                    models.CharField(
                        choices=[
                            ("paid", "paid"),
                            ("unpaid", "unpaid"),
                            ("pending", "pending"),
                        ],
                        default="unpaid",
                        max_length=10,
                    ),
                ),
                ("reference_id", models.CharField(max_length=100)),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                (
                    "payer_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.user"
                    ),
                ),
                (
                    "team_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="participant.team",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Participant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "anwesha_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.user",
                    ),
                ),
                (
                    "event_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="event.events",
                    ),
                ),
                (
                    "team_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="participant.team",
                    ),
                ),
            ],
        ),
    ]

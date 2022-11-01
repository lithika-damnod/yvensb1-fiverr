# Generated by Django 4.0.4 on 2022-11-01 02:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('u_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_name', models.TextField()),
                ('l_name', models.TextField()),
                ('age', models.IntegerField()),
                ('address_no', models.IntegerField()),
                ('address_street', models.TextField()),
                ('address_city', models.TextField()),
                ('address_country', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('number_plate', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('a_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('price_per_km', models.IntegerField()),
                ('posted_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.car')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
    ]

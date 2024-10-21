# Generated by Django 5.0.6 on 2024-10-21 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('auction_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('beneficiary', models.CharField(max_length=100)),
                ('auction_type', models.CharField(choices=[('classic', 'Классический аукцион'), ('blind', 'Закрытый аукцион'), ('dutch', 'Голландский аукцион')], max_length=10)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=255)),
                ('contacts', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AuctionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('starting_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('finish_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('auction_date', models.DateTimeField()),
            ],
        ),
    ]
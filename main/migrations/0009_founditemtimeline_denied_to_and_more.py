# Generated by Django 4.2.7 on 2023-12-04 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_founditem_owner_collected'),
    ]

    operations = [
        migrations.AddField(
            model_name='founditemtimeline',
            name='denied_to',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='founditemtimeline',
            name='show_buttons',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='founditemtimeline',
            name='activity_type',
            field=models.CharField(choices=[('reported', 'Item Reported'), ('denied', 'Item Denied to User'), ('claimed', 'Item Claimed'), ('verified', 'User Verified'), ('collected', 'Item Collected')], max_length=10),
        ),
    ]
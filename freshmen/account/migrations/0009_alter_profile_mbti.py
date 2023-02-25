# Generated by Django 3.2.18 on 2023-02-24 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_profile_mbti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mbti',
            field=models.CharField(choices=[('INFP', 'INFP'), ('ESFJ', 'ESFJ'), ('ENTP', 'ENTP'), ('ENFJ', 'ENFJ'), ('ISFJ', 'ISFJ'), ('INTJ', 'INTJ'), ('INTP', 'INTP'), ('ESTJ', 'ESTJ'), ('ISTJ', 'ISTJ'), ('ENFP', 'ENFP'), ('ISFP', 'ISFP'), ('INFJ', 'INFJ'), ('ESTP', 'ESTP'), ('ESFP', 'ESFP'), ('ENTJ', 'ENTJ'), ('ISTP', 'ISTP')], max_length=16, null=True),
        ),
    ]

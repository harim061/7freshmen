# Generated by Django 3.2.18 on 2023-02-24 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_profile_mbti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('female', '여성'), ('male', '남성')], max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mbti',
            field=models.CharField(choices=[('ISFP', 'ISFP'), ('INTJ', 'INTJ'), ('ESFJ', 'ESFJ'), ('ESTJ', 'ESTJ'), ('ENFJ', 'ENFJ'), ('ENFP', 'ENFP'), ('ESTP', 'ESTP'), ('ISTJ', 'ISTJ'), ('ESFP', 'ESFP'), ('ENTP', 'ENTP'), ('INTP', 'INTP'), ('INFP', 'INFP'), ('ISTP', 'ISTP'), ('INFJ', 'INFJ'), ('ISFJ', 'ISFJ'), ('ENTJ', 'ENTJ')], max_length=16, null=True),
        ),
    ]

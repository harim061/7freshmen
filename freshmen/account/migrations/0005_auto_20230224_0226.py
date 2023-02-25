# Generated by Django 3.2.18 on 2023-02-24 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20230224_0226'),
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
            field=models.CharField(choices=[('ENTJ', 'ENTJ'), ('ENFP', 'ENFP'), ('ESTP', 'ESTP'), ('ENTP', 'ENTP'), ('ISTJ', 'ISTJ'), ('ISFP', 'ISFP'), ('INTJ', 'INTJ'), ('INFP', 'INFP'), ('ESFJ', 'ESFJ'), ('ISFJ', 'ISFJ'), ('ENFJ', 'ENFJ'), ('ISTP', 'ISTP'), ('INTP', 'INTP'), ('INFJ', 'INFJ'), ('ESFP', 'ESFP'), ('ESTJ', 'ESTJ')], max_length=16, null=True),
        ),
    ]

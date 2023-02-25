# Generated by Django 3.2.18 on 2023-02-24 02:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SolveQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('solve_num', models.IntegerField(default=0)),
                ('answer', models.CharField(default='', max_length=30)),
                ('quiz_writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quesmodel')),
            ],
        ),
    ]

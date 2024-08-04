# Generated by Django 5.0.7 on 2024-08-04 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=512)),
                ('journal', models.CharField(blank=True, default='', max_length=512, null=True)),
                ('pub_date', models.CharField(blank=True, default='', max_length=32, null=True)),
                ('pub_year', models.IntegerField(blank=True, default=None, null=True)),
                ('doi', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('pmid', models.CharField(blank=True, default='', max_length=32, null=True)),
                ('article_type', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('description', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('novelty', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('limitation', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('research_goal', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('research_objects', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('field_category', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('disease_category', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('technique', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('model_type', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('data_type', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('sample_size', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
    ]
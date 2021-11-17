# Generated by Django 3.2.9 on 2021-11-17 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journalist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('image_profile', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('E', 'Editando'), ('P', 'Publicado'), ('B', 'Bloqueado')], default='E', max_length=2)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('publish_date', models.DateTimeField(null=True)),
                ('last_update_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=300)),
                ('main_image', models.ImageField(null=True, upload_to='')),
                ('write_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPaperApp.journalist')),
            ],
        ),
        migrations.AddField(
            model_name='journalist',
            name='thems',
            field=models.ManyToManyField(to='NewsPaperApp.Theme'),
        ),
    ]

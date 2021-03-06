# Generated by Django 2.0.1 on 2018-03-25 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apollo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=600)),
                ('src', models.TextField()),
                ('order', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apollo.Image'),
        ),
        migrations.AlterField(
            model_name='image',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apollo.Gallery'),
        ),
    ]

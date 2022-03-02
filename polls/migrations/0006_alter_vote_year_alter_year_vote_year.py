# Generated by Django 4.0.2 on 2022-03-02 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_rename_years_year_rename_year_year_vote_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.year'),
        ),
        migrations.AlterField(
            model_name='year',
            name='vote_year',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

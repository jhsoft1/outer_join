# Generated by Django 4.0.2 on 2022-03-02 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_years_alter_vote_voter'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Years',
            new_name='Year',
        ),
        migrations.RenameField(
            model_name='year',
            old_name='year',
            new_name='vote_year',
        ),
    ]

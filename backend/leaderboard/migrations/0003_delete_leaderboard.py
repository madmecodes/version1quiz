# Generated migration to delete Leaderboard model
# Using UserProgress from quiz app instead for single source of truth

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0002_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Leaderboard',
        ),
    ]

# Generated migration to clear Google URLs from avatar field

from django.db import migrations


def clear_google_urls(apps, schema_editor):
    """Clear avatar fields that contain Google URLs (not local files)"""
    CustomUser = apps.get_model('users', 'CustomUser')
    users_to_update = CustomUser.objects.filter(avatar__startswith='https://')
    count = users_to_update.count()
    users_to_update.update(avatar='')
    print(f"Cleared {count} users with Google avatar URLs")


def reverse_clear(apps, schema_editor):
    """No-op reverse migration"""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_avatar'),
    ]

    operations = [
        migrations.RunPython(clear_google_urls, reverse_clear),
    ]

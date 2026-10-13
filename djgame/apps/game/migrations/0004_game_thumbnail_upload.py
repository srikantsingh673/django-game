import django.core.validators
from django.db import migrations, models


def clear_url_thumbnails(apps, schema_editor):
    # Values from the old URL field (e.g. '/static/…', 'https://…') aren't uploads; blank shows the default
    Game = apps.get_model('game', 'Game')
    Game.objects.exclude(thumbnail='').exclude(thumbnail__startswith='game/thumbnails/').update(thumbnail='')


class Migration(migrations.Migration):
    """
    thumbnail_url (a URL string) becomes thumbnail (an uploaded image file).
    """

    dependencies = [
        ('game', '0003_game_gamedata_per_game'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='thumbnail_url',
            new_name='thumbnail',
        ),
        migrations.RunPython(clear_url_thumbnails, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='game',
            name='thumbnail',
            field=models.FileField(blank=True, help_text='Thumbnail image (PNG, JPG, GIF or WebP)', upload_to='game/thumbnails/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif', 'webp'])]),
        ),
    ]

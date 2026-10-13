import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Adds Game (JavaScript stored in the DB) and turns GameData into one save per user per game.
    GameData was empty when this was written, so the one-off default for `game` is never used.
    """

    dependencies = [
        ('game', '0002_gamedata_base_timestamps'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date and time when this entry was created in the system')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date and time when the table data was last updated in the system')),
                ('slug', models.SlugField(help_text='Used in the URL: /games/<slug>/', unique=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('thumbnail_url', models.CharField(blank=True, help_text='Image URL, e.g. https://… or /static/…', max_length=500)),
                ('code', models.TextField(help_text='JavaScript for the game. Draw on DjGame.canvas; use await DjGame.load() and DjGame.save(state) for progress.')),
                ('is_active', models.BooleanField(default=True, help_text='Only active games are listed and playable')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AlterField(
            model_name='gamedata',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_data', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gamedata',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='saves', to='game.game'),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='gamedata',
            constraint=models.UniqueConstraint(fields=('user', 'game'), name='one_save_per_user_per_game'),
        ),
    ]

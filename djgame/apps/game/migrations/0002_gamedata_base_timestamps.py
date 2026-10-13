from django.db import migrations, models


class Migration(migrations.Migration):
    """
    GameData now inherits ModelAbstractBase: created_at / updated_at become created / updated.
    """

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamedata',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='gamedata',
            old_name='updated_at',
            new_name='updated',
        ),
        migrations.AlterField(
            model_name='gamedata',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Date and time when this entry was created in the system'),
        ),
        migrations.AlterField(
            model_name='gamedata',
            name='updated',
            field=models.DateTimeField(auto_now=True, help_text='Date and time when the table data was last updated in the system'),
        ),
    ]

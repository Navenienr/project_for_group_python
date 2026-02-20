# Generated migration to remove News model from core app
# Note: News model was moved to news app, so this migration is not needed
# if News was never created in core. Keeping it for safety if migration 0001_initial
# was already applied with News model.

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('news', '0001_initial'),  # Зависимость от news миграции
    ]

    operations = [
        # News model should not exist in core if 0001_initial was updated correctly
        # This migration is kept for backward compatibility
    ]

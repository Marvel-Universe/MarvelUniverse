from django.apps import AppConfig


class MarveluniverseConfig(AppConfig):
    """
    AppConfig for the MarvelUniverse app.

    Attributes:
    - default_auto_field (str): The default value for the 'AutoField' option in model definitions.
    - name (str): The name of the app.

    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MarvelUniverse'

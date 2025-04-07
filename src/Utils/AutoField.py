from django.db import models
import random
import string


def generate_unique_id(prefix):
    """
    Generate a unique identifier with the specified prefix.
    """
    random_chars = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    return f"{prefix}_{random_chars}"


class CustomAutoField(models.CharField):
    """
    Custom CharField that generates unique identifiers with a prefix.
    """

    def __init__(self, prefix, *args, **kwargs):
        self.prefix = prefix
        kwargs["max_length"] = kwargs.get("max_length", 255)  # Set a default max_length
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        if not value:
            value = generate_unique_id(self.prefix)
            setattr(model_instance, self.attname, value)
        return value

    def deconstruct(self):
        """
        Return enough information to recreate the field as a 4-tuple:
        - field's class name
        - positional arguments
        - keyword arguments
        """
        name, path, args, kwargs = super().deconstruct()
        kwargs["prefix"] = (
            self.prefix
        )  # Ensure the 'prefix' is included in the deconstruction
        return name, path, args, kwargs

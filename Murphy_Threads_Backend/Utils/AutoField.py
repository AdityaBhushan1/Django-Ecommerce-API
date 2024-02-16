# common/fields.py

import random
import string
from django.db import models

def generate_unique_id(prefix):
    """
    Generate a unique identifier with the specified prefix.
    """
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return f"{prefix}_{random_chars}"

class CustomAutoField(models.CharField):
    """
    Custom AutoField that generates unique identifiers with a prefix.
    """
    def __init__(self, prefix, *args, **kwargs):
        self.prefix = prefix
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        if not value:
            value = generate_unique_id(self.prefix)
            setattr(model_instance, self.attname, value)
        return value

import os
from dotenv import dotenv_values
env_vars = dotenv_values()

IS_UNDER_DEVELOPMENT = env_vars.get("under_development")

print(IS_UNDER_DEVELOPMENT)
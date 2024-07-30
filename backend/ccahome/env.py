
import os
import pathlib
from functools import lru_cache

from decouple import Config, RepositoryEnv
# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

ENV_PATH = BASE_DIR.parent / '.env'


ENV_PATH = BASE_DIR / ".env"

@lru_cache
def get_config():
    if ENV_PATH.exists():
        return Config(RepositoryEnv(str(ENV_FILE)))
    from decouple import config
    return config

config = get_config()
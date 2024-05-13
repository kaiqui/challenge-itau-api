import os
from dotenv import load_dotenv


class Environment:
    def __init__(self, *keys):
        self._vars = {}
        self._load_env_file()
        self._load_variables(keys)

    def _load_env_file(self):
        try:
            dotenv_path = os.path.join(os.path.dirname(__file__), "app", ".env")
            if os.path.exists(dotenv_path):
                load_dotenv(dotenv_path)
            else:
                load_dotenv()
        except FileNotFoundError as e:
            raise FileNotFoundError("The specified .env file was not found.") from e

    def _load_variables(self, keys):
        for key in keys:
            value = os.getenv(key)
            if value is None:
                raise KeyError(f'Environment variable "{key}" is not defined.')
            self._vars[key] = value

    def get(self, name, default=None):
        return self._vars.get(name, default)

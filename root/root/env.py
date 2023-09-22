"""Модуль для работы с переменными окужения"""

from dataclasses import dataclass

from environs import Env


@dataclass
class DjangoSecretKey:
    secret_key: str


@dataclass
class EnvConfigs:
    secret_key: DjangoSecretKey


def load_config(env_file_path=None):
    env = Env()
    env.read_env(env_file_path)

    config = EnvConfigs(
        secret_key=env('SECRET_KEY')
    )

    return config

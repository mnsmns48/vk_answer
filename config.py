from environs import Env
from dataclasses import dataclass


@dataclass
class Hidden:
    vk_api_token: str


def load_config(path: str = None):
    env = Env()
    env.read_env()
    return Hidden(
        vk_api_token=env.str("VK_API_TOKEN")
    )


hidden_vars = load_config('.env')

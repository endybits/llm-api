from api.core.config import get_config_values

config = get_config_values()
OPENAI_API_KEY = config["openai_api_key"]
print(OPENAI_API_KEY)

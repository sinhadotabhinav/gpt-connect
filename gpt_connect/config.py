import os
from dotenv import load_dotenv
import yaml

load_dotenv()

def get_api_key():
    return os.getenv("OPENAI_API_KEY")

def load_config():
    with open('config.yaml', 'r') as file:
        return yaml.safe_load(file)

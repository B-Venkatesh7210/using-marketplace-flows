from mira_sdk import MiraClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")

# Initialize the client
client = MiraClient(config={"API_KEY": api_key})

version = "1.0.0"
input_data = {
    "age": "24",
    "height": "172cm",
    "skin_tone": "Fair",
    "color_preferences": "Green & Beige"
}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@anand/clothing-suggestion-generator/{version}"
else:
    flow_name = "@anand/clothing-suggestion-generator"

result = client.flow.execute(flow_name, input_data)
print(result)

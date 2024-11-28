from mira_sdk import MiraClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")

# Initialize the client
client = MiraClient(config={"API_KEY": api_key})

version = "0.0.2"
input_data = {
    "question": "What is the best way to learn about RAG Flows?"
}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@flamekaiser/karan-mira-clone/{version}"
else:
    flow_name = "@flamekaiser/karan-mira-clone"

result = client.flow.execute(flow_name, input_data)
print(result)
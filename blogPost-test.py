from mira_sdk import MiraClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")

# Initialize the client
client = MiraClient(config={"API_KEY": api_key})

version = "1.0.3"
input_data = {
    "blog_topic": "AI & Crypto",
    "content_type": "Hallucination and Biasness in AI LLM models",
    "audience_requirements": "A blog for Developer audience who are interested in AI and Crypto",
}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@super-labs/blog-post-generator/{version}"
else:
    flow_name = "@super-labs/blog-post-generator"

result = client.flow.execute(flow_name, input_data)
print(result)
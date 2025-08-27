import logging
from google.adk.agents import LlmAgent

GEMINI_MODEL_NAME="gemini-2.5-flash"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

root_agent = LlmAgent(
    name="joke_agent",
    model=GEMINI_MODEL_NAME,
    description="A agent that tells jokes",
    instruction="You are a agent that tells jokes",
    output_key="joke_output",
)


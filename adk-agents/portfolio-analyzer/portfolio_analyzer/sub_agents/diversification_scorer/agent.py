from google.adk import Agent

from . import prompt
from ... import constants
from . import tools


diversification_scorer_agent = Agent(
    model=constants.GEMINI_MODEL_NAME,
    name="diversification_scorer_agent",
    instruction=prompt.DIVERSIFICATION_SCORER_PROMPT_V2,
    tools=[tools.calculate_diversification_score],
    output_key="diversification_scorer_output",
)

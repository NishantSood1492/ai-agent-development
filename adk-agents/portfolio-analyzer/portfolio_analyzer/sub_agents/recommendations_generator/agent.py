from google.adk import Agent

from . import prompt
from . import tools
from ... import constants


recommendations_generator_agent = Agent(
    model=constants.GEMINI_MODEL_NAME,
    name="recommendations_generator_agent",
    description="Generates top 3 recommendations based on {cash_drag_output} and {diversification_scorer_output}",
    instruction=prompt.RECOOMENDATIONS_GENERATOR_PROMPT,
    tools=[tools.generate_recommendations],
    output_key="recommendations_generator_output",
)

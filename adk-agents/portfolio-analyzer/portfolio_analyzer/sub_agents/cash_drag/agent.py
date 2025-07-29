from google.adk import Agent

from . import prompt
from . import tools
from ... import constants


cash_drag_agent = Agent(
    model=constants.GEMINI_MODEL_NAME,
    name="cash_drag_agent",
    instruction=prompt.CASH_DRAG_ANALYZER_PROMPT,
    tools=[tools.calculate_cash_drag],
    output_key="cash_drag_output",
)

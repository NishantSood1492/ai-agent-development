"""Financial coordinator: provide reasonable investment strategies"""
from google.adk.agents import LlmAgent, SequentialAgent, ParallelAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.cash_drag import cash_drag_agent
from .sub_agents.diversification_scorer import diversification_scorer_agent
from .sub_agents.recommendations_generator import recommendations_generator_agent

from . import constants
from . import tools


portfolio_agent = LlmAgent(
    name="portfolio_agent",
    model=constants.GEMINI_MODEL_NAME,
    description="""Portfolio Agent: Responsible for fetching portfolio data.""",
    instruction=prompt.FINANCIAL_COORDINATOR_PROMPT_V2,
    output_key="financial_coordinator_output",
    tools=[
       tools.fetch_portfolio_data,
    ],
)

parallel_agents = ParallelAgent(
    name="parallel_agents",
    sub_agents=[cash_drag_agent, diversification_scorer_agent],
)

financial_coordinator_agent = SequentialAgent(
    name="financial_coordinator_agent",
    sub_agents=[portfolio_agent, parallel_agents, recommendations_generator_agent],
)

root_agent = financial_coordinator_agent

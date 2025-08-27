from google.adk.agents import Agent
from phoenix.otel import register
from .tools.rss_feed_tools import get_techcrunch_rss
from .tools.aggregator_tool import aggregator_tool
from .schemas import IdeaContent
from . import prompt


PHOENIX_PROJECT_NAME="idea-generator"
GEMINI_MODEL_NAME="gemini-2.0-flash"

techcrunch_rss = get_techcrunch_rss()
techcrunch_rss_aggregation = aggregator_tool(techcrunch_rss)


# configure the Phoenix tracer
tracer_provider = register(
  project_name=PHOENIX_PROJECT_NAME, # Default is 'default'
  auto_instrument=True # Auto-instrument your app based on installed OI dependencies
)

root_agent = Agent(
    name="idea_generator_agent", 
    model=GEMINI_MODEL_NAME,
    description=(
        "Agent to generate ideas based on the rss feeds provided"),
    instruction= prompt.IDEA_GENERATOR_PROMPT + f"""
        
        Here's the titles of the news articles:
        {techcrunch_rss_aggregation['title']}

        Here's the contents of the news articles:
        {techcrunch_rss_aggregation['content']}
        """,
    
    output_schema=IdeaContent,
    output_key="idea",
    include_contents='none',
)

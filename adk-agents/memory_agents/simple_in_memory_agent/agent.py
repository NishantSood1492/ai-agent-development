import asyncio
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
from dotenv import load_dotenv

APP_NAME = "simple_in_memory_agent"

# Load the environment vaiables for the model
load_dotenv()

# Initialize the in-memory session service
session_service = InMemorySessionService()

# Initialize the agent
agent = LlmAgent(
    name=APP_NAME,
    model="gemini-2.0-flash",
    description="A simple chatbot that stores and retrieves conversation history",
    instruction="""
    You are a simple chatbot that stores and retrieves conversation history.
    If the user tells you their name, you respond with a warm greeting. If the user doesn't tell you their name, you ask them to do so.
    """,
)


# Create a chat function that manages the session state
async def chat(user_id: str, message: str) -> str:
    # Chat function with persistent database memory
    session_id = f"session_{user_id}"

    # Create a get a session
    session = await session_service.get_session(
        app_name=APP_NAME, 
        user_id=user_id,
        session_id=session_id
    )

    # Check if the session exists, if not, create a new one
    if not session:
        session = await session_service.create_session(
            app_name=APP_NAME, 
            user_id=user_id, 
            session_id=session_id,
            state={"conversation_history": [] }
        )

    # Create user content
    user_content = types.Content(
        role="user",
        parts=[types.Part(text=message)]
    )

    # Run the agent with session
    response_text = ""
    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=user_content
    ): 
        if event.is_final_response():
            if event.content and event.content.parts:
                response_text = event.content.parts[0].text
            break
    
    return response_text


# Create a runner for the agent
runner = Runner(
    agent=agent,
    app_name=APP_NAME,
    session_service=session_service
)


    
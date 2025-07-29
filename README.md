# What is this Project About

TBD

# How to run this project

1. Setup Python virtual environment
   `python -m venv .venv`

2. Activate the virtual environment
   `source .venv/bin/activate`

3. Install dependencies (This will install google-adk and all it's dependencies in your virtual environment)
   `pip install google-adk`

4. switch to adk-agents directory (into a specific agent you would like to test)
   for example: `cd adk-agents/portfolio-analyzer`

5. Copy .example.env file to create a new .env file and update with your GEMINI_KEY

6. Run the following command to start adk web to test the agents
   `adk web`

# Example

## Porfolio Analyzer

![alt text](/screenshots/portfolio_analyzer.png)

from strands import Agent
from strands_tools import calculator, current_time

STANDARD_MODEL = "arn:aws:bedrock:eu-central-1:998978876161:inference-profile/eu.anthropic.claude-sonnet-4-20250514-v1:0"

agent = Agent(
    model=STANDARD_MODEL,
    tools=[calculator, current_time])

message="""
what is my age, I was born in 1095?
"""
agent(message)
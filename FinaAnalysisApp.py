import streamlit as st
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

st.title("🤖 Agentic AI: Financial Analyst")

# Setup the Agent
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_news=True)],
    instructions=["Use tables to display data.", "Be concise."],
    show_tool_calls=True
)

user_input = st.text_input("Enter a Stock Ticker (e.g., NVDA, AAPL):")

if user_input:
    with st.spinner("Agent is researching and calling tools..."):
        # The agent 'thinks' and decides which tools to call automatically
        response = agent.run(f"Analyze the performance of {user_input}")
        st.markdown(response.content)
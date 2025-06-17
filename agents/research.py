# legalAssistant/agents/research.py

import streamlit as st
import uuid
import os
from llama_stack_client import Agent
from tavily import TavilyClient
from .config import research_agent_config_template
from core.config import TAVILY_API_KEY

def run_research_agent(client, topic: str, model_id: str):
    """
    Executes the research agent to gather information on a legal topic.
    """
    research_agent_config = research_agent_config_template.copy()
    research_agent_config['model'] = model_id

    with st.spinner(f"Researching topic: {topic}..."):
        try:
            research_agent = Agent(client, **research_agent_config)
            session_id = research_agent.create_session(session_name=f"research_agent_{uuid.uuid4()}")

            # Turn 1: Generate search queries
            query_generation_prompt = f"Generate 2 specific search queries for the following legal topic: {topic}"
            query_generation = research_agent.create_turn(
                messages=[{"role": "user", "content": query_generation_prompt}],
                stream=False, session_id=session_id
            )
            queries = [line.strip("- ").strip() for line in query_generation.output_message.content.splitlines() if line.strip()]

            if not queries:
                st.warning("Research agent did not generate queries. Using the topic directly.")
                queries = [topic]

            if not TAVILY_API_KEY:
                st.error("TAVILY_API_KEY environment variable is not set. Research functionality will be limited.")
                st.info("You can set it by running: export TAVILY_API_KEY='your_api_key_here'")
                return {
                    "queries_executed": queries,
                    "summary": "Research unavailable - Tavily API key not configured",
                    "key_insights": ["API key required for web search functionality"],
                    "source_results": []
                }

            tavily_client = TavilyClient(api_key=TAVILY_API_KEY)
            query_to_search = queries[0]
            st.info(f"Executing search with query: '{query_to_search}'")
            tavily_results = tavily_client.search(query=query_to_search, search_depth="advanced", max_results=5)
            research_snippets = "\n\n".join([f"Source: {res.get('title', '')}\nContent: {res.get('content', '')}" for res in tavily_results.get("results", [])])

            # Turn 2: Summarize findings
            summarization_prompt = f"Please provide a concise summary of the following legal research findings:\n\n{research_snippets}"
            summary_response = research_agent.create_turn(
                messages=[{"role": "user", "content": summarization_prompt}],
                stream=False, session_id=session_id
            )
            summary = summary_response.output_message.content.strip()

            # Turn 3: Extract insights
            insights_prompt = f"Based on this summary, list 3 key legal insights as a bulleted list:\n\n{summary}"
            insights_response = research_agent.create_turn(
                messages=[{"role": "user", "content": insights_prompt}],
                stream=False, session_id=session_id
            )
            key_insights = [line.strip("-* ").strip() for line in insights_response.output_message.content.splitlines() if line.strip()]

            research_output = {
                "queries_executed": queries,
                "summary": summary,
                "key_insights": key_insights,
                "source_results": tavily_results.get("results", [])
            }
            st.success("Research completed successfully.")
            return research_output

        except Exception as e:
            st.error(f"An error occurred during research: {e}")
            return {}
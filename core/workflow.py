# legalAssistant/core/workflow.py

import streamlit as st
import json
import uuid
from llama_stack_client import Agent
from agents.config import (
    legal_orchestrator_agent_config_template,
    legal_worker_agent_config_template,
)
from agents.research import run_research_agent

def run_research_phase(client, research_topic, context, model_id):
    """Executes the research phase if a topic is provided."""
    if not research_topic:
        return context
    
    with st.expander("Research Agent Output", expanded=True):
        research_data = run_research_agent(client, research_topic, model_id)
        if research_data:
            context["research_summary"] = research_data.get("summary", "N/A")
            context["key_insights"] = research_data.get("key_insights", [])
            st.subheader("Research Summary")
            st.write(research_data.get("summary"))
            st.subheader("Key Insights")
            st.json(research_data.get("key_insights"))
        else:
            st.warning("Research step failed or returned no data.")
    
    return context

def run_orchestration_phase(client, task, context, model_id):
    """Executes the orchestration phase to break down the task."""
    legal_orchestrator_agent_config = legal_orchestrator_agent_config_template.copy()
    legal_orchestrator_agent_config['model'] = model_id
    
    with st.spinner("Orchestrator is analyzing the task..."):
        try:
            orchestrator_agent = Agent(client, **legal_orchestrator_agent_config)
            session_id = orchestrator_agent.create_session(f"orchestrator_{uuid.uuid4()}")
            prompt = f"Legal task: {task}. Context: {json.dumps(context)}"
            response = orchestrator_agent.create_turn(
                messages=[{"role": "user", "content": prompt}], 
                stream=False, 
                session_id=session_id
            )
            orchestrator_result = json.loads(response.output_message.content)
            st.success("Orchestration complete.")
            
            with st.expander("Orchestrator Agent Output", expanded=True):
                st.subheader("Task Analysis")
                st.write(orchestrator_result.get("analysis", "No analysis provided."))
            
            return orchestrator_result
            
        except Exception as e:
            st.error(f"Error during orchestration: {e}")
            st.code(response.output_message.content if 'response' in locals() else "No response object.")
            return None

def run_drafting_phase(client, orchestrator_result, context, model_id):
    """Executes the drafting phase to create legal documents."""
    worker_tasks = orchestrator_result.get("tasks", [])
    if not worker_tasks:
        st.warning("Orchestrator did not produce any tasks for the workers.")
        return
    
    st.subheader("Drafted Clauses")
    legal_worker_agent_config = legal_worker_agent_config_template.copy()
    legal_worker_agent_config['model'] = model_id
    
    for task_variant in worker_tasks:
        with st.spinner(f"Worker drafting '{task_variant.get('type', 'N/A')}' version..."):
            worker_agent = Agent(client, **legal_worker_agent_config)
            session_id = worker_agent.create_session(f"worker_{uuid.uuid4()}")
            worker_prompt = f"Your task is to draft: '{task_variant.get('description', 'Not specified')}'.\n\nContext: {json.dumps(context)}\n\nResearch Summary: {context.get('research_summary', 'N/A')}"
            response = worker_agent.create_turn(
                messages=[{"role": "user", "content": worker_prompt}], 
                stream=False, 
                session_id=session_id
            )
            
            st.markdown(f"---")
            st.markdown(f"#### Draft: `{task_variant.get('type')}`")
            st.info(f"{task_variant.get('description')}")
            st.markdown(response.output_message.content)

def run_legal_workflow(client, task, context, research_topic, model_id):
    """Main function to run the entire legal assistant workflow."""
    if not client:
        st.error("Client is not initialized. Cannot proceed.")
        return

    # Step 1: Research (Optional)
    context = run_research_phase(client, research_topic, context, model_id)
    
    # Step 2: Orchestration
    orchestrator_result = run_orchestration_phase(client, task, context, model_id)
    if not orchestrator_result:
        return
    
    # Step 3: Worker Drafting
    run_drafting_phase(client, orchestrator_result, context, model_id)
    
    st.success("All drafting tasks complete!") 
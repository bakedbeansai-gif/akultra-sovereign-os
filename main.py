import streamlit as st
import os
from crewai import Agent, Task, Crew, LLM

# --- 1. THE FREE CLOUD BRAIN ---
# No credit card needed for Hugging Face Free Inference
# Get a free token at huggingface.co/settings/tokens
os.environ["HUGGINGFACE_REPO_ID"] = "deepseek-ai/DeepSeek-V3"
os.environ["HUGGINGFACE_API_KEY"] = "YOUR_FREE_HF_TOKEN" 

remote_llm = LLM(
    model="huggingface/deepseek-ai/DeepSeek-V3",
    api_key=os.environ["HUGGINGFACE_API_KEY"]
)

# --- 2. THE CLOUD BUILDER ---
builder = Agent(
    role="Cloud Engineer",
    goal="Build tools that save to GitHub so I can access them anywhere.",
    backstory="You are a master of free-tier cloud architectures.",
    llm=remote_llm
)

# --- 3. THE UI ---
st.title("🏛️ AkUltra Sovereign Cloud")
st.write("Current Device:", st.query_params.get("device", "Unknown"))

mission = st.text_input("What should we build today?", "A travel checklist app")

if st.button("🚀 Deploy to Cloud"):
    with st.spinner("Brain is processing on Hugging Face..."):
        task = Task(
            description=f"Create the Python code for: {mission}. Save it as 'app.py'.",
            expected_output="Python code for the requested app.",
            agent=builder
        )
        crew = Crew(agents=[builder], tasks=[task])
        result = crew.kickoff()
        
        st.success("App Logic Generated!")
        st.code(result.raw)

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
import uuid

from workflow import run_agent
from utils import extract_text_from_pdf, extract_text_from_csv

# Page setup
st.set_page_config(
    page_title="Agentic AI Chat (Gemini)",
    layout="wide"
)

st.title("🤖 Agentic AI – Smart Operations Assistant")
st.caption("Agno + Gemini + Streamlit | Structured Agent Responses")

# Session ID for memory
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------------------
# Data Upload Section
# -------------------------------
st.subheader("📂 Upload Context Data (Optional)")

uploaded_pdf = st.file_uploader("Upload PDF (Packing List / BOL)", type=["pdf"])
uploaded_csv = st.file_uploader("Upload CSV (Inventory / Orders)", type=["csv"])

context_text = st.text_area(
    "Or paste raw text context",
    height=180,
    placeholder="This data will be used as context for the agent"
)

if uploaded_pdf:
    context_text = extract_text_from_pdf(uploaded_pdf)

elif uploaded_csv:
    context_text = extract_text_from_csv(uploaded_csv)

# Store context in session (acts like memory seed)
if context_text:
    st.session_state.context = context_text

# -------------------------------
# Chat Section
# -------------------------------
st.subheader("💬 Talk to the Agent")

user_question = st.text_input(
    "Ask your question",
    placeholder="Is this shipment ready for dispatch?"
)

if st.button("Send to Agent"):
    if not user_question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Agent is reasoning..."):
            final_input = user_question

            if "context" in st.session_state:
                final_input = f"""
CONTEXT DATA:
{st.session_state.context}

USER QUESTION:
{user_question}
"""

            response = run_agent(
                final_input,
                st.session_state.session_id
            )

        st.session_state.chat_history.append({
            "user": user_question,
            "agent": response
        })

# -------------------------------
# Display Chat History
# -------------------------------
for chat in reversed(st.session_state.chat_history):
    st.markdown("### 👤 You")
    st.write(chat["user"])

    st.markdown("### 🤖 Agent Response")
    st.markdown(chat["agent"])

    st.divider()



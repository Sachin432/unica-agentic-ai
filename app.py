import streamlit as st
import pandas as pd

from llm.groq_llm import get_llm
from agents.orchestrator import run_orchestration
from unica_api.mock_unica import trigger_campaign

# -----------------------------
# App Configuration
# -----------------------------
st.set_page_config(
    page_title="HCL Unica+ Autonomous AI",
    layout="wide"
)

st.title("AI-Driven Autonomous Campaign Orchestration – HCL Unica+")

# -----------------------------
# Load LLM (centralized)
# -----------------------------
llm = get_llm()

# -----------------------------
# Load Customer Data
# -----------------------------
try:
    df = pd.read_csv("data/customers.csv")
except Exception as e:
    st.error(f"Failed to load customer data: {e}")
    st.stop()

if df.empty:
    st.warning("Customer dataset is empty.")
    st.stop()

# Pick a random customer
customer = df.sample(1).to_dict(orient="records")[0]

# -----------------------------
# UI: Customer Profile
# -----------------------------
st.subheader("Customer Profile")
st.json(customer)

# -----------------------------
# Run Agentic Pipeline
# -----------------------------
if st.button("Run Autonomous Campaign Decision"):
    with st.spinner("Running agentic decision pipeline..."):
        result = run_orchestration(llm, customer)

    st.subheader("Agent Reasoning")
    st.json(result)

    # -----------------------------
    # Campaign Execution
    # -----------------------------
    if result.get("approved"):
        response = trigger_campaign(
            customer["customer_id"],
            result["strategy"],
            result["channel"],
            customer.get("email")
        )

        st.success("Campaign Executed Successfully")
        st.json(response)
    else:
        st.error(f"Blocked by Governance: {result.get('governance_reason')}")

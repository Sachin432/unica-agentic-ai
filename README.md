# Live Deployment

 **[https://unica-agentic-ai-qwrmgxjwftdppp85gvld45.streamlit.app/](https://unica-agentic-ai-qwrmgxjwftdppp85gvld45.streamlit.app/)**

---

# AI-Driven Autonomous Campaign Orchestration – HCL Unica+

An **enterprise-grade agentic AI system** that autonomously analyzes customer behavior, decides optimal marketing strategies, selects the best communication channels, and enforces governance rules — inspired by **HCL Unica+ marketing automation platforms**.

This project demonstrates how **LLM-based agents**, **deterministic governance**, and **real-time orchestration** can work together in a production-ready architecture.

---

##  Problem Statement

Modern marketing platforms must:

* Personalize campaigns at scale
* Optimize engagement continuously
* Respect customer consent and compliance
* Provide explainable AI decisions

Traditional rule-based systems struggle to adapt dynamically.
This project solves that by combining **agentic AI reasoning** with **strict governance enforcement**.

---

##  Solution Overview

The system uses **multiple specialized AI agents**, each responsible for a single decision:

1. **Customer Insight Agent**
   Analyzes engagement, churn risk, and intent

2. **Strategy Agent**
   Decides campaign strategy (Retention, Discount, Upsell, Do Nothing)

3. **Channel Agent**
   Selects best channel (Email / SMS / Push) and timing

4. **Governance Agent**
   Enforces compliance rules (opt-out, fatigue thresholds)

5. **Orchestrator**
   Coordinates agents and produces execution-ready output

All decisions are **explainable**, **auditable**, and **enterprise-safe**.

---

##  Architecture

```
Customer Data
     ↓
Customer Insight Agent
     ↓
Strategy Agent
     ↓
Channel Agent
     ↓
Governance Agent (Hard Rules)
     ↓
Campaign Execution (Mock Unica API)
```

LLMs provide **reasoning**, while governance provides **control**.

---

##  Project Structure

```
unica-agentic-ai/
│
├── app.py                     # Streamlit UI
├── config.py                  # Environment config
├── requirements.txt
│
├── data/
│   └── customers.csv          # 100 synthetic customers
│
├── agents/
│   ├── customer_agent.py
│   ├── strategy_agent.py
│   ├── channel_agent.py
│   ├── governance_agent.py
│   └── orchestrator.py
│
├── memory/
│   ├── embedder.py
│   └── vector_store.py
│
├── rl/
│   └── reward_engine.py       # (future RL optimization)
│
├── unica_api/
│   └── mock_unica.py          # Campaign trigger simulation
│
└── README.md
```

---

##  Tech Stack

* **Python**
* **Streamlit** – UI & deployment
* **LangChain** – Agent orchestration
* **Groq LPU (LLMs)** – Ultra-fast inference
* **Hugging Face** – Embeddings
* **LangSmith** – Tracing & observability
* **FAISS** – Vector storage (optional)
* **GitHub + Streamlit Cloud** – CI/CD

---

##  Governance Logic (Key Feature)

The system **never executes a campaign** if:

* Customer has opted out
* Fatigue score exceeds threshold
* Compliance rules are violated

Even if the LLM suggests a strategy, **governance always wins**.

Example:

```json
{
  "approved": false,
  "governance_reason": "Customer opted out"
}
```

This mirrors real-world **HCL Unica compliance enforcement**.

---

##  How to Run Locally

```bash
git clone https://github.com/Sachin432/unica-agentic-ai
cd unica-agentic-ai
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

##  Deployment

Deployed on **Streamlit Cloud**
Secrets managed via `secrets.toml` (Groq, HuggingFace, LangSmith keys)

Live App:
 **[https://unica-agentic-ai-qwrmgxjwftdppp85gvld45.streamlit.app/](https://unica-agentic-ai-qwrmgxjwftdppp85gvld45.streamlit.app/)**

---

##  Key Highlights (Interview-Ready)

* True **agentic AI architecture**
* Separation of reasoning vs execution
* Deterministic governance layer
* Explainable decisions
* Enterprise-ready orchestration
* Inspired by real **HCL Unica+ workflows**

---

##  Future Enhancements

* Reinforcement Learning for campaign optimization
* Real Unica API integration
* Multi-journey orchestration
* KPI dashboards
* A/B testing automation

---

## 👤 Author

**Sachin Kumar**
M.Tech (Data Science)

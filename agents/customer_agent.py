from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def customer_agent(llm, customer: dict):
    prompt = PromptTemplate(
        input_variables=["customer"],
        template="""
Analyze the following customer profile and return:
- intent
- churn_risk (low / medium / high)
- engagement_level

Customer profile:
{customer}
"""
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    # IMPORTANT FIX: pass named input
    return chain.run(
        {"customer": str(customer)}
    )

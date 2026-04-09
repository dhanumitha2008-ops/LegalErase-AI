import streamlit as st
import google.generativeai as genai

# 🔑 Paste your API key here
genai.configure(api_key="AIzaSyDzqPwIPIu68NKO3uFTziN89bnUfZyT8Jk")

# Use Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

st.title("⚖️ LegalErase AI")

st.header("Enter Contract Details")

# User Inputs
contract_type = st.selectbox(
    "Contract Type",
    ["Freelancer", "Employment", "NDA", "Vendor"]
)

business_type = st.text_input("Business Type")

country = st.text_input("Country")

payment = st.text_input("Payment Amount")

duration = st.text_input("Duration")

# Button Click
if st.button("Generate Contract"):

    # Contract Generation Prompt
    prompt = f"""
    Generate a professional legal contract.

    Details:
    Contract Type: {contract_type}
    Business Type: {business_type}
    Country: {country}
    Payment: {payment}
    Duration: {duration}

    Include standard legal clauses.
    """

    response = model.generate_content(prompt)

    st.subheader("📄 Generated Contract")

    st.write(response.text)

    # Risk Analysis Prompt
    risk_prompt = f"""
    Analyze the following contract and identify:

    - Missing legal clauses
    - Potential legal risks
    - Compliance issues

    Contract:
    {response.text}
    """

    risk_response = model.generate_content(risk_prompt)

    st.subheader("⚠️ Identified Legal Risks")

    st.write(risk_response.text)

    # Mitigation Suggestion Prompt
    mitigation_prompt = f"""
    Suggest legal clauses to fix the identified risks.

    Risks:
    {risk_response.text}
    """

    mitigation_response = model.generate_content(mitigation_prompt)

    st.subheader("✅ Suggested Risk Mitigation Clauses")

    st.write(mitigation_response.text)

    # Risk Level Display
    st.warning("⚠️ Risk Level: Medium (Review Recommended)")

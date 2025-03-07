import openai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

import os
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_gift_ideas(occasion, recipient_age, budget, relationship):
    prompt = f"""
    Suggest 5 unique and thoughtful gift ideas for a {relationship} who is {recipient_age} years old.
    The occasion is {occasion}, and the budget is {budget}.
    Provide a short description for each gift idea.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

# Streamlit UI
st.title("🎁 AI Gift Recommender")

occasion = st.selectbox("Select Occasion", ["Birthday", "Anniversary", "Graduation", "Wedding", "Housewarming", "Valentine's Day"])
recipient_age = st.number_input("Recipient's Age", min_value=1, max_value=100, value=25)
relationship = st.selectbox("Relationship", ["Friend", "Partner", "Parent", "Sibling", "Colleague"])
budget = st.selectbox("Select Budget", ["Under ₹500", "₹500 - ₹2000", "₹2000 - ₹5000", "Above ₹5000"])

if st.button("Get Gift Ideas"):
    st.write("**AI Suggestions:**")
    gift_ideas = generate_gift_ideas(occasion, recipient_age, budget, relationship)
    st.write(gift_ideas)

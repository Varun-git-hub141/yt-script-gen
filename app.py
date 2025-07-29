import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Securely get OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.set_page_config(page_title="🎬 YouTube Script Generator", layout="centered")
st.title("🎬 AI YouTube Script Generator")
st.markdown("Generate a full video script from a topic using GPT!")

# Input
user_topic = st.text_input("📝 Enter your video topic here:")
generate = st.button("▶️ Generate Script")

# Generate Script
if generate and user_topic:
    with st.spinner("Generating your script..."):
        prompt = f"Create a detailed YouTube video script for the topic: {user_topic}"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or gpt-4 if you have access
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=800
            )
            script = response['choices'][0]['message']['content']
            st.subheader("🎥 Generated Script")
            st.write(script)
        except Exception as e:
            st.error(f"❌ Error: {e}")

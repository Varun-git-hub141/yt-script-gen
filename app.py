import streamlit as st
import openai

# Set API Key (replace YOUR_API_KEY with your key or use secrets)
openai.api_key = "YOUR_API_KEY"

st.set_page_config(page_title="📖 AI Story Generator", layout="centered")
st.title("📖 AI Story Generator")
st.markdown("Enter a prompt or theme, and let AI create a story for you.")

# User input
prompt = st.text_input("📝 Your story idea (e.g. 'a dragon who wants to learn coding')")

if st.button("✨ Generate Story"):
    if prompt:
        with st.spinner("Generating your story..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or gpt-4 if available
                messages=[
                    {"role": "system", "content": "You are a creative story writer."},
                    {"role": "user", "content": f"Write a detailed short story about: {prompt}"}
                ],
                temperature=0.8,
                max_tokens=500
            )
            story = response['choices'][0]['message']['content']
            st.subheader("📚 Your Generated Story:")
            st.write(story)
    else:
        st.warning("Please enter a story idea to continue.")

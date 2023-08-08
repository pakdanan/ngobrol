import openai
import streamlit as st

st.title("ChatGPT-like clone")

openai.api_key = st.sidebar.text_input("API-KEY", type="password") #st.secrets["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"]

prompt = "Please generate a blog outline on how a beginner can break into the field of data science."

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant with extensive experience in data science and technical writing."},
    {"role": "user", "content": prompt}
  ]
)

st.text(completion.choices[0].message)

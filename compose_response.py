import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_chunks(chunks):
    prompt = "Summarize the following travel information:\n\n" + "\n\n".join(chunks)
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return res['choices'][0]['message']['content']

def compose_final_response(summary):
    prompt = f"Generate a travel recommendation based on this summary:\n\n{summary}"
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return res['choices'][0]['message']['content']
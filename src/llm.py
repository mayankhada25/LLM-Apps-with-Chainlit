from groq import Groq
from src.prompt import system_instruction
import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

client = Groq()

messages = [{"role": "user", "content": system_instruction}]

def ask_order(messages, model="meta-llama/llama-4-scout-17b-16e-instruct", temperature=0):
    completion = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=temperature,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
    )

    return completion.choices[0].message.content


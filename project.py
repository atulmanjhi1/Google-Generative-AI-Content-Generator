# https://github.com/atulmanjhi1/Google-Generative-AI-Content-Generator
import google.generativeai as gpt

prompt = input("ASK to Atul Manjhi:")

gpt.configure(api_key='Your_API_Key')

geminipro = gpt.GenerativeModel('gemini-pro')

response = geminipro.generate_content(prompt)

print(response.text)

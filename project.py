# https://github.com/atulmanjhi1/Google-Generative-AI-Content-Generator
import google.generativeai as gpt

prompt = input("ASK to Atul Manjhi:")

gpt.configure(api_key='AIzaSyDzeLERYL7HHJwJvSofAUjVT1H3YUojd_8')

geminipro = gpt.GenerativeModel('gemini-pro')

response = geminipro.generate_content(prompt)

print(response.text)

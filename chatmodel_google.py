from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
result = model.invoke("What is the capital of india?")
print(result.content)
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()  
load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.5)
result = model.invoke("Write a 5 line poem on cricket?")
print(result.content)
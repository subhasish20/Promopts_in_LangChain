from langchain_core.messages import  HumanMessage,AIMessage,SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import  load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.5)

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me the capital of India")
]

result = model.invoke(messages)

ai_message = AIMessage(content=result.content)
messages.append(ai_message)

print(messages)
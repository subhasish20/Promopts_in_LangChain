from langchain_core.prompts import  MessagesPlaceholder,ChatPromptTemplate
from  langchain_google_genai import  ChatGoogleGenerativeAI
from dotenv import  load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)


# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')

])

chat_history = []
# load chat history
with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())

print(chat_history)
# create prompt

prompt = chat_template.invoke(
    {
        'chat_history':chat_history,
        'query':'where is my refound'
    }
)

print(prompt)
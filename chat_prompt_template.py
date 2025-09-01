from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)

# Properly create the chat prompt template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful assistant in {domain}'),
    ('human', 'Explain in simple terms, what is {topic}')
])

# Fill the variables
prompt = chat_template.invoke(
    {
        'domain': "cricket",
        'topic': "bowling"
    }
)

print(prompt)

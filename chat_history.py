from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import  load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


# initializing a empty list fo storing the chat history
chat_history = []

while True:
    user_input = input("Your :")
    chat_history.append(user_input) # inserting into the chat_history
    if user_input == "exit":
        break
    else:
        result = model.invoke(chat_history)
        chat_history.append(result.content) # inserting into the chat_history
        print("AI : ",result.content)

print(chat_history)
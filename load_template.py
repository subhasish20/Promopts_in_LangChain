from langchain_google_genai import  ChatGoogleGenerativeAI
from langchain.prompts import  PromptTemplate,load_prompt
from dotenv import load_dotenv
import  streamlit as st
 

# loading the .env file
load_dotenv()

# fetching the llm model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

st.header("Text summarizer using AI")

# streamlit ui
text_input = st.text_input("Enter the text here !!")

style_input = st.selectbox("Enter the text style ",["concise", "detailed", "bullet points", "academic", "casual"])

length_input = st.selectbox("Enter the text length",["short", "medium", "long"])


template = load_prompt("template.json")


# invoking the template
prompt = template.invoke({
    'text':text_input,
    'style':style_input,
    'length':length_input

})
# sending to llm
result = llm.invoke(prompt)

# printing the result in the ui
if st.button("summarize"):
    st.write(result.content)
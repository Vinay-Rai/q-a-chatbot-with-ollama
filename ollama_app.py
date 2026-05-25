import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


import os
from dotenv import load_dotenv

load_dotenv()

## langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "simple q&a chatbot with ollama"

# prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant. please response to the user queries"),
        ("user","Question:{question}")
    ]
)

#temperature 0 means the llm model is not creative now
def generate_response(question,llm,temperature,max_tokens):
    llm = Ollama(model=llm)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({"question":question})
    return answer 


#titlee of the app
st.title("Enhanced q&a chatbot with ollama")

#dropdown to select varios openai models
llm = st.sidebar.selectbox("Select an  ai model",["gemma:2b"])

#adjust response parameter
temperature = st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max_Tokens",min_value=50,max_value=300,value=150)

#main interface for user
st.write("go ahead and ask any question")
user_input = st.text_input("you:")

if user_input:
    response = generate_response(user_input,llm,temperature,max_tokens)
    st.write(response)

else:
    st.write("please provide the query")
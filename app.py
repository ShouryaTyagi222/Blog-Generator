from langchain import HuggingFaceHub
import os
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'
llm = HuggingFaceHub(repo_id = 'meta-llama/Llama-2-7b', model_kwargs = {'temperature':0, 'max_length':256})

def getLLamaResponse(input_text, no_words, blog_style):
    template = 'write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words'

    prompt = PromptTemplate(input_variables = ['blog_style','input_text','no_words'],
                            template = template)
    
    response = llm(prompt.format(blog_style, input_text, no_words))

    print(response)
    return response



st.set_page_configs(page_title = 'Generate Blogs',
                    layout = 'centered',
                    initial_sidebar_state = 'collapsed')
st.header("generate Blogs")
input_text = st.text_input('enter the Blog topic')

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for', ('Reasearchers','Data Scientest','Common People'), index = 0)

submit = st.button('Generate')

if submit:
    st.write(getLLamaResponse(input_text, no_words, blog_style))
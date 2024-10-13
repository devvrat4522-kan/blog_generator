import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers



def llama_functions(input_text,blog_style,no_words):
    llm = CTransformers(model='model/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens':256,'temperature':0.01})
    
    
    template =""""
    Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words.
    """

    prompt = PromptTemplate(input_variables=["blog_style","input_text","no_words"],template=template)

    res = llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(res)
    return res


st.set_page_config(page_title="Generate Blog", page_icon='Blog',layout='centered',initial_sidebar_state='collapsed')

st.header("BLOG GENERATOR")

input_text = st.text_input("Enter the Blog Topic")

c1,c2 = st.columns([5,5])

with c1:
    no_words=st.text_input("Number of Words")

with c2:
    blog_style= st.selectbox("Writing the Blog for",('Researchers','Data Science','Student','Common People'),index=0)

submit = st.button("Generate")

if submit:
    st.write(llama_functions(input_text,blog_style,no_words))
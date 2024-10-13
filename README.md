# blog_generator

This is a web application built using Streamlit, Langchain, and Llama 2 that generates blogs based on user inputs such as blog topic, style, and word count. The Llama 2 model processes the given inputs and produces a well-structured blog according to the chosen specifications.

# Features
#### Input Topic: Users can provide the desired topic for the blog.
#### Blog Style: Choose from different writing styles such as Researchers, Data Science, Students, and Common People.
#### Word Limit: Specify the number of words for the blog.
#### Blog Generation: Click a button to generate the blog based on the given inputs.


# Requirements

To run the project, you need the following:

Python 3.8 or higher
Streamlit
Langchain
CTransformers (for Llama 2 model loading)

Installation

1. Clone this repository:
git clone https://github.com/your-username/blog-generator.git

2. Navigate to the project directory:
cd blog-generator

3. Install the required dependencies:
pip install -r requirements.txt

4. Download the Llama 2 model file and place it in the model directory:
Link: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
model/llama-2-7b-chat.ggmlv3.q8_0.bin


# Usage
Run the Streamlit application:

1. streamlit run app.py
2. Open the web application in your browser ( http://localhost:8501 ).
3. Fill in the blog topic, select the blog style, specify the number of words, and click on the "Generate" button.
4. The generated blog will appear on the screen.


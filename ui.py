import streamlit as st
import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

def grammar_and_style_check(text):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Choose the appropriate engine here
            prompt="Please correct the grammar and improve the style of the following text:\n\n" + text,
            temperature=0.0,
            max_tokens=300,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            n=1,
            stop=None
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Streamlit UI
st.title('Grammar and Style Check')

# User input text
text = st.text_area('Enter the text to check for grammar and style:')

if st.button('Check Grammar and Style'):
    # Perform grammar and style check
    corrected_text = grammar_and_style_check(text)
    
    # Display results
    if corrected_text:
        st.subheader('Original Text:')
        st.write(text)
        st.subheader('Corrected Text:')
        st.write(corrected_text)

# Add custom CSS for footer
footer_style = """
position: fixed;
left: 0;
bottom: 0;
width: 100%;
text-align: center;
padding: 10px;
background-color: rgba(255, 255, 255, 0.5);  /* Semi-transparent light background */
color: #000;                                  /* Dark text for visibility */
border-top: 1px solid #000;                   /* Border to distinguish the footer */
z-index: 1000;                                /* Ensures it stays on top of other elements */
"""

# Footer
st.markdown(
    '<div style="{}">Developed by mirac | Contact at: mirac.eth@ethereum.email</div>'.format(footer_style),
    unsafe_allow_html=True
)

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
            engine="gpt-3.5-turbo-instruct",  # Choose the appropriate engine here
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

# Get user input
text = input("Enter the text to check for grammar and style: ")

# Perform grammar and style check
corrected_text = grammar_and_style_check(text)

if corrected_text:
    print("Original Text:")
    print(text)
    print("Corrected Text:")
    print(corrected_text)

from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables
load_dotenv()

# GET API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def generate_tests(user_story):

    prompt = f"""
You are an expert QA automation engineer.

Convert the following user story into:
1. Positive test cases
2. Negative test cases
3. Edge cases
4. PyTest automation skeletons using Playwright

User Story:
{user_story}
"""
    # Send a request to OpenAI API to generate a response
    response = client.chat.completions.create(
        
        # Specify which model to use (fast + cost-effective for this project)
        model="gpt-4o-mini",

        # Provide the conversation input to the model
        # "role": "user" means this is the user's prompt
        # "content": prompt contains your user story + instructions
        messages=[{"role": "user", "content": prompt}]
    )

    # Extract and return the generated text from the API response
    # response.choices -> list of possible outputs from the model
    # [0] -> take the first (best) response
    # .message.content -> actual generated text (your test cases + code)
    return response.choices[0].message.content

from dotenv import load_dotenv
import os
import re
from openai import OpenAI

# Load environment variables
load_dotenv()

# GET API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def extract_python_code(text):
    # Remove markdown
    text = text.replace("```python", "").replace("```", "").strip()

    lines = text.splitlines()
    cleaned = []

    for line in lines:
        stripped = line.strip()

        # Keep comments
        if stripped.startswith("#"):
            cleaned.append(line)

        # Keep imports
        elif stripped.startswith("import") or stripped.startswith("from"):
            cleaned.append(line)

        # Keep decorators
        elif stripped.startswith("@"):
            cleaned.append(line)

        # keep function definitions
        elif stripped.startswith("def "):
            cleaned.append(line)
        
        # Keep indented lines (function body)
        elif line.startswith(" ") or line.startswith("\t"):
            cleaned.append(line)

    return "\n".join(cleaned).strip()

def generate_tests(user_story):

    prompt = f"""
You are an expert QA automation engineer.

Convert the following user story into:
1. Positive test cases
2. Negative test cases
3. Edge cases
4. PyTest automation skeletons using Playwright

STRICT RULES:
- Output ONLY valid Python code
- Do NOT include explanations
- Do NOT include markdown (no ``` blocks)
- Do NOT include comments outside the code
- The output must be directly runnable with pytest

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
    raw_output = response.choices[0].message.content

    # Clean AI output (extract only python code)
    cleaned = extract_python_code(raw_output)

    return cleaned

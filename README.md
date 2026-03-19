# AI Test Case Generator + Automation Runner

An end-to-end QA automation pipeline that converts user stories into executable test cases using AI, then runs them automatically with PyTest and Playwright, integrated with CI/CD.

## 🚀 Overview
This project demonstrates how AI can be integrated into the Software Development Life Cycle (SDLC) to automate test case generation and execution.
Pipeline Flow:
```
User Story → AI generates test cases → Test file created → PyTest executes → CI pipeline runs
```

## 🧠 Key Features
- AI-powered test case generation from user stories
- Automatic conversion to PyTest + Playwright test scripts
- Test execution using PyTest
- Output validation and cleaning of AI-generated code
- Continuous Integration with GitHub Actions
- Modular and scalable architecture

## 🏗️ Tech Stack
- Python
- OpenAI API
- PyTest
- Playwright
- GitHub Actions (CI/CD)
- python-dotenv

## 📂 Project Structure
```
ai-test-automation-runner
│
├── generator/
│   └── test_generator.py      # AI test generation + cleaning logic
│
├── runner/
│   └── run_tests.py           # Executes pytest via subprocess
│
├── tests/
│   └── test_generated.py      # AI-generated test cases
│   └── test_manual.py         # Manual test cases
│
├── main.py                    # Orchestrates pipeline
├── requirements.txt
├── .env                       # Stores API key (not committed)
└── .github/workflows/
    └── test_pipeline.yml      # GitHub Actions pipeline
```

## ⚙️ Setup Instructions
1. Clone the repository

```bash
git clone https://github.com/Miracle193/ai-test-automation-runner
cd ai-test-automation-runner
```

2. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
playwright install
playwright install-deps
```

4. Configure environment variables
Create a .env file:

```
OPENAI_API_KEY=your_api_key_here
```


## ▶️ Usage
Run the pipeline:

```bash
python main.py
```

Enter a user story when prompted:
```
As a user, I want to log in so that I can access my account
```


## 🧪 What Happens Next
1. AI generates PyTest + Playwright test cases
2. Output is cleaned and validated
3. Tests are saved to:
```
tests/test_generated.py
```
4. PyTest executes the tests
5. Results are printed in the terminal

## 🔁 CI/CD Pipeline
This project includes a GitHub Actions workflow that:
- Runs on every push and pull request
- Sets up a Linux environment
- Installs dependencies
- Executes PyTest automatically
- Workflow file:
.github/workflows/test_pipeline.yml

## ⚠️ Notes & Limitations
- AI-generated tests depend on prompt quality
- Dynamic websites may require selector adjustments
- Test reliability improves when using stable demo sites like SauceDemo
- Playwright browser dependencies must be installed for execution

## 💡 Future Improvements
- Add Streamlit UI for live interaction
- Implement AI-based test failure analysis
- Support multiple application domains dynamically
- Export tests to Gherkin (BDD format)
- Improve parsing with AST validation

## 🏁 Conclusion
This project demonstrates the integration of AI into QA automation workflows, showcasing skills in:
- Test automation
- CI/CD pipelines
- AI-assisted development
- Software testing best practices

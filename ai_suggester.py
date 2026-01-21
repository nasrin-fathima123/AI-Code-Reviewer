<<<<<<< HEAD
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    temperature=0.3
)

model = ChatHuggingFace(llm=llm, temperature=0)

def get_ai_suggestion(code_string, previous_suggestions=None):
    if previous_suggestions:
        prev_context = "\n".join(
            s["message"] for s in previous_suggestions
        )
    else:
        prev_context = ""

    response = model.invoke([
        HumanMessage(
            content=f"""
Review the following Python code and give concise, practical suggestions.

Give DIFFERENT suggestions from previous ones:
{prev_context}

Explain WHY suggestions were made.
Focus on scalability, time/space complexity, readability, performance.
Follow PEP8 coding standards.

Code:
{code_string}
"""
        )
    ])

    return [{
        "type": "AISuggestion",
        "message": response.content,
        "severity": "info"
    }]
=======
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    temperature=0.3
)

model = ChatHuggingFace(llm=llm, temperature=0)

def get_ai_suggestion(code_string, previous_suggestions=None):
    if previous_suggestions:
        prev_context = "\n".join(
            s["message"] for s in previous_suggestions
        )
    else:
        prev_context = ""

    response = model.invoke([
        HumanMessage(
            content=f"""
Review the following Python code and give concise, practical suggestions.

Give DIFFERENT suggestions from previous ones:
{prev_context}

Explain WHY suggestions were made.
Focus on scalability, time/space complexity, readability, performance.
Follow PEP8 coding standards.

Code:
{code_string}
"""
        )
    ])

    return [{
        "type": "AISuggestion",
        "message": response.content,
        "severity": "info"
    }]
>>>>>>> bc15ce42fab1e1aa4ec9fe1605ff34c3e2c6ae42

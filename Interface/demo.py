from flask import Flask, request, jsonify
import textwrap
import google.generativeai as genai
from IPython.display import display, Markdown
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_core.runnables import Runnable
from flask_cors import CORS
import numpy as np

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

# Configure Gemini API
api_key = 'AIzaSyC-jh6w2PyKRX6MOTnWG6WJFWpNecDiDbY'
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Define a function to generate text using Gemini
def generate_text(prompt):
    response = model.generate_content(prompt.text)
    if response and response.text:
        return response.text
    return "No response content available."

# Create a custom LLM class implementing Runnable interface
class CustomLLM(Runnable):
    def __init__(self, model):
        self.model = model

    def invoke(self, input_str: str, config=None, **kwargs) -> str:
        return generate_text(input_str)

    def __call__(self, input_str: str, config=None, **kwargs) -> str:
        return self.invoke(input_str, config=config, **kwargs)

# Initialize prompt template
prompt_template = PromptTemplate(
    template="""
    You are an expert in technology and a personality analyst. Your task is to ask 10 multiple-choice questions (4 options only each) designed to identify the most suitable tech field for me based on my answers.

    - You must Present one question at a time. Wait for my response before providing the next question only and always end the question with a question mark.
    - Questions should be in English, and answers must follow this specific format for options: _Option1,, Option2,, Option3_.
    - Questions should gradually transition from general interest in technology to deeper assessments of my skills and preferences.
    - After the 10th question, provide a clear and concise analysis of my answers and suggest the most suitable tech field in English.
    - Avoid asking about preferred fields like object-oriented programming (OOP) or machine learning (ML) or what do you prefer more software or hardware.
    Ensure that:
    - Each question starts on a new line.
    - Avoid using any formatting such as bold (), italics (*), or other special symbols in the question itself.
    - Maintain a conversational and professional tone throughout.


    Here is the conversation so far:
    {history}

    User: {input}

    Assistant:
    """
)



# Initialize global variables
memory = ConversationBufferMemory()
custom_llm = CustomLLM(model)
conversation = ConversationChain(
    llm=custom_llm,
    prompt=prompt_template,
    memory=memory,
)

def add_to_memory(user_input, response):
    memory.save_context(user_input, response)

def reset_memory():
    global memory, conversation
    memory = ConversationBufferMemory()
    add_to_memory({"input": ""}, {"response": "Hello, how can I help you today?"})
    conversation = ConversationChain(
        llm=custom_llm,
        prompt=prompt_template,
        memory=memory,
    )

def converse(user_input):
    inputs = {
        "input": user_input,
        "history": memory.chat_memory
    }
    return conversation(inputs)["response"]

# Flask routes
@app.route('/api/converse', methods=['POST'])
def converse_endpoint():
    try:
        data = request.get_json(force=True, silent=True)  # force=True will handle content-type issues
        
        if data is None:
            user_input = request.form.get('input', '')
        else:
            user_input = (
                data.get('input') or 
                data.get('message') or 
                data.get('text') or 
                data.get('query') or 
                ''
            )

        if not user_input or not isinstance(user_input, str):
            return jsonify({
                "error": "Input is required and must be a string",
                "received": user_input
            }), 400

        response = converse(user_input)
        
        return jsonify({
            "response": response,
            "status": "success"
        }), 200, {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        
    except Exception as e:
        print(f"Error in converse_endpoint: {str(e)}")
        return jsonify({
            "error": "Failed to process request",
            "details": str(e)
        }), 500

@app.route('/api/reset_memory', methods=['POST'])
def reset_memory_endpoint():
    try:
        reset_memory()
        return jsonify({"message": "Conversation memory has been reset."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Add a simple health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Add a root endpoint
@app.route('/', methods=['GET'])
def root():
    return jsonify({
        "message": "API is running",
        "endpoints": {
            "/api/converse": "POST - Send messages to the chatbot",
            "/api/reset_memory": "POST - Reset the conversation",
            "/health": "GET - Check API health"
        }
    }), 200

if __name__ == '__main__':
    # Initialize memory at startup
    reset_memory()
    # Run the Flask app with production settings
    app.run(host='0.0.0.0', port=5000)
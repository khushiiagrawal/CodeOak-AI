from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv
app = FastAPI()
load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")

class CodeRequest(BaseModel):
    code: str

@app.post("/analyze")
def analyze_code(request: CodeRequest):
    """Analyzes code and provides feedback"""
    prompt = f"Review the following Python code and suggest improvements:\n\n{request.code}\n\nSuggestions:"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return {"feedback": response["choices"][0]["message"]["content"]}

@app.post("/analyze_file")
async def analyze_file(file: UploadFile = File(...)):
    """Handles file uploads and analyzes their content"""
    content = await file.read()
    code = content.decode("utf-8")

    return analyze_code(CodeRequest(code=code))

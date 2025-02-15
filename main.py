from fastapi import FastAPI, HTTPException
import openai

app = FastAPI()

# Set up OpenAI API key
OPENAI_API_KEY = "your_openai_api_key"

@app.post("/generate_script/")
def generate_script(topic: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI scriptwriter for YouTube videos."},
                {"role": "user", "content": f"Write a 1-minute script about {topic}"}
            ]
        )
        script = response["choices"][0]["message"]["content"]
        return {"script": script}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    return {"message": "AI Video Generator API is running!"}

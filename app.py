from fastapi import FastAPI, HTTPException
import openai
app = FastAPI()

# Define your OpenAI API key
openai_api_key = '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'

# Define a function to generate the personalized learning path using OpenAI's API
def generate_learning_path(domain: str, proficiency: str, preferences: str) -> str:
    try:
        # Query OpenAI API to generate learning path
        prompt =(
            f"Given the domain {domain}, proficiency {proficiency}, and preferences {preferences}, "
            "provide a personalized learning path that summarizes key concepts and resources in numbered points"
            "up to 150 tokens:"
        )
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=150,
            api_key=openai_api_key  # Pass the API key explicitly
        )
        
        # Extract learning path from API response
        learning_path = response.choices[0].text.strip()
        return learning_path
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating learning path: {e}")

# Create a POST endpoint to accept JSON input
@app.post("/generate_learning_path")
async def create_learning_path(data: dict):
    try:
        domain = data["domain"]
        proficiency = data["proficiency"]
        preferences = data["preferences"]
    except KeyError as e:
        raise HTTPException(status_code=422, detail=f"Missing required field: {e}")

    learning_path = generate_learning_path(domain, proficiency, preferences)
    return {"learning_path": learning_path}

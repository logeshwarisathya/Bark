from fastapi import FastAPI
import httpx

app = FastAPI()


@app.get("/process_prompt")
async def process_prompt(prompt: str):
    url = "https://api.github.com/repos/{owner}/{repo}/process"
    owner = "your-github-username"  # Replace with your GitHub username
    repo = "Bark"  # Replace with the name of the Bark repository

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url.format(owner=owner, repo=repo),
            json={"prompt": prompt}
        )
        response.raise_for_status()
        result = response.json()

    return {"result": result}

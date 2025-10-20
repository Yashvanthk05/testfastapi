from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
  return "Demo FastAPI for Launchly Test"

@app.post("/test")
def test_endpoint(data:dict):
  return {"received_data": data}

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=8000)
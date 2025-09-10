from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # root route
def home():
    return {"message": "FastAPI is working ✅"}

@app.post("/webhook")  # webhook endpoint
def webhook():
    return {"message": "Webhook received!"}

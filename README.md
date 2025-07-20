# Sentiment Analysis API — FastAPI Backend

This project wraps the Sentiment Analysis model in a FastAPI backend, exposing RESTful API endpoints for predictions, health checks, and example retrieval.  

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Returns a simple health check (`{"status": "ok"}`) |
| `/predict` | POST | Accepts JSON input `{"text": "sample review"}` and returns the predicted sentiment |
| `/predict_proba` | POST | Same input as `/predict`, returns sentiment and probability/confidence score |
| `/example` | GET | Returns a random example review from the IMDB training dataset |

---

## How to Build and Run Locally Using Docker & Makefile

1. **Clone the repository:**

   ```bash
   git clone <YOUR_REPO_URL>
   cd <YOUR_PROJECT_DIRECTORY>


2. **Build the Docker container**

   ```bash
docker build -t sentiment-api .

3. **Run the Docker container:**
   ```bash
docker run -d -p 8000:8000 --name sentiment-container sentiment-api

4. **Access the FastAPI application in your browser:**

http://localhost:8000/docs

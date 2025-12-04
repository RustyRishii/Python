# Challenge 2 – Build a Simple REST API

Tech stack: FastAPI + Uvicorn

## Setup
```
pip install fastapi uvicorn
```

## Run
```
uvicorn basic_api:app --reload
```

## Test via curl
- GET metadata  
  `curl -s http://localhost:8000/info | jq`

- POST numbers to sum  
  `curl -s -X POST http://localhost:8000/math/sum -H "Content-Type: application/json" -d '{"numbers":[1,2,3.5]}' | jq`

Expected response:
```
{
  "count": 3,
  "total": 6.5,
  "average": 2.1666666667
}
```

## Challenge Extensions
- Add more routes (e.g., `/math/product`, `/health`).  
- Enable CORS middleware for frontend clients.  
- Replace the static `/info` payload with live metadata (uptime, git SHA).  
- Containerize with Docker and expose configurable host/port via env vars.  
- Write pytest integration tests using `TestClient`.


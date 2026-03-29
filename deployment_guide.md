# FinTracker Deployment Guide (Antigravity Cloud)

## Prerequisites
- Antigravity Node configured or standard python 3.10+ environment available.
- Internet connectivity to resolve external Python package indexes.

## Step 1: Project Setup
Ensure your structure maps successfully to the modular architecture:
```
FinTracker/
├── app.py
├── requirements.txt
├── deployment_guide.md
├── utils/
│   └── security.py
└── engine/
    ├── parser.py
    ├── categorizer.py
    ├── anomaly_detector.py
    └── optimizer.py
```

## Step 2: Environment Provisioning
Initialize a virtual environment to isolate dependencies natively:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Step 3: Local Engine Testing
Fire up the built-in Streamlit web server to view the interface locally:
```bash
streamlit run app.py
```

## Step 4: Scale to Production
For a robust runtime layout inside an enterprise cloud environment:
1. **Containerization:** Define a `Dockerfile` wrapping the target app with `python:3.10-slim`.
2. **Load Balancing:** Add an Nginx or Traefik reverse proxy to buffer `port 8501`.
3. **Data Security Pipeline:** Rest assured knowing any dataset ingested evaluates the `utils/security.py` PII redactor logic identically in memory before rendering.

#!/bin/bash
../venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8010 &
PYTHONPATH=$(pwd) ../venv/bin/streamlit run ui/dashboard.py --server.port 8510 --server.headless true
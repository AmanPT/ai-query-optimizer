# AI Query Optimizer

## Features
- Predicts query performance using ML
- GPT-based suggestions for optimization
- Executes queries on real PostgreSQL database

## Setup
1. Add your OpenAI API key and DB credentials to `.env`
2. Run `python train_model.py`
3. Start with `uvicorn main:app`
4. Launch `streamlit run ui_app.py`

## Deployment
Use `render.yaml` to deploy on Render.

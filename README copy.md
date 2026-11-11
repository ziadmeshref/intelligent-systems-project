# P8: Warehouse Re-Slotting from Predicted Demand

## Project Overview
This project optimizes warehouse layout by forecasting product demand using a Neural Network, generating an initial layout with a Constraint Satisfaction Problem (CSP), and improving the layout via Search algorithms (Greedy Best-First, bounded UCS, A*).

## Environment Setup
```bash
pip install -r requirements.txt
```

## Run Commands
- **Download & Preprocess Data:** `python make_data.py`
- **Run Demo:** `python run_demo.py`
- **Run Tests:** `pytest tests/`
- **Run Experiments:** `python experiments/run_experiments.py`


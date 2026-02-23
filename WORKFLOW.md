# Water Governance Dashboard — Workflow & Procedures

This document explains the overall functionality, architecture, operational procedure, and maintenance steps for the District Water Stress Monitoring & Tanker Allocation Dashboard.

---

## 1. Purpose

Provide district-level situational awareness and operational guidance for water resource management by:
- Predicting Water Stress Index (WSI) per village using a Random Forest model
- Calculating water shortfall and required tankers
- Ranking villages by a priority score
- Visualizing geospatial distribution and routes
- Enabling interactive "what-if" model testing
- Exporting actionable allocation plans

---

## 2. High-level Components

- `app.py` — Streamlit application (UI + orchestration)
- `dataset.csv` — Input data (villages, rainfall, groundwater, population, storage, coords)
- `generate_models.py` — Script to train & save `random_forest.pkl` and `scaler.pkl`
- `random_forest.pkl` — Trained Random Forest model (WSI predictor)
- `scaler.pkl` — `StandardScaler` used to scale model inputs
- `config.py` — Centralized settings (tanker capacity, per-capita need, thresholds)
- `verify_setup.py` — System verification script
- `requirements.txt` — Python dependencies

---

## 3. End-to-end Data & Prediction Flow

1. Data ingestion: `app.py` reads `dataset.csv` into a pandas DataFrame.
2. Feature engineering: compute `rainfall_deviation`, `groundwater_trend`, `water_shortfall`, `tankers_required`.
3. Load model artifacts: `random_forest.pkl` and `scaler.pkl` are loaded via `pickle`.
4. Preprocessing: selected features are scaled with `scaler.transform()`.
5. Prediction: model.predict(X_scaled) → `WSI` (clipped 0–1) appended to DataFrame.
6. Priority scoring: `priority_score = 0.7 * WSI + 0.3 * normalized_population`.
7. Aggregation: compute KPIs (total villages, high-stress count, total tankers, top priority village).
8. Visualization: folium maps, ranking tables, charts, and simulation controls are displayed in Streamlit.
9. Export: allocation plan prepared and made available as downloadable CSV.

Diagram (ASCII):

```
dataset.csv
    ↓
Feature Engineering ---> (water_shortfall, tankers_required)
    ↓
Scale features (scaler.pkl)
    ↓
RandomForest (random_forest.pkl) -> WSI
    ↓
Priority Scoring -> Ranking & Routes
    ↓
Streamlit UI (maps, tables, simulation, exports)
```

---

## 4. UI / Functional Overview

- **Header**: title, subtitle, last-updated timestamp.
- **KPI Row**: Total Villages, High Stress Villages (WSI>0.7), Total Tankers Required, Highest Priority Village.
- **Interactive Map**: Folium map with color-coded markers (green/yellow/orange/red) and popups showing village details.
- **Priority Ranking**: Interactive table sorted by `priority_score` with Rank, Village, WSI, Tankers, Priority Score.
- **Village Simulation Panel**: Dropdown to inspect a village; WSI progress bar, tanks required, storage %, groundwater trend.
- **Interactive Model Testing**: Sliders to change rainfall/groundwater/population/storage and see live WSI prediction (demonstrates model is active).
- **Route Optimization**: Displays route (polyline) from a tanker base to top N priority villages.
- **Export**: CSV downloads for full allocation plan and high-priority villages.

---

## 5. Operator Procedure (Daily Use)

1. Start the app:

```bash
# optional (generate models only if needed):
python generate_models.py

# run dashboard
streamlit run app.py
```

2. Open browser at `http://localhost:8501`.
3. Review KPIs at top of dashboard.
4. Inspect interactive map for clusters of red/orange markers.
5. Open the Priority Ranking table and identify top N urgent villages.
6. Use the Route Optimization tab to preview tanker routing for the top 5.
7. For any village, use the Village Simulation to validate local metrics and requirement.
8. Use the Interactive Model Testing to illustrate how changes (e.g., rainfall event) affect WSI.
9. Click `Download Allocation Plan as CSV` and share with operations teams.

---

## 6. Administrators / Developer Procedure (Model updates)

1. Collect updated dataset (append or replace `dataset.csv`).
2. (Optional) Tune feature engineering or weights in `config.py`.
3. Retrain model:

```bash
python generate_models.py
```

4. Confirm `random_forest.pkl` and `scaler.pkl` created successfully.
5. Restart Streamlit app (or it will auto-reload if running):

```bash
streamlit run app.py
```

6. Validate WSI distributions and KPI sanity checks.

---

## 7. Deployment Notes

- This app runs entirely locally but can be deployed to a server or Streamlit Cloud. For production, consider:
  - Protecting access (auth + HTTPS)
  - Adding logging and audit trails for exported plans
  - Scheduling automated model retraining using a CI job
  - Enabling monitored cron jobs to fetch data inputs (if available)

---

## 8. Troubleshooting — Common Issues & Fixes

- `ModuleNotFoundError: No module named 'folium'` → run `pip install -r requirements.txt` (or install `folium` and `streamlit-folium`).
- Build errors installing `numpy` on Windows (compilation) → ensure pip/wheel updated and prefer binary wheels; run `python -m pip install --upgrade pip setuptools wheel` then `pip install numpy`.
- Map tiles not rendering → check internet connectivity (Folium uses external tiles).
- Model files missing → run `python generate_models.py` to recreate `random_forest.pkl` and `scaler.pkl`.
- Incorrect WSI range or NaNs → verify `dataset.csv` has correct numeric columns and no NaNs; check `verify_setup.py` for integrity checks.

---

## 9. Maintenance & Best Practices

- Keep `config.py` as the single source for tunable parameters (weights, thresholds, tanker capacity).
- Version-control datasets and model artifacts in a secure storage (e.g., S3, internal artifact store).
- Add unit tests for `calculate_feature_engineering()`, `predict_wsi()`, and `calculate_priority_score()`.
- Add logging for exports and user actions if deployed to shared servers.
- Schedule periodic retraining if data changes frequently.

---

## 10. Quick Reference Commands

```bash
# Install dependencies (once)
pip install -r requirements.txt

# Verify environment
python verify_setup.py

# Generate models (if missing)
python generate_models.py

# Run dashboard
streamlit run app.py
```

---

## 11. Contact & Support

For questions about model behavior or production deployment, consult the `README.md` or contact the data science team responsible for the Random Forest model.


---

_Last updated: February 2026_
# 🚀 START HERE - Quick Reference Card

## One-Minute Overview

You have a **professional Water Governance Dashboard** with:
- 🗺️ Interactive maps of 50 villages
- 📊 ML predictions for water stress
- 📥 Export features for reporting
- 🎯 Smart resource allocation

---

## LAUNCH NOW (3 seconds)

### Windows Users 🪟
```
Double-click: setup_and_run.bat
```

### Mac/Linux Users 🍎🐧
```
Terminal: ./setup_and_run.sh
```

### Or Manual
```
streamlit run app.py
```

---

## In Your Browser

→ Go to: **http://localhost:8501**

---

## What You'll See

```
Dashboard with:
✅ 4 KPI Metrics at top
✅ 2 Interactive Maps (tabs)
✅ Priority Ranking Table
✅ Village Details (dropdown)
✅ Statistics Charts
✅ Export Buttons
```

---

## Color Legend

- 🟢 Green = Low stress
- 🟡 Yellow = Moderate
- 🟠 Orange = High
- 🔴 Red = Critical

---

## Key Metrics

| Metric | What It Means |
|--------|--------------|
| **WSI** | Water Stress (0-1, higher = worse) |
| **Priority** | Resource allocation order |
| **Tankers** | Water transport needed |

---

## Download Data

- **Allocation Plan**: Complete village list with all data
- **High Priority**: Only critical villages

Click buttons in "Export Options" section

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Won't start | `python verify_setup.py` |
| Missing packages | `pip install -r requirements.txt` |
| Port in use | `streamlit run app.py --server.port 8502` |
| Map not showing | Check internet connection |

---

## Documentation

- 📖 **QUICKSTART.md** - 5-minute guide
- 📘 **README.md** - Full documentation  
- 📋 **INDEX.md** - All files explained
- ✅ **SETUP_COMPLETE.md** - What you have

---

## Key Files

```
dataset.csv              ← 50 villages
app.py                  ← Dashboard
random_forest_model.pkl ← ML model
scaler.pkl              ← Feature scaler
config.py               ← Settings
```

---

## 30-Second Setup

```bash
# Already installed?
pip install -r requirements.txt

# Run dashboard:
streamlit run app.py

# Open browser:
http://localhost:8501
```

---

## Questions?

1. **"How do I...?"** → See QUICKSTART.md
2. **"What is...?"** → See README.md
3. **"Which file does...?"** → See INDEX.md

---

## ✨ Key Features

1. **50 Villages** - All loaded and analyzed
2. **Predictive Model** - WSI calculated for each
3. **Interactive Maps** - Color-coded stress levels
4. **Priority Table** - Sorted by importance
5. **Export Tools** - Download as CSV
6. **Professional UI** - Government-grade design

---

## Getting Help

```bash
# Check system:
python verify_setup.py

# Regenerate models:
python generate_models.py

# Launch (Windows):
setup_and_run.bat

# Launch (Mac/Linux):
./setup_and_run.sh
```

---

## Ready?

```
Pick your OS:

🪟 Windows:  setup_and_run.bat
🍎 Mac:      ./setup_and_run.sh
🐧 Linux:    ./setup_and_run.sh

Or:          streamlit run app.py
```

Then open: **http://localhost:8501**

---

**Your professional Water Governance Dashboard is ready to go!** 💧📊✨

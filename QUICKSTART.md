# 🚀 Quick Start Guide

Get the Water Governance Dashboard running in **5 minutes**!

---

## ⚡ 5-Minute Setup

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```
**Time**: 2-3 minutes (depends on internet speed)

### Step 2: Generate ML Models
```bash
python generate_models.py
```
**Time**: < 1 minute

This creates:
- ✅ `random_forest.pkl` (trained WSI prediction model)
- ✅ `scaler.pkl` (feature scaler)

### Step 3: Launch the Dashboard
```bash
streamlit run app.py
```
**Time**: < 1 minute

The app will automatically open at **http://localhost:8501**

---

## 🎯 What You'll See

### On First Load:
1. ✅ KPI dashboard with metrics
2. ✅ Interactive maps with 50 villages
3. ✅ Priority ranking table
4. ✅ Export options

### Features Available:
- 🗺️ **Interactive Maps**: Explore village locations and stress levels
- 📊 **Data Visualization**: Charts and statistics
- 🎯 **Village Simulation**: Click dropdown to analyze any village
- 📥 **Export**: Download allocation plans as CSV

---

## 🔍 Navigating the Dashboard

### Top Section: Key Metrics
```
Total Villages | High Stress Villages | Total Tankers | Top Priority Village
```

### Tabs for Maps
- **Overview Map**: See all villages color-coded by stress level
- **Route Optimization**: View tanker distribution routes

### Priority Table
Sort villages by priority score to see which need immediate attention.

### Village Details Dropdown
Select any village to see:
- Water Stress Index with progress bar
- Tanker requirements
- Storage levels
- Rainfall and groundwater data

### Export Section
Download data for reports and operations:
- Complete allocation plan
- High-priority villages only

---

## 🎨 Understanding the Colors

On the map, markers show:
- 🟢 **Green**: Low stress (Safe)
- 🟡 **Yellow**: Moderate (Monitor)
- 🟠 **Orange**: High (Action needed)
- 🔴 **Red**: Critical (Urgent intervention)

---

## 📊 Understanding Key Metrics

| Metric | Meaning |
|--------|---------|
| **WSI** | Water Stress Index (0-1)<br>Higher = More stressed |
| **Priority Score** | Allocation priority<br>70% stress + 30% population |
| **Tankers Required** | Number of 10K-liter tankers needed |
| **Stress Category** | Low / Moderate / High / Critical |

---

## 💡 Tips & Tricks

### 1. Find Most Critical Villages
- Go to **Priority Ranking Table**
- Top rows = Most urgent

### 2. Check Specific Village
- Use **Village Simulation** dropdown
- View all metrics in one place

### 3. Plan Tanker Routes
- Go to **Route Optimization** tab
- See top 5 villages with distribution paths

### 4. Report Generation
- Click **Download Allocation Plan as CSV**
- Open in Excel for further analysis

---

## 🐛 Troubleshooting

### Problem: "Module not found streamlit"
```bash
pip install -r requirements.txt
```

### Problem: Model files not found
```bash
python generate_models.py
```

### Problem: Port 8501 already in use
```bash
streamlit run app.py --server.port 8502
```

### Problem: Map not showing
- Check internet connection (Folium needs it for tiles)
- Wait 5-10 seconds for map to load

---

## 📁 Files Created

After setup, your folder will have:
```
Bugboys2/
├── dataset.csv              ← Village data (provided)
├── random_forest.pkl        ← Generated model
├── scaler.pkl               ← Generated scaler
├── app.py                   ← Main dashboard
├── generate_models.py       ← Model training script
├── requirements.txt         ← Dependencies
├── README.md                ← Full documentation
└── QUICKSTART.md            ← You are here!
```

---

## ✅ Verification Checklist

- [ ] Python 3.8+ installed
- [ ] `pip install -r requirements.txt` completed
- [ ] `python generate_models.py` completed
- [ ] `random_forest.pkl` and `scaler.pkl` files exist
- [ ] `streamlit run app.py` launches successfully
- [ ] Dashboard shows all 50 villages
- [ ] Maps display correctly

---

## 🎓 Next Steps

### Learn More About:
1. **Dashboard Features** → See `README.md`
2. **Data Structure** → Check `dataset.csv`
3. **Model Details** → Review `generate_models.py`

### Customization:
1. Modify per capita water need in `app.py` (line 202)
2. Adjust priority scoring weights (line 251)
3. Change tanker capacity (line 205)

### Advanced Usage:
1. Use your own trained models (replace `.pkl` files)
2. Add real-time data integration
3. Deploy to Streamlit Cloud for sharing

---

## 🌐 Deploy to Cloud (Optional)

### Deploy to Streamlit Cloud for Free:

1. Push folder to GitHub
2. Go to share.streamlit.io
3. Select your GitHub repo
4. Done! Dashboard is live

---

## 📞 Need Help?

Check in this order:
1. **QUICKSTART.md** (this file) - Common issues
2. **README.md** - Detailed documentation
3. **app.py comments** - Code-level details
4. **generate_models.py** - Model training details

---

## 🎉 You're All Set!

Your professional Water Governance Dashboard is ready to go!

**Start here:**
```bash
streamlit run app.py
```

Open **http://localhost:8501** in your browser and explore!

---

**Happy analyzing! 💧📊**

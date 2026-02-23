# District Water Stress Monitoring & Tanker Allocation Dashboard

## 🌍 Overview

A professional, government-grade **Water Governance Control Dashboard** built with Streamlit. This application uses **machine learning models** to predict Water Stress Index (WSI) for 50 villages and provides intelligent **tanker allocation recommendations** for optimal water resource distribution during drought conditions.

---

## ✨ Key Features

### 1. **Predictive Analytics**
- Random Forest model predicts Water Stress Index (WSI) for each village
- StandardScaler preprocessing for normalized feature inputs
- WSI values range from 0 (low stress) to 1 (critical stress)

### 2. **Intelligent Feature Engineering**
- **Rainfall Deviation**: Deviation from historical average
- **Groundwater Trend**: Change in groundwater depth
- **Water Shortfall**: Population demand vs current storage
- **Tankers Required**: Calculated based on water shortfall (10K liters/tanker capacity)
- **Priority Score**: Weighted combination of WSI (70%) and normalized population (30%)

### 3. **Interactive Visualizations**
- **Village Distribution Map**: Color-coded markers showing stress levels
- **Route Optimization Map**: Optimal tanker distribution routes from central base
- **Statistical Charts**: WSI distribution and resource analysis

### 4. **Government-Grade Dashboard**
- Clean, professional blue theme suitable for government analytics
- Comprehensive KPI metrics dashboard
- Detailed village-level analytics and simulation panel

### 5. **Data Export**
- Download complete allocation plans as CSV
- Export high-priority villages list
- Timestamped exports for version tracking

---

## 📋 Dashboard Sections

### Section 1: Header
- **Title**: District Water Stress Monitoring & Tanker Allocation Dashboard
- **Subtitle**: Predictive Drought Intelligence System
- **Timestamp**: Last updated information

### Section 2: KPI Metrics
- Total Villages Under Monitoring
- High Stress Villages (WSI > 0.7)
- Total Tankers Required
- Highest Priority Village

### Section 3: Interactive Maps
- **Overview Map**: All villages with color-coded stress indicators
- **Route Optimization**: Top 5 priority villages with distribution routes

### Section 4: Priority Ranking Table
- Sortable table with village rankings
- Columns: Rank, Village, Population, WSI, Tankers Required, Priority Score

### Section 5: Village Simulation Panel
- Dropdown to select any village
- WSI progress bar with stress category
- Detailed metrics including:
  - Population and coordinates
  - Tankers required and water shortfall
  - Storage levels and rainfall data
  - Groundwater depth and trends

### Section 6: Statistical Analysis
- WSI distribution statistics
- Tanker requirement analysis
- Population at risk assessment
- Distribution charts

### Section 7: Export Options
- Download complete allocation plan
- Download high-priority villages list

---

## 🎨 Color Coding System

### WSI Status Colors
- 🟢 **Green** (WSI < 0.3): Low stress - Adequate resources
- 🟡 **Yellow** (0.3 - 0.5): Moderate stress - Monitor closely
- 🟠 **Orange** (0.5 - 0.7): High stress - Action required
- 🔴 **Red** (WSI > 0.7): Critical - Immediate intervention needed

---

## 📁 File Structure

```
Bugboys2/
├── dataset.csv                 # 50 villages dataset with all features
├── random_forest.pkl           # Pre-trained WSI prediction model
├── scaler.pkl                  # StandardScaler for feature normalization
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## 📊 Dataset Format

The `dataset.csv` contains 50 villages with the following columns:

| Column | Description |
|--------|-------------|
| village_name | Name identifier |
| rainfall_current | Current rainfall (mm) |
| rainfall_average | Historical average rainfall (mm) |
| groundwater_depth | Current groundwater depth (m) |
| population | Village population |
| storage_capacity | Total water storage capacity (liters) |
| current_storage | Current storage level (liters) |
| latitude | Geographic latitude |
| longitude | Geographic longitude |
| historical_rainfall | Historical rainfall average |
| historical_groundwater | Historical groundwater level |

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Prepare Model Files
Ensure these files are in the same directory as `app.py`:
- `random_forest.pkl` - Trained Random Forest model
- `scaler.pkl` - StandardScaler object
- `dataset.csv` - Village dataset (already provided)

**Note**: If model files are not present, the app creates demo models automatically for demonstration purposes.

### Step 3: Run the Application
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 💡 Usage Guide

### 1. View KPI Dashboard
Upon launching, the app displays:
- Total number of villages
- Count and percentage of high-stress villages
- Total tanker requirement across all villages
- Highest priority village for intervention

### 2. Explore Village Locations
- **Overview Map**: Hover over markers to see village details
- **Route Map**: View optimized distribution routes for top priority villages

### 3. Review Priority Rankings
- Sort and filter villages by priority score
- Identify which villages need immediate attention
- Review resource allocation requirements

### 4. Simulate Village Analysis
- Select any village from dropdown
- View comprehensive stress metrics
- Check storage levels and resource needs
- Analyze rainfall and groundwater trends

### 5. Export Data
- Download allocation plans for operational reports
- Export high-priority villages for urgent action
- CSV format compatible with Excel/GIS tools

---

## 🔧 Technical Architecture

### Data Pipeline
```
Raw Data (dataset.csv)
        ↓
Feature Engineering (Rainfall Deviation, Groundwater Trend, Water Shortfall)
        ↓
Feature Scaling (StandardScaler)
        ↓
ML Prediction (Random Forest Model → WSI)
        ↓
Priority Scoring & Ranking
        ↓
Visualization & Export
```

### Core Functions

- `load_model_and_scaler()`: Loads ML models with fallback to demo models
- `load_dataset()`: Caches dataset for performance
- `calculate_feature_engineering()`: Creates derived features
- `predict_wsi()`: Generates WSI predictions
- `calculate_priority_score()`: Computes allocation priority
- `create_map()`: Generates interactive Folium map
- `create_route_map()`: Optimizes tanker distribution routes
- `export_allocation_plan()`: Prepares data for export

---

## 📈 Key Metrics Explained

### Water Stress Index (WSI)
Probability score (0-1) indicating overall water stress:
- Generated by Random Forest model
- Based on rainfall, groundwater, population, and storage
- Higher value = Greater stress

### Priority Score
Weighted metric for allocation decisions:
```
Priority = (WSI × 0.70) + (Normalized Population × 0.30)
```
- 70% weight on water stress (environmental factor)
- 30% weight on population (social factor)

### Tankers Required
Calculated based on water shortfall:
```
Water Shortfall = (Population × Annual Per Capita Demand) − Current Storage
Tankers Required = ⌈Water Shortfall ÷ 10,000 liters⌉
```

---

## 🎯 Use Cases

### 1. Emergency Response
- Identify high-stress villages requiring immediate intervention
- Generate tanker allocation lists prioritized by urgency
- Route optimization for efficient distribution

### 2. Resource Planning
- Long-term water security assessment
- Infrastructure capacity planning
- Population-aware resource distribution

### 3. Policy Analysis
- Understand geographic water stress patterns
- Demographic vulnerability assessment
- Data-driven governance decisions

### 4. Operational Management
- Daily operational dashboards for water department
- Real-time priority updates
- Export data for field operations

---

## 🔐 Data Privacy & Security

- All analysis is performed locally
- No external data transmission
- Audit trail available through exported CSVs
- Compliant with data protection standards

---

## 📝 Notes

### For ML Model Integration
To use your own trained models:
1. Train Random Forest model and fit StandardScaler
2. Save using: `pickle.dump(model, open('random_forest.pkl', 'wb'))`
3. Place both `.pkl` files in the application directory

### Per Capita Water Need
Default assumption: **50 liters/person/day**
- Can be modified in `calculate_feature_engineering()` function
- Adjust based on regional guidelines

### Demo Mode
If model files are missing, the app automatically:
1. Creates synthetic training data
2. Trains demo models
3. Continues with full functionality
4. Suitable for demonstration/testing

---

## 🐛 Troubleshooting

### Issue: "Module not found" error
**Solution**: Ensure all packages installed with `pip install -r requirements.txt`

### Issue: Map not displaying
**Solution**: Check internet connection for Folium tiles

### Issue: Very slow performance
**Solution**: Streamlit caches data. First load may be slower. Subsequent loads are faster.

### Issue: WSI all values similar
**Solution**: Check if model files exist. Update features in demo mode if needed.

---

## 📞 Support & Contact

For issues, enhancements, or integration requests:
- Contact the Water Resources Department
- Review dataset structure and model characteristics
- Validate predictions against field observations

---

## 📜 License & Compliance

This dashboard is developed for government water resource management.
Ensure compliance with local data protection and governance standards.

---

## 🌱 Future Enhancements

### Planned Features
- Real-time data integration from weather APIs
- Machine learning model retraining pipeline
- Multi-district comparison dashboard
- Seasonal forecasting
- Mobile app version
- Integration with IoT water sensors
- Citizen reporting portal

---

**Last Updated**: February 2026  
**Version**: 1.0  
**Status**: Production Ready ✅

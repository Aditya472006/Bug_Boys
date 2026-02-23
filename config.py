"""
Configuration file for Water Governance Dashboard
Customize these settings to adapt the dashboard to your needs
"""

# ==================== WATER PARAMETERS ====================
PER_CAPITA_DAILY_NEED = 50  # liters per person per day
ANNUAL_PER_CAPITA_NEED = PER_CAPITA_DAILY_NEED * 365  # liters per person per year
TANKER_CAPACITY = 10000  # liters per tanker

# ==================== PRIORITY SCORING WEIGHTS ====================
WSI_WEIGHT = 0.70  # Weight for Water Stress Index
POPULATION_WEIGHT = 0.30  # Weight for population

# ==================== WSI THRESHOLDS ====================
WSI_LOW_THRESHOLD = 0.3  # Below this = Low stress
WSI_MODERATE_THRESHOLD = 0.5  # Between 0.3 and 0.5 = Moderate
WSI_HIGH_THRESHOLD = 0.7  # Between 0.5 and 0.7 = High
# Above 0.7 = Critical

# ==================== UI COLORS ====================
COLOR_MAP = {
    'low': 'green',
    'moderate': 'yellow',
    'high': 'orange',
    'critical': 'red'
}

# ==================== MAP SETTINGS ====================
DEFAULT_MAP_ZOOM = 10
ROUTE_TOP_N_VILLAGES = 5  # Number of top villages to show on route map

# ==================== MODEL PARAMETERS ====================
TRAIN_TEST_SPLIT = 0.2
RANDOM_FOREST_PARAMS = {
    'n_estimators': 100,
    'max_depth': 10,
    'min_samples_split': 5,
    'min_samples_leaf': 2,
    'random_state': 42,
    'n_jobs': -1
}

# ==================== DATASET ====================
DATASET_FILE = 'dataset.csv'
MODEL_FILE = 'random_forest.pkl'
SCALER_FILE = 'scaler.pkl'

# ==================== FEATURE COLUMNS ====================
FEATURE_COLUMNS = [
    'rainfall_current',
    'rainfall_average',
    'groundwater_depth',
    'population',
    'current_storage'
]

# ==================== STRESS CATEGORIES ====================
STRESS_CATEGORIES = {
    'low': 'Low',
    'moderate': 'Moderate',
    'high': 'High',
    'critical': 'Critical'
}

# ==================== EXPORT SETTINGS ====================
EXPORT_COLUMNS = [
    'rank',
    'village_name',
    'population',
    'WSI',
    'water_shortfall',
    'tankers_required',
    'priority_score',
    'stress_category',
    'latitude',
    'longitude'
]

# ==================== APPLICATION SETTINGS ====================
APP_TITLE = "District Water Stress Monitoring & Tanker Allocation Dashboard"
APP_SUBTITLE = "Predictive Drought Intelligence System"
PAGE_ICON = "💧"

# ==================== DATA CACHING ====================
CACHE_TTL = 3600  # Cache time-to-live in seconds

# ==================== TANKER BASE LOCATION ====================
# Leave as None to use automatic center calculation from data
TANKER_BASE_LAT = None
TANKER_BASE_LON = None

# If you want to specify a fixed base location, use:
# TANKER_BASE_LAT = 18.5204
# TANKER_BASE_LON = 73.8567

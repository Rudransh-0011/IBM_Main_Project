# ensemble_models.py

from sklearn.ensemble import VotingRegressor
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from xgboost import XGBRegressor

# Define models
models = [
    ('gb', GradientBoostingRegressor()),
    ('rf', RandomForestRegressor()),
    ('xgb', XGBRegressor())
]

# Create ensemble
ensemble = VotingRegressor(models)
ensemble.fit(X_train, y_train)
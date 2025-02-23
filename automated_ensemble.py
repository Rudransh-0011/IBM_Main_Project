# automated_ensemble.py

from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor, StackingRegressor
from sklearn.linear_model import LinearRegression

# Define base models
base_models = [
    ('gb', GradientBoostingRegressor()),
    ('rf', RandomForestRegressor())
]

# Define meta-model
meta_model = LinearRegression()

# Create stacking ensemble
stacking = StackingRegressor(estimators=base_models, final_estimator=meta_model)
stacking.fit(X_train, y_train) # type: ignore
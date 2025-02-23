# bayesian_optimization.py

from hyperopt import fmin, tpe, hp, Trials

# Define objective function
def objective(params):
    # Train model with params
    return -accuracy  # Minimize negative accuracy

# Define search space
space = {
    'n_estimators': hp.choice('n_estimators', range(100, 1000)),
    'max_depth': hp.choice('max_depth', range(1, 20))
}

# Run optimization
if __name__ == "__main__":
    trials = Trials()
    best = fmin(objective, space, algo=tpe.suggest, max_evals=100, trials=trials)
    print(best)
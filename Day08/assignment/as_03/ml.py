import pickle
file_path = r'D:\Program Files\Python\Day08\assignment\as_03\employee'

def save_experiment(snapshot, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(snapshot,file)

def load_experiment(file_path):
    try: 
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            return data
    except FileNotFoundError:
        print("File doesnt exist")

class ExperimentSnapshot:
    def __init__(self, experiment_id: str, model_type: str, hyperparameters: dict, metrics: dict, timestamp: str):
        self.experiment_id = experiment_id
        self.model_type = model_type
        self.hyperparameters = hyperparameters
        self.metrics = metrics
        self.timestamp = timestamp

    def get_best_metric(self, metric_name):
        return self.metrics[metric_name]

exp = ExperimentSnapshot(
    experiment_id="EXP-2026-001",
    model_type="RandomForest",
    hyperparameters={"n_estimators": 100, "max_depth": 10},
    metrics={"accuracy": 0.942, "f1_score": 0.938},
    timestamp="2026-09-01 10:00:00"
)

save_experiment(exp, "experiment_01.pkl")

restored_exp = load_experiment("experiment_01.pkl")
print(restored_exp.model_type)                    # Output: RandomForest
print(restored_exp.get_best_metric("accuracy"))   # Output: 0.942

    
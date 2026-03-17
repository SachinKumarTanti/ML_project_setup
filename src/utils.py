import sys
import os

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
import dill
from src.execption import CustomException


def save_object(file_path, obj):
    try:
        DIR_PATH = os.path.dirname(file_path)
        os.makedirs(DIR_PATH, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X_train, y_train, X_test, y_test, models,params):
    try:
        report = {}

        for i in range(len(models)):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]

            # Perform GridSearchCV to find the best hyperparameters for the model
            gs = GridSearchCV(model, param, cv=3)
            gs.fit(X_train, y_train)

            # Set the model to the best parameters found by GridSearchCV
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            # Predict on the test set and calculate the r2 score
            y_test_pred = model.predict(X_test)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)
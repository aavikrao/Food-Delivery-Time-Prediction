import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from data_preprocessing import get_features_target


def train_models():

    print("=" * 50)
    print("FOOD DELIVERY TIME PREDICTION")
    print("MODEL TRAINING")
    print("=" * 50)

    # Load dataset
    X, y, numerical_features, categorical_features = get_features_target()

    print("\nDataset loaded successfully!")
    print("Total records:", len(X))
    print("Numerical features:", numerical_features)
    print("Categorical features:", categorical_features)

    # Split numerical and categorical preprocessing
    numerical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ("num", numerical_transformer, numerical_features),
        ("cat", categorical_transformer, categorical_features)
    ])

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("\nTraining samples:", len(X_train))
    print("Testing samples:", len(X_test))

    # Define models
    models = {
        "Linear Regression": LinearRegression(),

        "Random Forest": RandomForestRegressor(
            n_estimators=200,
            random_state=42,
            max_depth=None
        )
    }

    results = []
    trained_models = {}

    # Train and evaluate each model
    for name, model in models.items():

        print("\n" + "-" * 40)
        print("Training:", name)

        pipeline = Pipeline(steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ])

        pipeline.fit(X_train, y_train)

        predictions = pipeline.predict(X_test)

        mae = mean_absolute_error(y_test, predictions)
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        r2 = r2_score(y_test, predictions)

        print("\nResults for", name)
        print("MAE:", round(mae, 2))
        print("RMSE:", round(rmse, 2))
        print("R2 Score:", round(r2, 4))

        results.append({
            "Model": name,
            "MAE": mae,
            "RMSE": rmse,
            "R2 Score": r2
        })

        trained_models[name] = pipeline

    # Compare models
    results_df = pd.DataFrame(results)

    print("\n" + "=" * 50)
    print("MODEL COMPARISON")
    print("=" * 50)

    print(results_df.to_string(index=False))

    # Select best model based on lowest MAE
    best_model_name = results_df.loc[
        results_df["MAE"].idxmin(), "Model"
    ]

    best_model = trained_models[best_model_name]

    # Save best model
    joblib.dump(best_model, "best_delivery_model.pkl")

    # Save comparison results
    results_df.to_csv("model_results.csv", index=False)

    print("\nBest Model:", best_model_name)
    print("Model saved as best_delivery_model.pkl")
    print("Results saved as model_results.csv")

    print("\nMODEL TRAINING COMPLETED!")


if __name__ == "__main__":
    train_models()

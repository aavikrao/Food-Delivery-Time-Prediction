import joblib
import pandas as pd

MODEL_FILE = "best_delivery_model.pkl"


def predict_delivery_time(
    distance,
    weather,
    traffic,
    time_of_day,
    vehicle,
    preparation_time,
    courier_experience
):
    model = joblib.load(MODEL_FILE)

    new_order = pd.DataFrame([{
        "Distance_km": distance,
        "Weather": weather,
        "Traffic_Level": traffic,
        "Time_of_Day": time_of_day,
        "Vehicle_Type": vehicle,
        "Preparation_Time_min": preparation_time,
        "Courier_Experience_yrs": courier_experience
    }])

    prediction = model.predict(new_order)

    return round(prediction[0], 2)


if __name__ == "__main__":

    result = predict_delivery_time(
        distance=8.5,
        weather="Clear",
        traffic="Medium",
        time_of_day="Evening",
        vehicle="Bike",
        preparation_time=15,
        courier_experience=2
    )

    print("\nFOOD DELIVERY TIME PREDICTION")
    print("-" * 35)
    print("Predicted delivery time:", result, "minutes")

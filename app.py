import streamlit as st
import pandas as pd

from prediction import predict_delivery_time

# Page configuration
st.set_page_config(
    page_title="Food Delivery Predictor",
    page_icon="🍔",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
.main {
    background-color: #f7f8fc;
}
h1 {
    color: #29345c;
    text-align: center;
}
.subtitle {
    text-align: center;
    color: #666;
}
.result {
    background-color: #e8f5e9;
    padding: 25px;
    border-radius: 12px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("🍔 Food Delivery Time Predictor")

st.markdown(
    '<p class="subtitle">Machine Learning Based Delivery Time Estimation</p>',
    unsafe_allow_html=True
)

st.divider()

# Load dataset categories
df = pd.read_csv("Food_Delivery_Times.csv")

weather_options = sorted(df["Weather"].dropna().unique().tolist())
traffic_options = sorted(df["Traffic_Level"].dropna().unique().tolist())
time_options = sorted(df["Time_of_Day"].dropna().unique().tolist())
vehicle_options = sorted(df["Vehicle_Type"].dropna().unique().tolist())

st.subheader("📦 Enter Order Details")

col1, col2 = st.columns(2)

with col1:
    distance = st.number_input(
        "Delivery Distance (km)",
        min_value=0.1,
        value=8.5,
        step=0.5
    )

    weather = st.selectbox(
        "Weather",
        weather_options
    )

    traffic = st.selectbox(
        "Traffic Level",
        traffic_options
    )

    time_of_day = st.selectbox(
        "Time of Day",
        time_options
    )

with col2:
    vehicle = st.selectbox(
        "Vehicle Type",
        vehicle_options
    )

    preparation_time = st.number_input(
        "Preparation Time (minutes)",
        min_value=0.0,
        value=15.0,
        step=1.0
    )

    courier_experience = st.number_input(
        "Courier Experience (years)",
        min_value=0.0,
        value=2.0,
        step=0.5
    )

st.divider()

# Prediction button
if st.button("🚀 Predict Delivery Time", use_container_width=True):

    try:
        prediction = predict_delivery_time(
            distance,
            weather,
            traffic,
            time_of_day,
            vehicle,
            preparation_time,
            courier_experience
        )

        st.success("Prediction completed successfully!")

        st.markdown(
            f"""
            <div class="result">
                <h3>Estimated Delivery Time</h3>
                <h1>{prediction} Minutes</h1>
                <p>Your order's estimated delivery duration</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.balloons()

    except Exception as error:
        st.error(f"Prediction failed: {error}")

st.divider()

# Model Performance Dashboard

st.header("📊 Model Performance Dashboard")

results = pd.read_csv("model_results.csv")

st.subheader("Algorithm Comparison")
st.dataframe(
    results,
    use_container_width=True,
    hide_index=True
)

best_model = results.loc[results["R2 Score"].idxmax()]

st.subheader("🏆 Best Performing Model")

st.success(
    f"Best Model: {best_model['Model']}"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("MAE", f"{best_model['MAE']:.2f} min")

with col2:
    st.metric("RMSE", f"{best_model['RMSE']:.2f} min")

with col3:
    st.metric("R² Score", f"{best_model['R2 Score']:.4f}")

st.subheader("R² Score Comparison")

st.bar_chart(
    results.set_index("Model")[["R2 Score"]]
)


st.caption(
    "Developed using Python, Pandas, Scikit-learn and Streamlit"
)


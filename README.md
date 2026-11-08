# Food Delivery Time Prediction using Machine Learning

## Project Overview
This project uses Machine Learning to predict food delivery time based on different factors such as delivery distance, weather conditions, traffic conditions, vehicle type, and courier experience.


## Team and Roles

| Member | Entry No. | Role |
|---|---|---|
| Aavik | 2026EEB1313 | Execution Lead |
| Mahak | 2026MCB1540 | Documentation Lead |
| Anghan Divij Krunal | 2026AIB1012 | PPT Lead |
| Nanong Tamut | 2026DAB1298 | Video Lead |


## Objectives
- Predict food delivery time using Machine Learning.
- Perform data preprocessing and exploratory data analysis.
- Train and compare multiple regression algorithms.
- Evaluate model performance using MAE, RMSE, and R² Score.
- Develop an interactive web application using Streamlit.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

## Machine Learning Algorithms
1. Linear Regression
2. Random Forest Regression

## Project Structure

```text
ai-project/
│
├── Food_Delivery_Times.csv
├── data_preprocessing.py
├── eda.py
├── model_training.py
├── prediction.py
├── main.py
├── app.py
│
├── best_delivery_model.pkl
├── model_results.csv
│
├── delivery_time_distribution.png
├── distance_vs_delivery.png
├── traffic_vs_delivery.png
│
├── requirements.txt
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project:

```bash
cd ai-project
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal to access the application.

## Model Evaluation

The models are evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

Actual model results are available in `model_results.csv`.

## Future Scope
- Integrate real-time traffic information.
- Use a larger delivery dataset.
- Explore advanced machine learning algorithms.
- Deploy the application online.

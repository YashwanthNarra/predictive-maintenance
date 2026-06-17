import streamlit as st
import pandas as pd
import joblib

# Load model and columns
model = joblib.load("../artifacts/model.pkl")
feature_columns = joblib.load("../artifacts/feature_columns.pkl")

st.title("Predictive Maintenance System")

st.set_page_config(
    page_title="Predictive Maintenance",
    page_icon="🔧",
    layout="centered"
)

st.markdown(
    """
    Predict machine failure based on operating conditions.
    """
)

machine_type = st.selectbox(
    "Machine Type",
    ["L", "M", "H"]
)

air_temp = st.number_input(
    "Air Temperature (K)",
    value=300.0
)

process_temp = st.number_input(
    "Process Temperature (K)",
    value=310.0
)

rot_speed = st.number_input(
    "Rotational Speed (rpm)",
    value=1500
)

torque = st.number_input(
    "Torque (Nm)",
    value=40.0
)

tool_wear = st.number_input(
    "Tool Wear (min)",
    value=10
)

if st.button("Predict"):

    input_df = pd.DataFrame({
        "Air_temperature": [air_temp],
        "Process_temperature": [process_temp],
        "Rotational_speed": [rot_speed],
        "Torque": [torque],
        "Tool_wear": [tool_wear]
    })

    # Dummy variables
    input_df["L"] = 0
    input_df["M"] = 0

    if machine_type == "L":
        input_df["L"] = 1

    elif machine_type == "M":
        input_df["M"] = 1

    input_df = input_df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    prob = model.predict_proba(input_df)[0][1]

    st.write(f"Failure Probability percentage : {(100*prob):0.2f}%")

    if prob >= 0.5:
        st.error("Machine Failure Predicted")
    else:
        st.success("No Machine Failure Predicted")
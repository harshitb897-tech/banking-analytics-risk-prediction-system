import streamlit as st
import joblib
import pandas as pd
from pathlib import Path

# Project folder ka exact path
BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"

# Page Configuration
st.set_page_config(
    page_title="Banking Analytics & Risk Prediction System",
    page_icon="🏦",
    layout="wide"
)
# Load Loan Models
loan_model = joblib.load(MODELS_DIR / "loan_prediction_model.pkl")
loan_scaler = joblib.load(MODELS_DIR / "loan_scaler.pkl")

# Load Credit Risk Model
credit_model = joblib.load(MODELS_DIR / "credit_risk_balanced_model.pkl")

# Load Credit Risk Scaler
credit_scaler = joblib.load(MODELS_DIR / "credit_risk_balanced_scaler.pkl")

# Load Fraud Detection Model
fraud_model = joblib.load(MODELS_DIR / "fraud_detection_model.pkl")

# Load Fraud Scaler
fraud_scaler = joblib.load(MODELS_DIR / "fraud_scaler.pkl")

# Load Customer Segmentation Model
customer_model = joblib.load(
    MODELS_DIR / "customer_segmentation_model.pkl"
)

# Load Customer Segmentation Scaler
customer_scaler = joblib.load(
    MODELS_DIR / "customer_segmentation_scaler.pkl"
)

# Main Title
st.title("🏦 Banking Analytics & Risk Prediction System")
st.write("Machine Learning based banking risk analysis and customer insights")

# Sidebar Navigation
st.sidebar.title("Navigation")

option = st.sidebar.selectbox(
    "Select Module",
    [
        "Home",
        "Loan Approval Prediction",
        "Credit Risk Prediction",
        "Fraud Detection",
        "Customer Segmentation"
    ]
)

# Home
if option == "Home":
    st.subheader("Welcome to Banking Analytics System")
    st.info("Select a module from the sidebar to continue.")

# Loan Approval
elif option == "Loan Approval Prediction":
    st.subheader("🏦 Loan Approval Prediction")
    st.write("Enter applicant details to predict loan approval.")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        self_employed = st.selectbox("Self Employed", ["Yes", "No"])
        applicant_income = st.number_input(
            "Applicant Income",
            min_value=0,
            value=5000
        )

    with col2:
        coapplicant_income = st.number_input(
            "Coapplicant Income",
            min_value=0,
            value=0
        )
        loan_amount = st.number_input(
            "Loan Amount",
            min_value=0,
            value=100
        )
        loan_term = st.number_input(
            "Loan Amount Term",
            min_value=12,
            value=360
        )
        credit_history = st.selectbox(
            "Credit History",
            [1.0, 0.0]
        )
        property_area = st.selectbox(
            "Property Area",
            ["Rural", "Semiurban", "Urban"]
        )

    if st.button("Predict Loan Approval"):

        # Convert categorical values to numbers
        gender_value = 1 if gender == "Male" else 0
        married_value = 1 if married == "Yes" else 0
        dependents_value = 3 if dependents == "3+" else int(dependents)
        education_value = 0 if education == "Graduate" else 1
        self_employed_value = 1 if self_employed == "Yes" else 0

        property_value = {
            "Rural": 0,
            "Semiurban": 1,
            "Urban": 2
        }[property_area]

        input_data = [[
            gender_value,
            married_value,
            dependents_value,
            education_value,
            self_employed_value,
            applicant_income,
            coapplicant_income,
            loan_amount,
            loan_term,
            credit_history,
            property_value
        ]]

        input_df = pd.DataFrame(
            input_data,
            columns=[
                "Gender",
                "Married",
                "Dependents",
                "Education",
                "Self_Employed",
                "ApplicantIncome",
                "CoapplicantIncome",
                "LoanAmount",
                "Loan_Amount_Term",
                "Credit_History",
                "Property_Area"
            ]
        )

        # Scale input
        input_scaled = loan_scaler.transform(input_df)

        # Prediction
        prediction = loan_model.predict(input_scaled)[0]

        if prediction == 1:
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Rejected")
# Credit Risk
elif option == "Credit Risk Prediction":
    st.subheader("📊 Credit Risk Prediction")
    st.write("Enter applicant and loan details to assess credit risk.")

    col1, col2 = st.columns(2)

    with col1:
        person_age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=30
        )

        person_income = st.number_input(
            "Annual Income",
            min_value=0,
            value=50000
        )

        person_home_ownership = st.selectbox(
            "Home Ownership",
            ["RENT", "OWN", "MORTGAGE", "OTHER"]
        )

        person_emp_length = st.number_input(
            "Employment Length (Years)",
            min_value=0.0,
            value=5.0
        )

        loan_intent = st.selectbox(
            "Loan Intent",
            [
                "PERSONAL",
                "EDUCATION",
                "MEDICAL",
                "VENTURE",
                "HOMEIMPROVEMENT",
                "DEBTCONSOLIDATION"
            ]
        )

        loan_grade = st.selectbox(
            "Loan Grade",
            ["A", "B", "C", "D", "E", "F", "G"]
        )

    with col2:
        loan_amnt = st.number_input(
            "Loan Amount",
            min_value=0,
            value=10000
        )

        loan_int_rate = st.number_input(
            "Interest Rate (%)",
            min_value=0.0,
            value=10.0
        )

        loan_percent_income = st.number_input(
            "Loan Percent of Income",
            min_value=0.0,
            max_value=1.0,
            value=0.20
        )

        cb_person_default_on_file = st.selectbox(
            "Previous Default on File",
            ["N", "Y"]
        )

        cb_person_cred_hist_length = st.number_input(
            "Credit History Length (Years)",
            min_value=0,
            value=5
        )

    if st.button("Predict Credit Risk"):

        # Convert categorical values to numbers
        home_ownership_map = {
            "RENT": 0,
            "OWN": 1,
            "MORTGAGE": 2,
            "OTHER": 3
        }

        loan_intent_map = {
            "PERSONAL": 0,
            "EDUCATION": 1,
            "MEDICAL": 2,
            "VENTURE": 3,
            "HOMEIMPROVEMENT": 4,
            "DEBTCONSOLIDATION": 5
        }

        loan_grade_map = {
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
            "E": 4,
            "F": 5,
            "G": 6
        }

        default_map = {
            "N": 0,
            "Y": 1
        }

        input_data = [[
            person_age,
            person_income,
            home_ownership_map[person_home_ownership],
            person_emp_length,
            loan_intent_map[loan_intent],
            loan_grade_map[loan_grade],
            loan_amnt,
            loan_int_rate,
            loan_percent_income,
            default_map[cb_person_default_on_file],
            cb_person_cred_hist_length
        ]]

        input_df = pd.DataFrame(
            input_data,
            columns=[
                "person_age",
                "person_income",
                "person_home_ownership",
                "person_emp_length",
                "loan_intent",
                "loan_grade",
                "loan_amnt",
                "loan_int_rate",
                "loan_percent_income",
                "cb_person_default_on_file",
                "cb_person_cred_hist_length"
            ]
        )

        # Scale input
        input_scaled = credit_scaler.transform(input_df)

        # Prediction
        prediction = credit_model.predict(input_scaled)[0]

        if prediction == 1:
            st.error("⚠️ High Credit Risk")
        else:
            st.success("✅ Low Credit Risk")

# Fraud Detection
elif option == "Fraud Detection":
    st.subheader("🚨 Fraud Detection")
    st.write("Enter transaction details to check whether a transaction is potentially fraudulent.")

    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=100.0
    )

    time = st.number_input(
        "Transaction Time",
        min_value=0.0,
        value=1000.0
    )

    st.write("Enter V1 to V28 transaction features:")

    cols = st.columns(4)

    v_values = []

    for i in range(28):
        with cols[i % 4]:
            value = st.number_input(
                f"V{i+1}",
                value=0.0,
                format="%.6f"
            )
            v_values.append(value)

    if st.button("Check Transaction"):

        input_data = [[time] + v_values + [amount]]

        input_df = pd.DataFrame(
            input_data,
            columns=[
                "Time",
                *[f"V{i}" for i in range(1, 29)],
                "Amount"
            ]
        )

        # Scale input
        input_scaled = fraud_scaler.transform(input_df)

        # Isolation Forest prediction
        prediction = fraud_model.predict(input_scaled)[0]

        if prediction == -1:
            st.error("🚨 Potential Fraudulent Transaction Detected")
        else:
            st.success("✅ Transaction Appears Normal")

# Customer Segmentation
# Customer Segmentation
elif option == "Customer Segmentation":

    st.subheader("👥 Customer Segmentation")
    st.write(
        "Enter customer transaction details to identify the customer segment."
    )

    col1, col2 = st.columns(2)

    with col1:
        total_transactions = st.number_input(
            "Total Transactions",
            min_value=0,
            value=10
        )

        total_transaction_amount = st.number_input(
            "Total Transaction Amount (INR)",
            min_value=0.0,
            value=10000.0
        )

    with col2:
        average_transaction_amount = st.number_input(
            "Average Transaction Amount (INR)",
            min_value=0.0,
            value=1000.0
        )

        account_balance = st.number_input(
            "Account Balance (INR)",
            min_value=0.0,
            value=50000.0
        )

    if st.button("Identify Customer Segment"):

        input_data = [[
            total_transactions,
            total_transaction_amount,
            average_transaction_amount,
            account_balance
        ]]

        input_df = pd.DataFrame(
            input_data,
            columns=[
                "Total_Transactions",
                "Total_Transaction_Amount",
                "Average_Transaction_Amount",
                "Account_Balance"
            ]
        )

        # Scale input
        input_scaled = customer_scaler.transform(input_df)

        # Predict cluster
        cluster = customer_model.predict(input_scaled)[0]

        st.success(f"✅ Customer belongs to Segment {cluster}")

        # Segment description
        segment_names = {
            0: "Regular / Low-Value Customers",
            1: "Active / Medium-Value Customers",
            2: "High-Value Customers",
            3: "Premium / High-Activity Customers"
        }

        st.info(
            f"Customer Segment: {segment_names.get(cluster, f'Segment {cluster}')}"
        )
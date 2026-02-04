import streamlit as st
import pickle
import pandas as pd
import plotly.express as px
import base64


st.set_page_config(page_title='TECO Customer Churn Predictor', page_icon= "TECOCo.jpeg", layout="wide")
st.title('TECO Customer Churn Predictor')

with st.sidebar:

    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="display:flex; justify-content:center;">
            <img src="data:image/jpeg;base64,{}" width="120">
        </div>
        """.format(base64.b64encode(open("TECOCo.jpeg", "rb").read()).decode()),
        unsafe_allow_html=True
    )
    st.markdown("<hr style='margin:10px 0;'>", unsafe_allow_html=True)

    st.markdown(
        "<h4 style='text-align:center; margin-top:0; margin-bottom:0;'>Customer Churn Predictor</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            background-color:#f3f4f6;
            padding:12px;
            border-radius:10px;
            text-align:center;
        ">
            <p style="margin:0; font-size:12px; color:black;">Machine Learning Model Type</p>
            <p style="margin:0; font-size:18px; font-weight:500; color:black">AdaBoost</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<hr style='margin:12px 0;'>", unsafe_allow_html=True)

    st.markdown(
        "<p style='font-size:13px; text-align:center;'>"
        "This system estimates customer churn probability using Machine learning based on demographics, service usage, contract type, and billing behavior."
        "</p>",
        unsafe_allow_html=True
    )

#Load Model
@st.cache_resource
def load_model():
    with open('model_Ada_tuned.sav', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

container = st.container(border=True)

with container:

    st.markdown(
        "<span style='font-size:18px; font-weight:700;'>Customer Personal Information</span>",
        unsafe_allow_html=True
    )

    gender = st.radio(
        "# Select Gender",
        ["Male", "Female"],
        horizontal=True
    )

    st.markdown("<hr style='margin:4px 0;'>", unsafe_allow_html=True)

    st.markdown(
        "<span style='font-size:15px; font-weight:600;'>Customer Status</span>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        senior_citizen = "Yes" if st.checkbox("Senior Citizen") else "No"
        partner = "Yes" if st.checkbox("Has Partner") else "No"

    with col2:
        dependents = "Yes" if st.checkbox("Has Dependents") else "No"

st.markdown(
    "<span style='font-size:16px; font-weight:600;'>Customer Tenure</span>",
    unsafe_allow_html=True
)

tenure = st.slider(
    'Tenure (months)',
    0, 72,
    help='Number of months the customer has stayed with the company.'
)

container3 = st.container(border=True)

with container3:

    st.markdown(
        "<span style='font-size:16px; font-weight:600;'>Phone Services</span>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1,1])

    with col1:
        phone_service = st.radio(
            "Phone Service",
            ["Yes", "No"],
            horizontal=True
        )

    with col2:
        if phone_service == "Yes":
            st.success("Phone service active")
            multiple_line = "Yes" if st.toggle(
                "Multiple Lines Enabled",
                help="Customer has more than one phone line."
            ) else "No"

        else:
            multiple_line = "No phone service"
            st.warning("Multiple line service unavailable")

    if phone_service == "Yes" and multiple_line == "Yes":
        st.info("Customer uses multi-line phone setup.")

container3 = st.container(border=True)

with container3:

    st.markdown(
        "<span style='font-size:18px; font-weight:700;'>Internet Details</span>",
        unsafe_allow_html=True
    )

    st.caption("Customer internet configuration.")

    st.markdown("<hr style='margin:6px 0;'>", unsafe_allow_html=True)

    internet_service = st.selectbox('internet service',
        ['DSL', 'Fiber optic', 'No']
    )

    if internet_service in ('DSL', 'Fiber optic'):

        st.markdown('##### Internet Service perks')

        st.caption("Select all Internet Service perks currently active on the customer's account.")

        container = st.container(border=True)

        with container:
            col1, col2 = st.columns(2)

            with col1:
                online_security   = 'Yes' if st.checkbox('Online Security') else 'No'
                online_backup     = 'Yes' if st.checkbox('Online Backup') else 'No'
                device_protection = 'Yes' if st.checkbox('Device Protection') else 'No'

            with col2:
                tech_support    = 'Yes' if st.checkbox('Tech Support') else 'No'
                StreamingTV     = 'Yes' if st.checkbox('Streaming TV') else 'No'
                StreamingMovies = 'Yes' if st.checkbox('Streaming Movies') else 'No'

    else:
        online_security = online_backup = device_protection = tech_support = StreamingTV = StreamingMovies = 'No internet service'

    if internet_service == 'No':
        st.warning('Internet perks are unavailable without internet service.')

container4 = st.container(border=True)

with container4:

    st.markdown(
        "<span style='font-size:18px; font-weight:700;'>Contract & Billing Details</span>",
        unsafe_allow_html=True
    )

    st.caption("Customer subscription and payment configuration.")

    st.markdown("<hr style='margin:6px 0;'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        contract = st.selectbox(
            "Contract Type",
            ["Month-to-month", "One year", "Two year"],
            help="Longer contracts usually correlate with lower churn risk."
        )

        billing = "Yes" if st.toggle(
            "Paperless Billing Enabled",
            help="Customer receives bills electronically instead of paper invoices."
        ) else "No"

    with col2:
        payment_method = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ],
            help="Automatic payment methods generally reduce churn probability."
        )

    st.markdown(
        "<span style='font-size:16px; font-weight:600;'>Billing Charges</span>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        monthly_charge = st.number_input(
            'Monthly Charge',
            min_value=18.0,
            max_value=119.0,
            step=1.0,
            format='%.2f',
            help='Recurring monthly subscription cost.'
        )

    with col2:
        total_charge = st.number_input(
            'Total Charge',
            min_value=18.0,
            max_value=8685.0,
            step=10.0,
            format='%.2f',
            help='Total amount billed to the customer so far.'
        )

actual_charges = monthly_charge * tenure

if st.button('Predict'):
    df = pd.DataFrame([{
        'gender': gender,
        'SeniorCitizen': senior_citizen,
        'Partner': partner,
        'Dependents': dependents,
        'tenure': tenure,
        'PhoneService': phone_service,
        'MultipleLines': multiple_line,
        'InternetService': internet_service,
        'OnlineSecurity' : online_security,
        'OnlineBackup' : online_backup,
        'DeviceProtection' : device_protection,
        'TechSupport' : tech_support,
        'StreamingTV' : StreamingTV, 
        'StreamingMovies' : StreamingMovies,
        'Contract' : contract,
        'PaperlessBilling' : billing,
        'PaymentMethod' : payment_method,
        'MonthlyCharges' : monthly_charge,
        'TotalCharges' : total_charge,
        'ActualTotalCharges' : actual_charges
    }])
    df['SeniorCitizen'] = df['SeniorCitizen'].map({'Yes': 1, 'No': 0})

    col1, col2 = st.columns(2)

    with col1:
        pred = model.predict(df)[0]
        prob_churn = model.predict_proba(df)[0, 1]
        prob_stay = 1 - prob_churn

        status = 'Likely to Churn' if pred == 1 else 'Likely to Stay'
        color = '#f04b4b' if pred == 1 else '#52ea8a'

        st.markdown(f'''
        <div style='
            padding:18px;
            border-radius:12px;
            background-color:{color}20;
            border:1px solid {color};
        '>
            <h3 style='margin-bottom:8px;'>Prediction Result</h3>
            <h2 style='color:{color}; margin-top:0;'>{status}</h2>
            <p style='font-size:16px; margin-bottom:4px;'>
                <b>Churn Probability:</b> {prob_churn*100:.2f}%
            </p>
            <p style='font-size:16px;'>
                <b>Stay Probability:</b> {prob_stay*100:.2f}%
            </p>
        </div>
        ''', unsafe_allow_html=True)

    with col2:
        prob_df = pd.DataFrame({
            'Outcome': ['Stay', 'Churn'],
            'Probability': [prob_stay, prob_churn]
        })

        fig = px.pie(
            prob_df,
            names='Outcome',
            values='Probability',
            hole=0.45,
            color='Outcome',
            color_discrete_map={
                'Stay': '#21a150',
                'Churn': '#ca2b2b'
            }
        )

        fig.update_traces(
            textinfo='percent+label',
            hovertemplate='<b>%{label}</b><br>Probability: %{percent}<extra></extra>',
            pull=[0, 0.1]
        )

        fig.update_layout(
            title='Customer Churn Probability Distribution',
            legend_title='Outcome',
        )

        st.plotly_chart(fig, use_container_width=True)
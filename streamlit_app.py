import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk
import time
from urllib.error import URLError
import requests

import datetime



###########  Header Start ############################

 

import streamlit as st
# Title Section and Dropdown Menu
st.markdown(
    """
   <style>
        /* Title Section Styling */
        .title-section {
            padding: 20px;
            background: linear-gradient(135deg, #b9d2ec, #bcd2e58c);
            color: white;
            border-radius: 25px;
            box-shadow: 0 12px 18px rgba(0, 0.44, 0.55, 0.55);
            text-align: center;
            margin-top: 20px;
            margin-bottom: 20px;
            transition: all 0.3s ease-in-out;
        }

             .title-section h1:   {
            text-shadow: 0 0 5px rgba(255, 255, 255, 1),
                         0 0 10px rgba(0, 123, 255, 1),
                         0 0 15px rgba(0, 123, 255, 1);
            transform: scale(1.1);
        }

        

        .title-section h1 {
            font-size: 3em;
            font-weight: bold;
            margin-bottom: 10px;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.9),
                         0 0 20px rgba(0, 123, 255, 0.8),
                         0 0 30px rgba(0, 123, 255, 0.7);
            transition: all 0.3s ease-in-out;
        }

        .title-section h1:hover {
            text-shadow: 0 0 5px rgba(255, 255, 255, 1),
                         0 0 10px rgba(0, 123, 255, 1),
                         0 0 15px rgba(0, 123, 255, 1);
            transform: scale(1.1);
        }

        .title-section h2 {
            font-size: 2em;
            font-weight: semi-bold;
            margin-bottom: 15px;
            text-shadow: 0 0 8px rgba(255, 255, 255, 0.8),
                         0 0 15px rgba(0, 123, 255, 0.7);
        }

        .title-section p {
            font-size: 1.2em;
            margin: 0;
            line-height: 1.6;
            color: rgba(255, 255, 255, 0.9);
        }

    

    
        /* Dropdown Button Styling */
        .dropdown-button {
            background-color: #b3cfed;
            color: white;
            font-size: 12px;
            font-weight: bold;
            padding: 10px 15px;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0.44, 0.55);
            transition: all 0.3s ease-in-out;
            text-align: center;
        }

        .dropdown-button:hover {
            background-color: #0056b3;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.55);
        }

        /* Dropdown Menu Styling */
        .dropdown-container {
            position: absolute;
            top: 20px;
            right: 20px; /* Positioning the dropdown to the right-hand side */
            display: inline-block;
        }

        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f8f9fa;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            border-radius: 10px;
            margin-top: 10px;
            min-width: 220px; /* Slightly larger for better readability */
    right: 0; /* Align dropdown content to the right */
            z-index: 1;
            right: 0; /* Align the dropdown to the right */
        }

        .dropdown-content a {
            color: black;
            font-size: 14px;
            font-weight: 500;
            padding: 10px 20px;
            text-decoration: none;
            display: block;
            border-radius: 5px;
            transition: background-color 0.2s ease;
        }

        .dropdown-content a:hover {
            background-color: #cce4f7;
            color: #0056b3;
        }

        /* Show the dropdown content on hover */
        .dropdown-container:hover .dropdown-content {
            display: block;
        }

        /* Dropdown Arrow Styling */
        .dropdown-arrow {
            margin-left: 5px;
            font-size: 12px;
        }

        /* Responsive Adjustments */
        @media screen and (max-width: 768px) {
            .dropdown-button {
                font-size: 10px;
                padding: 8px 12px;
            }

            .dropdown-content {
                min-width: 180px; /* Adjust dropdown width for smaller screens */
            }

            .dropdown-content a {
                font-size: 12px;
                padding: 8px 15px;
            }
        }
  </style>



    <!-- Dropdown Menu -->
    <div class="dropdown-container">
        <button class="dropdown-button">
            Menu <span class="dropdown-arrow">▼</span>
        </button>
        <div class="dropdown-content">
            <a href="/?page=Home">Home</a>
            <a href="/?page=Calculators">Calculators</a>
            <a href="/?page=Business">Business</a>
            <a href="/?page=RealEstate">Real Estate</a>
            <a href="/?page=Investment">Investment</a>
            <a href="/?page=MarketAnalysis">Market Analysis</a>
            <a href="/?page=Trends">Trends</a>
            <a href="/?page=Contact">Contact</a>
        </div>
    </div>

    <!-- Title Section -->
    <div class="title-section">
        <h1>VillaTerras Ai</h1>
        <h2>Ai Real Estate Agent | Assistant</h2>
        <p><strong>VillaTerras Ai Real Estate Dashboard</strong>.</p>
        <p>All Real Estate Knowledge in One Place.</p>
        
 
 

  <p>Analyze, compare, and manage properties with advanced metrics and tools, all with VillaTerras.com</p>


 
    <p style="font-size:12px; color:lightgrey;">
      Written by Ekbalam.
    </p> 


    """,
    unsafe_allow_html=True
)


###########  Header End ############################



# Utility function to load JSON data
import streamlit as st
import pandas as pd
import numpy as np
from urllib.error import URLError

# Utility function to load JSON data
@st.cache_data
def from_data_file(filename):
    """Fetch data from a remote JSON file."""
    url = f"https://raw.githubusercontent.com/streamlit/example-data/master/hello/v1/{filename}"
    try:
        return pd.read_json(url)
    except ValueError:
        st.error(f"Error loading data from {url}. Ensure the file exists and is formatted correctly.")
        return pd.DataFrame()

# Sidebar configuration function
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# --- Not so DUMMY Data Loader ---


@st.cache_data
def load_data(filename):
    """Placeholder function to load JSON data."""
    try:
        return pd.read_json(filename)
    except ValueError:
        st.error(f"Error loading data from {filename}. Ensure the file exists and is formatted correctly.")
        return pd.DataFrame()








def configure_sidebar():
    """Sets up the sidebar and returns the user inputs."""
    st.sidebar.header("Filters")

    # Location Details
    st.sidebar.subheader("Location Details")
    location_details = {
        "address": st.sidebar.text_input("Address", value="", key="location_address_sidebar_1"),
        "city": st.sidebar.text_input("City", value="", key="location_city_sidebar_1"),
        "state": st.sidebar.text_input("State", value="", key="location_state_sidebar_1"),
        "zip": st.sidebar.text_input("Zip Code", value="", key="location_zip_sidebar_1"),
    }

    # Property Details
    st.sidebar.subheader("Property Details")
    property_details = {
        "price_range": st.sidebar.slider(
            "Price Range ($)", 50000, 5000000, (100000, 1000000), step=50000, key="price_range_sidebar"
        ),
        "bedrooms": st.sidebar.slider("Bedrooms", 1, 10, (2, 4), key="bedrooms_sidebar"),
        "bathrooms": st.sidebar.slider("Bathrooms", 1, 10, (1, 3), key="bathrooms_sidebar"),
        "area_range": st.sidebar.slider(
            "Living Area (sq ft)", 500, 10000, (1000, 5000), step=100, key="area_range_sidebar"
        ),
        "land_area": st.sidebar.slider(
            "Land Area (sq ft)", 1000, 50000, (5000, 20000), step=500, key="land_area_sidebar"
        ),
    }

    # Financial Details
    st.sidebar.subheader("Financial Details")
    financial_details = {
        "property_price": st.sidebar.number_input("Property Price ($)", value=300000, step=10000, key="property_price_sidebar"),
        "down_payment": st.sidebar.number_input("Down Payment ($)", value=60000, step=1000, key="down_payment_sidebar"),
        "closing_costs": st.sidebar.number_input("Closing Costs ($)", value=5000, step=500, key="closing_costs_sidebar"),
        "rehab_costs": st.sidebar.number_input("Rehabilitation Costs ($)", value=10000, step=500, key="rehab_costs_sidebar"),
        "annual_property_taxes": st.sidebar.number_input(
            "Annual Property Taxes ($)", value=5000, step=500, key="annual_property_taxes_sidebar"
        ),
        "annual_insurance": st.sidebar.number_input("Annual Insurance ($)", value=1200, step=100, key="annual_insurance_sidebar"),
        "annual_utilities": st.sidebar.number_input("Annual Utilities ($)", value=3000, step=500, key="annual_utilities_sidebar"),
        "maintenance_perc": st.sidebar.number_input("Maintenance (% of Rent)", value=10, step=1, key="maintenance_perc_sidebar"),
        "capex_perc": st.sidebar.number_input("Capital Expenditure (% of Rent)", value=10, step=1, key="capex_perc_sidebar"),
        "mgmt_perc": st.sidebar.number_input("Property Management (% of Rent)", value=8, step=1, key="mgmt_perc_sidebar"),
        "vacancy_perc": st.sidebar.number_input("Vacancy Rate (%)", value=5, step=1, key="vacancy_perc_sidebar"),
        "hoa_fees": st.sidebar.number_input("HOA Fees (Monthly $)", value=0, step=50, key="hoa_fees_sidebar"),
        "other_income": st.sidebar.number_input("Other Income (Monthly $)", value=0, step=50, key="other_income_sidebar"),
        "interest_rate": st.sidebar.number_input("Interest Rate (%)", value=4.5, step=0.1, key="interest_rate_sidebar"),
        "loan_term": st.sidebar.number_input("Loan Term (Years)", value=30, step=1, key="loan_term_sidebar"),
        "annual_rent_income": st.sidebar.number_input(
            "Annual Rent Income ($)", value=30000, step=1000, key="annual_rent_income_sidebar"
        ),
        "appreciation_rate": st.sidebar.number_input("Appreciation Rate (%)", value=3.0, step=0.1, key="appreciation_rate_sidebar"),
        "inflation_rate": st.sidebar.number_input("Inflation Rate (%)", value=2.0, step=0.1, key="inflation_rate_sidebar"),
        "selling_costs_perc": st.sidebar.number_input("Selling Costs (% of Sale Price)", value=6.0, step=0.1, key="selling_costs_sidebar"),
    }

    return location_details, property_details, financial_details










# Calculation function
def calculate_metrics(financial_details):
    """Calculate key financial metrics."""
    price = financial_details["property_price"]
    rent = financial_details["annual_rent_income"]
    down = financial_details["down_payment"]
    closing = financial_details["closing_costs"]
    rehab = financial_details["rehab_costs"]
    taxes = financial_details["annual_property_taxes"]
    insurance = financial_details["annual_insurance"]
    utilities = financial_details["annual_utilities"]
    maintenance_perc = financial_details["maintenance_perc"]
    capex_perc = financial_details["capex_perc"]
    mgmt_perc = financial_details["mgmt_perc"]
    vacancy_perc = financial_details["vacancy_perc"]
    rate = financial_details["interest_rate"]
    term = financial_details["loan_term"]
    hoa_fees = financial_details["hoa_fees"] * 12  # Annualized
    other_income = financial_details["other_income"] * 12  # Annualized

    loan_amount = price - down
    monthly_rate = rate / 100 / 12
    num_payments = term * 12

    try:
        monthly_payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)
    except ZeroDivisionError:
        monthly_payment = 0

    annual_debt_service = monthly_payment * 12
    operating_expenses = taxes + insurance + utilities + hoa_fees + (rent * (maintenance_perc + capex_perc + mgmt_perc) / 100)
    effective_gross_income = rent * (1 - vacancy_perc / 100) + other_income
    noi = effective_gross_income - operating_expenses

    cash_flow = noi - annual_debt_service
    total_investment = down + closing + rehab
    cap_rate = (noi / price) * 100 if price > 0 else 0
    cash_on_cash = (cash_flow / total_investment) * 100 if total_investment > 0 else 0
    break_even_rent = (operating_expenses + annual_debt_service) / (1 - vacancy_perc / 100)

    return {
        "Monthly Payment": monthly_payment,
        "Annual Debt Service": annual_debt_service,
        "Operating Expenses": operating_expenses,
        "Effective Gross Income": effective_gross_income,
        "NOI": noi,
        "Cash Flow": cash_flow,
        "Cap Rate": cap_rate,
        "Cash on Cash": cash_on_cash,
        "Break-Even Rent": break_even_rent,
    }







# Main function  INVESTMENT CALCULATOR            WORKS  

def main():
    st.title("Real Estate Investment Calculator")
    st.write("Analyze your real estate investment with detailed metrics.")

    # Sidebar Inputs
    location_details, property_details, financial_details = configure_sidebar()

    # Calculate Metrics
    metrics = calculate_metrics(financial_details)

    # Display Metrics
    st.header("Investment Metrics")
    for key, value in metrics.items():
        st.write(f"**{key}:** ${value:,.2f}" if "($)" in key or "Payment" in key else f"**{key}:** {value:.2f}%")

    st.write("Use the sidebar to adjust variables and see real-time analysis.")


# Run the app
if __name__ == "__main__":
    main()







# Sensitivity Analysis Function
def sensitivity_analysis(rent_income, property_price, down_payment, closing_costs, rehab_costs,
                         taxes, insurance, utilities, maintenance, capex, mgmt_perc, vacancy_perc,
                         hoa_fees, other_income, rate, term, appreciation_rate=0.0, inflation_rate=0.0):
    """
    Perform sensitivity analysis on rent and price, considering additional variables.
    """
    rent_range = np.linspace(rent_income * 0.8, rent_income * 1.2, 20)
    price_range = np.linspace(property_price * 0.8, property_price * 1.2, 20)

    # Call helper function to compute sensitivity analysis results
    return perform_sensitivity_analysis(rent_range, price_range, down_payment, closing_costs, rehab_costs,
                                        taxes, insurance, utilities, maintenance, capex, mgmt_perc, vacancy_perc,
                                        hoa_fees, other_income, rate, term, appreciation_rate, inflation_rate)


# Perform Sensitivity Analysis Function
def perform_sensitivity_analysis(rent_range, price_range, down_payment, closing_costs, rehab_costs,
                                 taxes, insurance, utilities, maintenance, capex, mgmt_perc, vacancy_perc,
                                 hoa_fees, other_income, rate, term, appreciation_rate, inflation_rate):
    """
    Perform sensitivity analysis for a range of rent and price combinations.
    """
    results = []

    for rent in rent_range:
        for price in price_range:
            # Prepare financial details for the current combination
            financial_details = {
                "property_price": price,
                "annual_rent_income": rent,
                "down_payment": down_payment,
                "closing_costs": closing_costs,
                "rehab_costs": rehab_costs,
                "annual_property_taxes": taxes,
                "annual_insurance": insurance,
                "annual_utilities": utilities,
                "maintenance_perc": maintenance,
                "capex_perc": capex,
                "mgmt_perc": mgmt_perc,
                "vacancy_perc": vacancy_perc,
                "hoa_fees": hoa_fees,
                "other_income": other_income,
                "interest_rate": rate,
                "loan_term": term,
                "appreciation_rate": appreciation_rate,
                "inflation_rate": inflation_rate,
            }

            # Calculate metrics for the current combination
            metrics = calculate_metrics(financial_details)

            # Append results for this combination
            results.append({
                "Rent Income ($)": rent,
                "Property Price ($)": price,
                "Cap Rate (%)": metrics.get("Cap Rate", 0),  # Default to 0 if not found
                "Cash Flow ($)": metrics.get("Cash Flow", 0),  # Default to 0 if not found
                "Break-Even Rent ($)": metrics.get("Break-Even Rent", None),
                "Cash-on-Cash ROI (%)": metrics.get("Cash on Cash", 0),  # Renamed to match calculation
            })

    return pd.DataFrame(results)


# Metrics Calculation Function
def calculate_metrics(financial_details):
    """
    Calculate key financial metrics based on provided financial details.
    """
    price = financial_details["property_price"]
    rent = financial_details["annual_rent_income"]
    down = financial_details["down_payment"]
    closing = financial_details["closing_costs"]
    rehab = financial_details["rehab_costs"]
    taxes = financial_details["annual_property_taxes"]
    insurance = financial_details["annual_insurance"]
    utilities = financial_details["annual_utilities"]
    maintenance_perc = financial_details["maintenance_perc"]
    capex_perc = financial_details["capex_perc"]
    mgmt_perc = financial_details["mgmt_perc"]
    vacancy_perc = financial_details["vacancy_perc"]
    hoa_fees = financial_details["hoa_fees"] * 12  # Annualize
    other_income = financial_details["other_income"] * 12  # Annualize
    rate = financial_details["interest_rate"]
    term = financial_details["loan_term"]

    loan_amount = price - down
    monthly_rate = rate / 100 / 12
    num_payments = term * 12

    try:
        monthly_payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)
    except ZeroDivisionError:
        monthly_payment = 0

    annual_debt_service = monthly_payment * 12
    operating_expenses = taxes + insurance + utilities + hoa_fees + (rent * (maintenance_perc + capex_perc + mgmt_perc) / 100)
    effective_gross_income = rent * (1 - vacancy_perc / 100) + other_income
    noi = effective_gross_income - operating_expenses

    cash_flow = noi - annual_debt_service
    total_investment = down + closing + rehab

    cap_rate = (noi / price) * 100 if price > 0 else 0
    cash_on_cash = (cash_flow / total_investment) * 100 if total_investment > 0 else 0
    try:
        break_even_rent = (operating_expenses + annual_debt_service) / (1 - vacancy_perc / 100)
    except ZeroDivisionError:
        break_even_rent = 0

    return {
        "Monthly Payment": monthly_payment,
        "Annual Debt Service": annual_debt_service,
        "Operating Expenses": operating_expenses,
        "Effective Gross Income": effective_gross_income,
        "NOI": noi,
        "Cash Flow": cash_flow,
        "Cap Rate": cap_rate,
        "Cash on Cash": cash_on_cash,
        "Break-Even Rent": break_even_rent,
    }



# Main Function
def main():
    st.title("Real Estate Investment Calculator")
    st.write("Analyze your real estate investment with advanced metrics and sensitivity analysis.")

    # Sidebar for User Inputs
    st.sidebar.header("Input Parameters")
    rent_income = st.sidebar.number_input("Annual Rent Income ($)", value=30000, step=1000)
    property_price = st.sidebar.number_input("Property Price ($)", value=300000, step=10000)
    down_payment = st.sidebar.number_input("Down Payment ($)", value=60000, step=5000)
    closing_costs = st.sidebar.number_input("Closing Costs ($)", value=5000, step=500)
    rehab_costs = st.sidebar.number_input("Rehab Costs ($)", value=10000, step=1000)
    taxes = st.sidebar.number_input("Annual Property Taxes ($)", value=5000, step=500)
    insurance = st.sidebar.number_input("Annual Insurance ($)", value=1200, step=100)
    utilities = st.sidebar.number_input("Annual Utilities ($)", value=3000, step=500)
    maintenance = st.sidebar.number_input("Maintenance (% of Rent)", value=10, step=1)
    capex = st.sidebar.number_input("Capital Expenditures (% of Rent)", value=10, step=1)
    mgmt_perc = st.sidebar.number_input("Property Management (% of Rent)", value=8, step=1)
    vacancy_perc = st.sidebar.number_input("Vacancy Rate (%)", value=5, step=1)
    hoa_fees = st.sidebar.number_input("HOA Fees (Monthly $)", value=1000, step=50)
    other_income = st.sidebar.number_input("Other Income (Monthly $)", value=500, step=50)
    rate = st.sidebar.number_input("Interest Rate (%)", value=4.5, step=0.1)
    term = st.sidebar.number_input("Loan Term (Years)", value=30, step=1)
    appreciation_rate = st.sidebar.number_input("Appreciation Rate (%)", value=3, step=0.1)
    inflation_rate = st.sidebar.number_input("Inflation Rate (%)", value=2, step=0.1)

    # Perform Sensitivity Analysis
    st.subheader("Sensitivity Analysis Results")
    try:
        sensitivity_results = sensitivity_analysis(
            rent_income, property_price, down_payment, closing_costs, rehab_costs,
            taxes, insurance, utilities, maintenance, capex, mgmt_perc, vacancy_perc,
            hoa_fees, other_income, rate, term, appreciation_rate=appreciation_rate, inflation_rate=inflation_rate
        )
        st.write("The table below shows the sensitivity of key financial metrics to variations in rent income and property price.")
        st.dataframe(sensitivity_results)

    except Exception as e:
        st.error(f"An error occurred while performing the sensitivity analysis: {e}")

if __name__ == "__main__":
    main()

# Perform Sensitivity Analysis
# Example usage
rent_range = np.linspace(2000, 4000, 20)  # Example rent range
price_range = np.linspace(100000, 500000, 20)  # Example property price range

try:
    # Perform sensitivity analysis
    sensitivity_df = perform_sensitivity_analysis(
        rent_range=rent_range,
        price_range=price_range,
        down_payment=50000,
        closing_costs=5000,
        rehab_costs=10000,
        taxes=5000,
        insurance=2000,
        utilities=3000,
        maintenance=10,
        capex=10,
        mgmt_perc=8,
        vacancy_perc=5,
        hoa_fees=100,
        other_income=500,
        rate=4.5,
        term=30,
        appreciation_rate=3,
        inflation_rate=2
    )

    # Check if the resulting DataFrame is valid
    if not sensitivity_df.empty:
        # Format key columns for clarity
        sensitivity_df["Rent Income ($)"] = sensitivity_df["Rent Income ($)"].map("${:,.2f}".format)
        sensitivity_df["Property Price ($)"] = sensitivity_df["Property Price ($)"].map("${:,.2f}".format)
        sensitivity_df["Cap Rate (%)"] = sensitivity_df["Cap Rate (%)"].map("{:.2f}%".format)
        sensitivity_df["Cash Flow ($)"] = sensitivity_df["Cash Flow ($)"].map("${:,.2f}".format)
        sensitivity_df["Break-Even Rent ($)"] = sensitivity_df["Break-Even Rent ($)"].map("${:,.2f}".format)

        # Display results as a dataframe
        st.subheader("Sensitivity Analysis Results")
        st.dataframe(sensitivity_df)

        # Optional: Add a heatmap or visualization
        st.subheader("Sensitivity Analysis Visualization")
        heatmap = alt.Chart(sensitivity_df).mark_rect().encode(
            x=alt.X("Rent Income ($):N", title="Rent Income"),
            y=alt.Y("Property Price ($):N", title="Property Price"),
            color=alt.Color("Cap Rate (%):Q", title="Cap Rate (%)", scale=alt.Scale(scheme="blues")),
            tooltip=["Rent Income ($)", "Property Price ($)", "Cap Rate (%)", "Cash Flow ($)", "Break-Even Rent ($)"]
        ).properties(width=800, height=400)
        st.altair_chart(heatmap, use_container_width=True)
    else:
        st.error("The sensitivity analysis returned an empty DataFrame. Please check your input parameters.")

except Exception as e:
    st.error(f"An error occurred while performing the sensitivity analysis: {e}")






# Main application
def main():
    # Sidebar setup to gather input details
    location_details, property_details, financial_details = configure_sidebar()

    # Extract financial details and calculate metrics
    try:
        metrics = calculate_metrics(financial_details)

        # Display Metrics
        st.header("Investment Metrics")
        st.write("The key metrics for your real estate investment are calculated below:")
        for key, value in metrics.items():
            if "($)" in key or "Payment" in key or "Rent" in key:
                st.write(f"**{key}:** ${value:,.2f}")
            else:
                st.write(f"**{key}:** {value:.2f}%")

    except Exception as e:
        st.error(f"An error occurred while calculating metrics: {e}")

if __name__ == "__main__":
    main()





# Perform sensitivity analysis
try:
    # Call the sensitivity analysis function
    sensitivity_df = sensitivity_analysis(
        financial_details["annual_rent_income"], financial_details["property_price"],
        financial_details["down_payment"], financial_details["closing_costs"],
        financial_details["rehab_costs"], financial_details["annual_property_taxes"],
        financial_details["annual_insurance"], financial_details["annual_utilities"],
        financial_details["maintenance_perc"], financial_details["capex_perc"],
        financial_details["mgmt_perc"], financial_details["vacancy_perc"],
        financial_details["hoa_fees"], financial_details["other_income"],
        financial_details["interest_rate"], financial_details["loan_term"],
        appreciation_rate=financial_details.get("appreciation_rate", 3),
        inflation_rate=financial_details.get("inflation_rate", 2)
    )

    # Display sensitivity analysis results
    if not sensitivity_df.empty:
        st.header("Sensitivity Analysis")
        st.write("Explore how changes in rent and price affect key metrics.")
        st.dataframe(sensitivity_df)

        # Optional: Add a heatmap visualization for better insights
        st.subheader("Sensitivity Analysis Visualization")
        heatmap = alt.Chart(sensitivity_df).mark_rect().encode(
            x=alt.X("Rent Income ($):Q", title="Rent Income"),
            y=alt.Y("Property Price ($):Q", title="Property Price"),
            color=alt.Color("Cap Rate (%):Q", title="Cap Rate (%)", scale=alt.Scale(scheme="greens")),
            tooltip=["Rent Income ($)", "Property Price ($)", "Cap Rate (%)", "Cash Flow ($)"]
        ).properties(width=800, height=400)
        st.altair_chart(heatmap, use_container_width=True)
    else:
        st.error("No results were generated for the sensitivity analysis. Please check your inputs.")

except Exception as e:
    st.error(f"An error occurred during the sensitivity analysis: {e}")

# Run the app
if __name__ == "__main__":
    main()











@st.cache_data
def from_data_file(filename):
    url = (
        "https://raw.githubusercontent.com/streamlit/"
        "example-data/master/hello/v1/%s" % filename
    )
    return pd.read_json(url)

import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
from urllib.error import URLError


# Function to simulate data file retrieval
@st.cache_data
def from_data_file(filename):
    url = f"https://raw.githubusercontent.com/streamlit/example-data/master/hello/v1/{filename}"
    try:
        return pd.read_json(url)
    except ValueError:
        st.error(f"Error loading data from {url}. Ensure the file exists and is formatted correctly.")
        return pd.DataFrame()


# Sidebar configuration for map settings
st.sidebar.subheader("Map Layers & Settings")
user_lat = st.sidebar.number_input("Starting Latitude", value=37.76, step=0.01)
user_lon = st.sidebar.number_input("Starting Longitude", value=-122.4, step=0.01)
hex_radius = st.sidebar.slider("Hexagon Radius (meters)", min_value=100, max_value=1000, value=200, step=50)

# Define layers for visualization
try:
    ALL_LAYERS = {
        "VillaZone": pdk.Layer(
            "HexagonLayer",
            data=from_data_file("bike_rental_stats.json"),
            get_position=["lon", "lat"],
            radius=hex_radius,
            elevation_scale=4,
            elevation_range=[0, 1000],
            extruded=True,
        ),
        "Residential": pdk.Layer(
            "HexagonLayer",
            data=from_data_file("bike_rental_stats.json"),
            get_position=["lon", "lat"],
            radius=hex_radius,
            elevation_scale=4,
            elevation_range=[0, 1000],
            extruded=True,
        ),
        "Multifamily": pdk.Layer(
            "HexagonLayer",
            data=from_data_file("bike_rental_stats.json"),
            get_position=["lon", "lat"],
            radius=hex_radius,
            elevation_scale=4,
            elevation_range=[0, 1000],
            extruded=True,
        ),
        "Retail": pdk.Layer(
            "HexagonLayer",
            data=from_data_file("bike_rental_stats.json"),
            get_position=["lon", "lat"],
            radius=hex_radius,
            elevation_scale=4,
            elevation_range=[0, 1000],
            extruded=True,
        ),
        "Industrial Parks": pdk.Layer(
            "HexagonLayer",
            data=from_data_file("bike_rental_stats.json"),
            get_position=["lon", "lat"],
            radius=hex_radius,
            elevation_scale=4,
            elevation_range=[0, 1000],
            extruded=True,
        ),
        "Schools": pdk.Layer(
            "HexagonLayer",
            data=from_data_file("bike_rental_stats.json"),
            get_position=["lon", "lat"],
            radius=hex_radius,
            elevation_scale=4,
            elevation_range=[0, 1000],
            extruded=True,
        ),
        "Heatmap": pdk.Layer(
            "HeatmapLayer",
            data=from_data_file("bike_rental_stats.json"),
            get_position=["lon", "lat"],
            get_weight="investment_potential" if "investment_potential" in from_data_file("bike_rental_stats.json").columns else None,
            radius=500,
        ),
        "Bike Rentals": pdk.Layer(
            "HexagonLayer",
            data=from_data_file("bike_rental_stats.json"),
            get_position=["lon", "lat"],
            radius=hex_radius,
            elevation_scale=4,
            elevation_range=[0, 1000],
            extruded=True,
        ),
        "Bart Stop Exits": pdk.Layer(
            "ScatterplotLayer",
            data=from_data_file("bart_stop_stats.json"),
            get_position=["lon", "lat"],
            get_color=[200, 30, 0, 160],
            get_radius="[exits]" if "exits" in from_data_file("bart_stop_stats.json").columns else 100,
            radius_scale=0.05,
        ),
        "Bart Stop Names": pdk.Layer(
            "TextLayer",
            data=from_data_file("bart_stop_stats.json"),
            get_position=["lon", "lat"],
            get_text="name" if "name" in from_data_file("bart_stop_stats.json").columns else "",
            get_color=[0, 0, 0, 200],
            get_size=10,
            get_alignment_baseline="'bottom'",
        ),
        "Outbound Flow": pdk.Layer(
            "ArcLayer",
            data=from_data_file("bart_path_stats.json"),
            get_source_position=["lon", "lat"],
            get_target_position=["lon2", "lat2"],
            get_source_color=[200, 30, 0, 160],
            get_target_color=[200, 30, 0, 160],
            auto_highlight=True,
            width_scale=0.0001,
            get_width="outbound" if "outbound" in from_data_file("bart_path_stats.json").columns else 1,
            width_min_pixels=3,
            width_max_pixels=30,
        ),
    }

    # Select layers to display
    st.sidebar.subheader("Layer Visibility")
    selected_layers = [
        layer
        for layer_name, layer in ALL_LAYERS.items()
        if st.sidebar.checkbox(layer_name, True)
    ]

    if selected_layers:
        # Render the map with selected layers
        st.pydeck_chart(
            pdk.Deck(
                map_style="mapbox://styles/mapbox/streets-v11",
                initial_view_state={
                    "latitude": user_lat,
                    "longitude": user_lon,
                    "zoom": 11,
                    "pitch": 50,
                },
                layers=selected_layers,
                tooltip={"html": "<b>Location:</b> {name}<br><b>Value:</b> {value}", "style": {"color": "white"}},
            )
        )
    else:
        st.error("Please choose at least one layer above.")

except URLError as e:
    st.error(
        f"""
        **This demo requires internet access.**
        Connection error: {e.reason}
        """
    )










# Bar Chart for Key Metrics
chart = alt.Chart(comparison_df).mark_bar().encode(
    x=alt.X("Metric", sort=None, title="Metric"),
    y=alt.Y("Value", title="Value"),
    tooltip=["Metric", "Value"]
).interactive()
st.altair_chart(chart, use_container_width=True)







# Sensitivity Analysis
st.subheader("Sensitivity Analysis")
st.write("Explore how changes in key variables affect property performance.")

# Sensitivity Analysis Example Data
sensitivity_df = pd.DataFrame({
    "Interest Rate (%)": [2.5, 3.0, 3.5, 4.0, 4.5, 5.0],
    "Monthly Payment ($)": [
        calculate_metrics(property_price, annual_rent_income, annual_expenses, down_payment, rate, loan_term)[2]
        for rate in [2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
    ]
})
st.line_chart(sensitivity_df.set_index("Interest Rate (%)"))

# AI Predictions
st.subheader("AI-Powered Predictions")
st.write("Leverage AI to forecast future returns, property appreciation, and investment performance.")

# Placeholder for AI Model Integration
st.write("**Predicted 5-Year Appreciation:** 12.5%")
st.write("**Predicted Rental Growth Rate (Next 5 Years):** 4.2% per year")
st.write("**Risk Assessment Score:** Low Risk (Score: 2.1/10)")

# Generate Reports
st.subheader("Downloadable Reports")
if st.button("Generate Investment Report"):
    # Placeholder for PDF generation function
    st.success("Investment report has been generated and is ready for download!")
    # st.download_button(label="Download Report", data=report_file, file_name="Investment_Report.pdf")







# Visualization: Real Estate Price Distribution
if st.checkbox("Show Price Distribution"):
    price_data = pd.DataFrame({"Price ($)": np.random.randint(price_range[0], price_range[1], 50)})
    st.bar_chart(price_data)

# Data: Gross Real Estate GDP 
@st.cache_data
def get_UN_data():
    AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")

try:
    df = get_UN_data()
    countries = st.multiselect("Choose countries", list(df.index), ["United States of America", "Mexico", "Canada",])
    if not countries:
        st.error("Please select at least Two countries.")
    else:
        data = df.loc[countries]
        data /= 1000000.0
        st.subheader("Gross Real Estate GDP ($T)")
        st.dataframe(data.sort_index())

        # Altair chart
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(columns={"index": "year", "value": "Gross Agricultural Production ($B)"})
        chart = alt.Chart(data).mark_area(opacity=0.3).encode(
            x="year:T",
            y=alt.Y("Gross Agricultural Production ($B):Q", stack=None),
            color="Region:N",
        )
        st.altair_chart(chart, use_container_width=True)
except URLError as e:
    st.error(f"This demo requires internet access. Connection error: {e.reason}")



# Dynamic Line Chart with Progress Bar
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text(f"{i}% complete")
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

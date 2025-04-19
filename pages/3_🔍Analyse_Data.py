import streamlit as st
import pandas as pd
from scipy.stats import chi2_contingency

#Page COnfiguration
st.set_page_config(
    page_title="analysis page",
    page_icon= "🔍"
)
#CSS
st.markdown("<h1 style='color: white;'>🔍 CARRY OUT ANALYSIS HERE</h1>", unsafe_allow_html=True)


#Basic Statistics
if "data" in st.session_state:
    st.markdown("<h2 style='color: black;'>1. UNIVARIATE ANALYSIS</h2>", unsafe_allow_html=True)
    data = st.session_state.data
   
   
    non_numeric_columns = data.select_dtypes(include=["object", "string", "category"]).columns

    st.write("**Frequency Distribution**")
    what_to_analyse = {"Descriptive Statistics for Selected variables":'few_vars', "Frequency Distribution for all Variables":"all_vars"}
    to_pick1 = st.selectbox("How many variables do you want to analyse", list(what_to_analyse.keys()))
    selected_type = what_to_analyse[to_pick1]

    #Analysis for selected variables
    if what_to_analyse is not None:
        if selected_type == 'few_vars':
            selected_variables = st.multiselect('Select the variables', non_numeric_columns)
            if selected_variables:
                fewvarstable = []
                for var in selected_variables:
                    selected_vars_table = data[var].value_counts(dropna=True).reset_index()
                    selected_vars_table.columns = ["Category","Frequency"]
                    selected_vars_table["Percentage"] = ((selected_vars_table['Frequency']/selected_vars_table['Frequency'].sum())*100).round(2)
                    selected_vars_table['Variable'] = var
                    selected_vars_table = selected_vars_table[['Variable', 'Category', 'Frequency', 'Percentage']]
                    fewvarstable.append(selected_vars_table)
                    combined_few_vars_table = pd.concat(fewvarstable,ignore_index=True)
                st.dataframe(combined_few_vars_table)


    #Analysis for all variables
            elif selected_type == "all_vars":
                st.write("**Analysis for all Varaibles**")
                allvarstable = []
                for var in non_numeric_columns:
                    selected_vars_table1 = data[var].value_counts(dropna=True).reset_index()
                    selected_vars_table - selected_vars_table1
                    selected_vars_table.columns = ["Category","Frequency"]
                    selected_vars_table["Percentage"] = ((selected_vars_table['Frequency']/selected_vars_table['Frequency'].sum())*100).round(2)
                    selected_vars_table['Variable'] = var
                    selected_vars_table = selected_vars_table[['Variable', 'Category', 'Frequency', 'Percentage']]
                    allvarstable.append(selected_vars_table)
                    combined_all_vars_table = pd.concat(allvarstable,ignore_index=True)
                    


   
    st.markdown("<h2 style='color: black;'>2. BIVARIATE ANALYSIS</h2>", unsafe_allow_html=True)
    st.write("**Bivariate analysis - Two-way tables**")
    outcome_variable = st.selectbox("Select the Outome Variable", data.columns)
    explanatory_variables = st.multiselect("Select the Explanatory Variables", [col for col in data.columns if col != outcome_variable])
    bivariate_crosstabs = []
    if outcome_variable and explanatory_variables:
        for var in explanatory_variables:
            cross_tab1 = pd.crosstab( data[var],data[outcome_variable])
            cross_tab = cross_tab1
            cross_tab['Variable'] = var
            cross_tab['Category'] = cross_tab.index
            
            cross_tab = cross_tab[['Variable', 'Category'] + [col for col in cross_tab.columns if col not in ['Variable', 'Category']]]
            bivariate_crosstabs.append(cross_tab)

            
        concated = pd.concat(bivariate_crosstabs, ignore_index=True)
        st.dataframe(concated)
        





                




else:
    st.warning("No data found. Go to the upload data page and upload your excel file")

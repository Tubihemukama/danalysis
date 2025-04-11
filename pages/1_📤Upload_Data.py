import streamlit as st
import pandas as pd

# File Upload
file_upload = st.file_uploader('Choose your Excel File', type=['xlsx','xls'])

if file_upload is not None:
    # Read sheet names first
    xls = pd.ExcelFile(file_upload)
    sheet_names = xls.sheet_names

    # Let user select a sheet
    selected_sheet = st.selectbox("Select a sheet", sheet_names)

    # Load and store only the selected sheet
    if "selected_sheet" not in st.session_state or st.session_state.selected_sheet != selected_sheet:
        data = pd.read_excel(xls, sheet_name=selected_sheet)
        st.session_state.data = data
        st.session_state.selected_sheet = selected_sheet
        st.success(f"Loaded sheet: {selected_sheet}")
    else:
        data = st.session_state.data

    st.write('**Data Preview**')
    st.dataframe(data.head())

else:
    st.info("Please upload a file to get started.")

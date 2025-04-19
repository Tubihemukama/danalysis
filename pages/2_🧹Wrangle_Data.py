import streamlit as st
import pandas as pd
import numpy as np

# Page Config
st.set_page_config(page_title="Data Wrangling", page_icon="🧹")

st.title("🧹 Data Wrangling Page")

if "data" in st.session_state:
    data = st.session_state.data

    st.markdown("### 📂 1. Handle Missing Values")
    missing_cols = data.columns[data.isnull().any()]
    if len(missing_cols) > 0:
        st.write("The following columns have missing values:")
        st.write(missing_cols)

        with st.expander("🧹 Drop or Fill Missing Values"):
            drop_missing = st.checkbox("Drop rows with missing values", value=False)
            fill_missing = st.checkbox("Fill missing values with a value (e.g., 0, mean)", value=False)

            if drop_missing:
                data = data.dropna()
                st.write("Missing values dropped.")
            elif fill_missing:
                fill_value = st.selectbox("Select filling strategy", ["0", "Mean", "Median"])
                if fill_value == "0":
                    data = data.fillna(0)
                elif fill_value == "Mean":
                    data = data.fillna(data.mean())
                elif fill_value == "Median":
                    data = data.fillna(data.median())
                st.write(f"Missing values filled with {fill_value}.")
            
            st.write("Preview after missing value handling:")
            st.dataframe(data.head())

    else:
        st.write("No missing values detected in the dataset!")

    st.markdown("### 📋 2. Rename Columns")
    columns_to_rename = st.multiselect("Select columns to rename", data.columns)
    if columns_to_rename:
        new_names = {}
        for col in columns_to_rename:
            new_name = st.text_input(f"New name for column '{col}'", value=col)
            if new_name != col:
                new_names[col] = new_name

        if new_names:
            data.rename(columns=new_names, inplace=True)
            st.write("Columns renamed.")
            st.dataframe(data.head())

    st.markdown("### 🔄 3. Convert Data Types")
    st.write("Convert columns to appropriate data types.")
    cols_to_convert = st.multiselect("Select columns to convert", data.columns)
    if cols_to_convert:
        conversion_type = st.selectbox("Select conversion type", ["string", "category", "numeric"])
        for col in cols_to_convert:
            if conversion_type == "string":
                data[col] = data[col].astype(str)
            elif conversion_type == "category":
                data[col] = data[col].astype("category")
            elif conversion_type == "numeric":
                data[col] = pd.to_numeric(data[col], errors='coerce')

        st.write(f"Columns converted to {conversion_type}.")
        st.dataframe(data.head())

    st.markdown("### 🔎 4. Filter Rows Based on Conditions")
    st.write("Filter rows based on specific conditions.")
    filter_column = st.selectbox("Select column to filter by", data.columns)
    filter_operator = st.selectbox("Select filter operator", ["==", ">", "<", ">=", "<=", "!="])
    filter_value = st.text_input("Enter filter value")

    if filter_value:
        try:
            filter_value = float(filter_value)
        except ValueError:
            pass  # Keep as string if it's not a number

        if filter_operator == "==":
            data = data[data[filter_column] == filter_value]
        elif filter_operator == ">":
            data = data[data[filter_column] > filter_value]
        elif filter_operator == "<":
            data = data[data[filter_column] < filter_value]
        elif filter_operator == ">=":
            data = data[data[filter_column] >= filter_value]
        elif filter_operator == "<=":
            data = data[data[filter_column] <= filter_value]
        elif filter_operator == "!=":
            data = data[data[filter_column] != filter_value]

        st.write(f"Filtered rows where {filter_column} {filter_operator} {filter_value}.")
        st.dataframe(data.head())

    st.markdown("### 💾 5. Download Cleaned Data")
    st.write("Download the cleaned dataset.")
    if st.button("Download Cleaned Data"):
        cleaned_file = data.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=cleaned_file,
            file_name="cleaned_data.csv",
            mime="text/csv"
        )

else:
    st.warning("No data found. Go to the upload data page and upload your excel file.")

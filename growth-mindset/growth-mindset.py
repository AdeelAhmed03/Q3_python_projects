import streamlit as st
import PyPDF2
from docx import Document
import pandas as pd
from PIL import Image
import os
import tempfile
import matplotlib.pyplot as plt
import plotly.express as px

# Function to convert PDF to Word
def pdf_to_word(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    doc = Document()
    for page in pdf_reader.pages:
        doc.add_paragraph(page.extract_text())
    return doc

# Function to convert Excel to CSV
def excel_to_csv(excel_file):
    df = pd.read_excel(excel_file)
    return df.to_csv(index=False)

# Function to convert image formats
def convert_image(image_file, target_format):
    img = Image.open(image_file)
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{target_format}") as tmp_file:
        img.save(tmp_file.name, format=target_format.upper())
        return tmp_file.name

# Function to visualize data
def visualize_data(df):
    st.subheader("Data Visualization")
    
    # Plot histogram for numerical columns
    numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns
    if len(numerical_columns) > 0:
        selected_column = st.selectbox("Select a column for histogram", numerical_columns)
        fig = px.histogram(df, x=selected_column, title=f"Histogram of {selected_column}")
        st.plotly_chart(fig)
    
    # Plot bar chart for categorical columns
    categorical_columns = df.select_dtypes(include=["object"]).columns
    if len(categorical_columns) > 0:
        selected_column = st.selectbox("Select a column for bar chart", categorical_columns)
        fig = px.bar(df[selected_column].value_counts(), title=f"Bar Chart of {selected_column}")
        st.plotly_chart(fig)

# Function to clean data
def clean_data(df):
    st.subheader("Data Cleaning")
    
    # Remove duplicates
    if st.checkbox("Remove duplicates"):
        df = df.drop_duplicates()
        st.write("Duplicates removed!")
    
    # Fill missing values
    if st.checkbox("Fill missing values"):
        numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns
        categorical_columns = df.select_dtypes(include=["object"]).columns
        
        for col in numerical_columns:
            df[col].fillna(df[col].mean(), inplace=True)
        for col in categorical_columns:
            df[col].fillna(df[col].mode()[0], inplace=True)
        st.write("Missing values filled!")
    
    return df

# Streamlit App
st.title("File Converter and Data Cleaning Web App")
st.write("Upload a file, convert it, and perform data cleaning and visualization.")

# File uploader
uploaded_file = st.file_uploader("Upload a file", type=["pdf", "xlsx", "csv", "jpg", "png", "jpeg"])

# Target format selection
if uploaded_file:
    file_type = uploaded_file.type.split("/")[-1]
    st.write(f"Uploaded file type: {file_type}")

    if file_type == "pdf":
        target_format = st.selectbox("Select target format", ["docx"])
    elif file_type in ["xlsx", "csv"]:
        target_format = st.selectbox("Select target format", ["csv"])
    elif file_type in ["jpg", "png", "jpeg"]:
        target_format = st.selectbox("Select target format", ["png", "jpg", "jpeg"])
    else:
        st.error("Unsupported file format!")

    # Convert and download
    if st.button("Convert"):
        with st.spinner("Converting..."):
            try:
                if file_type == "pdf" and target_format == "docx":
                    doc = pdf_to_word(uploaded_file)
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_file:
                        doc.save(tmp_file.name)
                        st.success("Conversion successful!")
                        st.download_button("Download Word File", tmp_file.name, file_name="converted.docx")
                elif file_type == "xlsx" and target_format == "csv":
                    csv_data = excel_to_csv(uploaded_file)
                    st.success("Conversion successful!")
                    st.download_button("Download CSV File", csv_data, file_name="converted.csv")
                elif file_type in ["jpg", "png", "jpeg"] and target_format in ["png", "jpg", "jpeg"]:
                    converted_image_path = convert_image(uploaded_file, target_format)
                    st.success("Conversion successful!")
                    st.download_button(f"Download {target_format.upper()} File", open(converted_image_path, "rb"), file_name=f"converted.{target_format}")
                else:
                    st.error("Unsupported conversion!")
            except Exception as e:
                st.error(f"An error occurred: {e}")

    # Data cleaning and visualization for CSV/Excel files
    if file_type in ["xlsx", "csv"]:
        df = pd.read_excel(uploaded_file) if file_type == "xlsx" else pd.read_csv(uploaded_file)
        st.subheader("Uploaded Data")
        st.write(df)

        # Data cleaning
        df = clean_data(df)
        st.subheader("Cleaned Data")
        st.write(df)

        # Data visualization
        visualize_data(df)
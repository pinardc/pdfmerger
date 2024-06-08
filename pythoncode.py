import streamlit as st
from PyPDF2 import PdfMerger
import io

# Function to merge PDFs
def merge_pdfs(pdf_list):
    merger = PdfMerger()
    for pdf in pdf_list:
        # Make sure to use `BytesIO` for reading the file
        merger.append(io.BytesIO(pdf.getbuffer()))
    merged_pdf = io.BytesIO()
    merger.write(merged_pdf)
    merged_pdf.seek(0)
    return merged_pdf

# Streamlit interface

# Add the logo to the app
logo_path = "Ani.ML_C_hrzHealth.png"  # Update this path if the logo is in a different directory
st.image(logo_path, width=400)

# Title
st.title("PDF Merger Utility")


# File uploader
uploaded_files = st.file_uploader("Upload PDF files", accept_multiple_files=True, type='pdf')

# Merge button
if st.button("Merge PDFs"):
    if uploaded_files:
        # Call the merge_pdfs function and pass the uploaded files
        merged_pdf = merge_pdfs(uploaded_files)
        # Create a download button for the merged PDF
        st.download_button(label="Download Merged PDF",
                           data=merged_pdf,
                           file_name="merged.pdf",
                           mime="application/pdf")
    else:
        st.error("Please upload some PDF files to merge")


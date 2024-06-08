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

# Function to add a logo
def add_logo():
    st.markdown(
        """
        <style>
            .logo-container {
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 10px 0;
            }
            .logo-container img {
                max-width: 150px;  # Adjust the max-width to make the logo smaller
                height: auto;
            }
        </style>
        <div class="logo-container">
            <img src="logo.png" alt="Logo">
        </div>
        """,
        unsafe_allow_html=True,
    )

# Add the logo to the app
add_logo()

# Streamlit interface
st.title("ANI.ML Health Inc. PDF Merger")


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

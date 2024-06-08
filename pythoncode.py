# Install the required packages
pip install streamlit pyngrok pypdf2

# Write the Streamlit app to a file
%%writefile streamlit_app.py
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
st.title("ANI.ML Health Inc. PDF Merger")

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: /content/Untitled.jpg;
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "My Company Name";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


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

# Run Streamlit App
!streamlit run /content/streamlit_app.py &>/content/logs.txt &



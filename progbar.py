import streamlit as st 
import requests

progress_text = st.empty()
progress_bar = st.progress(0)
def download_file(url, filename):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    with open(filename, "wb") as f:
        downloaded = 0
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)
                percent = int(downloaded * 100 / total_size) if total_size else 0
                # Update the progress text and progress bar
                progress_text.subheader(f'Progress:{percent}%')
                progress_bar.progress(percent)
    return filename
download_file('file url', 'output.file')
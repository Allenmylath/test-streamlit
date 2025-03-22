import streamlit as st
import streamlit.components.v1 as components
import re

# Simple page config with fewer parameters
st.set_page_config(
    page_title="Web Page Embedder",
    layout="wide"
)

# App title and description
st.title("Interactive Web Page Embedder")
st.markdown("This app allows you to embed and interact with external web pages.")

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    
    # URL input
    default_url = "https://streamlit.io/"
    url = st.text_input("Enter website URL:", value=default_url)
    
    # Height configuration
    height = st.slider("Frame height (pixels):", min_value=400, max_value=1000, value=600, step=50)
    
    # Width configuration
    full_width = st.checkbox("Full width", value=True)
    if not full_width:
        width = st.slider("Frame width (pixels):", min_value=400, max_value=1200, value=800, step=50)
    else:
        width = None

# URL validation
def is_valid_url(url):
    regex = re.compile(
        r'^(?:http|https)://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

# Main content area
if is_valid_url(url):
    st.markdown(f"### Currently embedding: [{url}]({url})")
    
    # Embed the webpage using components.html
    components.html(
        f"""
        <iframe 
            src="{url}" 
            width="{width if width else '100%'}" 
            height="{height}px" 
            style="border:none;" 
            scrolling="yes"
            allow="accelerometer; autoplay; camera; encrypted-media; geolocation; gyroscope; microphone; midi; payment; usb; xr-spatial-tracking"
            allowfullscreen="true"
            sandbox="allow-forms allow-modals allow-pointer-lock allow-popups allow-presentation allow-same-origin allow-scripts"
        ></iframe>
        """,
        height=height,
        width=width,
    )
else:
    if url != "":
        st.error("Please enter a valid URL (must start with http:// or https://).")
    else:
        st.info("Enter a URL in the sidebar to begin.")

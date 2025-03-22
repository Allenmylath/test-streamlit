import streamlit as st
import streamlit.components.v1 as components
import re

# Set page config
st.set_page_config(
    page_title="Web Page Embedder",
    page_title_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
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
    
    # Scroll behavior
    scrolling = st.checkbox("Enable scrolling", value=True)
    
    # Refresh button
    if st.button("Refresh Frame"):
        st.rerun()
    
    st.divider()
    st.markdown("⚠️ **Note:** Some websites may block embedding through their security policies (X-Frame-Options).")

# URL validation
def is_valid_url(url):
    regex = re.compile(
        r'^(?:http|https)://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # or IP
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

# Main content area
if is_valid_url(url):
    # Create container for the embedded webpage
    web_container = st.container()
    
    with web_container:
        st.markdown(f"### Currently embedding: [{url}]({url})")
        
        # Generate HTML for the iframe with specified parameters
        iframe_width = "100%" if width is None else f"{width}px"
        iframe_scrolling = "yes" if scrolling else "no"
        
        # Embed the webpage using components.html
        components.html(
            f"""
            <iframe 
                src="{url}" 
                width="{iframe_width}" 
                height="{height}px" 
                style="border:none;" 
                scrolling="{iframe_scrolling}"
                allow="accelerometer; autoplay; camera; encrypted-media; geolocation; gyroscope; microphone; midi; payment; usb; xr-spatial-tracking"
                allowfullscreen="true"
                sandbox="allow-forms allow-modals allow-pointer-lock allow-popups allow-presentation allow-same-origin allow-scripts"
            ></iframe>
            """,
            height=height,
            width=width,
        )
        
        st.caption("If the website doesn't load, it may be blocking iframe embedding due to security policies.")
else:
    if url != "":
        st.error("Please enter a valid URL (must start with http:// or https://).")
    else:
        st.info("Enter a URL in the sidebar to begin.")

# Add error handling for specific cases
try:
    # This is just a placeholder for potential additional error handling
    pass
except Exception as e:
    st.error(f"An error occurred: {e}")
    
# Footer
st.divider()
st.markdown("**Note:** While this app attempts to embed external websites, not all websites allow embedding due to security settings (X-Frame-Options headers).")

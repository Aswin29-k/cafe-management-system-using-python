import streamlit as st

# Create a box-like container using HTML and CSS
st.markdown("""
    <style>
        .box-container {
            border: 2px solid #4CAF50;  # Green border
            padding: 20px;
            border-radius: 10px;
            background-color: #f4f4f4;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            p{
            color:black;
            }
        }
    </style>
    <div class="box-container">
        <h3>This is a box container</h3>
        <p>You can add your content inside this box!</p>
    </div>
""", unsafe_allow_html=True)






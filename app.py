import streamlit as st

# Page config
st.set_page_config(
    page_title="Ruan — Your Business Friend",
    page_icon="🤖",
    layout="centered"
)

# Header
st.markdown("""
    <h1 style='text-align:center; color:#534AB7;'>
        Ruan 🤖
    </h1>
    <h4 style='text-align:center; color:#888780;'>
        Your AI Business Friend
    </h4>
    <hr style='border: 1px solid #EEEDFE;'/>
""", unsafe_allow_html=True)

# Ruan greeting
st.markdown("""
    <div style='
        background:#EEEDFE;
        border-radius:16px;
        padding:24px;
        text-align:center;
        margin-top:32px;
    '>
        <h2>🙏 Namaste!</h2>
        <p style='font-size:18px; color:#534AB7;'>
            I am <b>Ruan</b> — your personal business analyst.
        </p>
        <p style='font-size:15px; color:#666;'>
            Upload your sales data and I will tell you
            exactly what is making you money
            and what is costing you.
        </p>
        <p style='font-size:14px; color:#888;'>
            In your language. In your city. For free.
        </p>
    </div>
""", unsafe_allow_html=True)

# Language selector
st.markdown("<br>", unsafe_allow_html=True)
lang = st.selectbox(
    "🌐 Choose your language / ಭಾಷೆ ಆಯ್ಕೆ ಮಾಡಿ / भाषा चुनें",
    ["English", "Kannada", "Hindi", "Tamil"]
)

# Business type
business = st.selectbox(
    "🏪 What is your business?",
    ["Medical Shop", "Kirana Store", "Textile Shop",
     "Shoe Showroom", "Fancy Store", "Vegetable Stall",
     "Pan Shop", "Hardware Store", "Other"]
)

# City
city = st.text_input("📍 Which city are you in?", placeholder="e.g. Mysuru, Bangalore, Chennai")

# Continue button
if st.button("Let's Go! →", use_container_width=True):
    if city:
        st.success(f"Welcome! Ruan is ready to help your {business} in {city}. 🎉")
        st.balloons()
    else:
        st.warning("Please enter your city name!")
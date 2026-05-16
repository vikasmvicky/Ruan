import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="Ruan — Your Business Friend",
    page_icon="🤖",
    layout="centered"
)

# Ruan animated character
def show_ruan(emotion="happy"):
    emotions = {
        "happy": {
            "mouth": "M304 214 Q320 228 336 214",
            "browL": "M288 170 Q300 164 312 170",
            "browR": "M328 170 Q340 164 352 170",
            "msg": "Namaste! I am Ruan 🙏"
        },
        "thinking": {
            "mouth": "M308 218 Q320 218 332 218",
            "browL": "M288 172 Q300 168 312 173",
            "browR": "M328 168 Q340 172 352 173",
            "msg": "Let me analyse your data... 🤔"
        },
        "excited": {
            "mouth": "M300 212 Q320 232 340 212",
            "browL": "M288 166 Q300 160 312 166",
            "browR": "M328 166 Q340 160 352 166",
            "msg": "I found something amazing! 🎉"
        },
        "worried": {
            "mouth": "M304 220 Q320 212 336 220",
            "browL": "M288 174 Q300 170 312 175",
            "browR": "M328 175 Q340 170 352 174",
            "msg": "Hmm, something needs attention... ⚠️"
        }
    }
    e = emotions[emotion]
    html = f"""
    <style>
    @keyframes float {{
        0%,100%{{transform:translateY(0)}}
        50%{{transform:translateY(-8px)}}
    }}
    @keyframes blink {{
        0%,90%,100%{{transform:scaleY(1)}}
        95%{{transform:scaleY(0.1)}}
    }}
    @keyframes screenflash {{
        0%,100%{{opacity:1}}
        50%{{opacity:0.6}}
    }}
    @keyframes wiggle {{
        0%,100%{{transform:rotate(-4deg)}}
        50%{{transform:rotate(4deg)}}
    }}
    .ruan-body {{ animation: float 3s ease-in-out infinite; }}
    .ruan-eyes {{ animation: blink 4s ease-in-out infinite; transform-origin: center; }}
    .screen1 {{ animation: screenflash 2s ease-in-out infinite; }}
    .screen2 {{ animation: screenflash 2.5s ease-in-out infinite; }}
    .screen3 {{ animation: screenflash 1.8s ease-in-out infinite; }}
    .owl {{ animation: wiggle 3s ease-in-out infinite; transform-origin: 520px 260px; }}
    .ruan-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        background: #F5F4FD;
        border-radius: 24px;
        padding: 16px;
        margin-bottom: 16px;
    }}
    .ruan-msg {{
        background: #EEEDFE;
        border-radius: 16px;
        padding: 12px 24px;
        color: #3C3489;
        font-size: 16px;
        font-weight: 500;
        margin-top: 8px;
        font-family: Arial, sans-serif;
        text-align: center;
    }}
    </style>

    <div class="ruan-container">
    <svg width="480" viewBox="0 0 680 420">

    <g class="ruan-body">
      <!-- Body -->
      <rect x="278" y="230" width="84" height="90" rx="20" fill="#FAC775"/>
      <rect x="278" y="248" width="84" height="8" rx="2" fill="#534AB7" opacity="0.3"/>
      <rect x="278" y="264" width="84" height="8" rx="2" fill="#534AB7" opacity="0.3"/>
      <!-- Neck -->
      <rect x="307" y="215" width="26" height="22" rx="8" fill="#FAC775"/>
      <!-- Head -->
      <ellipse cx="320" cy="185" rx="52" ry="50" fill="#FAC775"/>
      <!-- Hair -->
      <ellipse cx="320" cy="142" rx="50" ry="22" fill="#2C2C2A"/>
      <ellipse cx="278" cy="162" rx="14" ry="20" fill="#2C2C2A"/>
      <ellipse cx="362" cy="162" rx="14" ry="20" fill="#2C2C2A"/>
      <!-- Ears -->
      <ellipse cx="269" cy="188" rx="10" ry="12" fill="#FAC775"/>
      <ellipse cx="371" cy="188" rx="10" ry="12" fill="#FAC775"/>
      <!-- Eyes -->
      <g class="ruan-eyes">
        <ellipse cx="300" cy="185" rx="13" ry="14" fill="white"/>
        <ellipse cx="302" cy="186" rx="8" ry="9" fill="#2C2C2A"/>
        <ellipse cx="304" cy="183" rx="3" ry="3" fill="white"/>
        <ellipse cx="340" cy="185" rx="13" ry="14" fill="white"/>
        <ellipse cx="342" cy="186" rx="8" ry="9" fill="#2C2C2A"/>
        <ellipse cx="344" cy="183" rx="3" ry="3" fill="white"/>
      </g>
      <!-- Eyebrows -->
      <path d="{e['browL']}" fill="none" stroke="#2C2C2A" stroke-width="3" stroke-linecap="round"/>
      <path d="{e['browR']}" fill="none" stroke="#2C2C2A" stroke-width="3" stroke-linecap="round"/>
      <!-- Nose -->
      <ellipse cx="320" cy="200" rx="5" ry="4" fill="#EF9F27" opacity="0.5"/>
      <!-- Mouth -->
      <path d="{e['mouth']}" fill="none" stroke="#2C2C2A" stroke-width="3" stroke-linecap="round"/>
      <!-- Cheeks -->
      <ellipse cx="283" cy="207" rx="12" ry="8" fill="#F0997B" opacity="0.4"/>
      <ellipse cx="357" cy="207" rx="12" ry="8" fill="#F0997B" opacity="0.4"/>
      <!-- Arms -->
      <rect x="234" y="235" width="48" height="18" rx="9" fill="#FAC775" transform="rotate(20 258 244)"/>
      <rect x="358" y="235" width="48" height="18" rx="9" fill="#FAC775" transform="rotate(-20 382 244)"/>
      <!-- Legs -->
      <rect x="288" y="315" width="26" height="50" rx="12" fill="#534AB7"/>
      <rect x="326" y="315" width="26" height="50" rx="12" fill="#534AB7"/>
      <ellipse cx="301" cy="364" rx="18" ry="10" fill="#2C2C2A"/>
      <ellipse cx="339" cy="364" rx="18" ry="10" fill="#2C2C2A"/>

      <!-- Data screen 1 -->
      <g class="screen1">
        <rect x="148" y="160" width="80" height="56" rx="6" fill="#E6F1FB" stroke="#378ADD" stroke-width="1"/>
        <rect x="154" y="168" width="28" height="4" rx="2" fill="#378ADD" opacity="0.6"/>
        <rect x="154" y="200" width="8" height="10" rx="1" fill="#534AB7"/>
        <rect x="165" y="194" width="8" height="16" rx="1" fill="#1D9E75"/>
        <rect x="176" y="197" width="8" height="13" rx="1" fill="#BA7517"/>
        <rect x="187" y="190" width="8" height="20" rx="1" fill="#534AB7"/>
      </g>

      <!-- Data screen 2 -->
      <g class="screen2">
        <rect x="270" y="68" width="100" height="60" rx="6" fill="#E1F5EE" stroke="#1D9E75" stroke-width="1"/>
        <polyline points="278,110 294,102 310,108 326,94 342,88 358,92" fill="none" stroke="#1D9E75" stroke-width="2" stroke-linecap="round"/>
      </g>

      <!-- Data screen 3 -->
      <g class="screen3">
        <rect x="412" y="150" width="80" height="56" rx="6" fill="#FAEEDA" stroke="#BA7517" stroke-width="1"/>
        <circle cx="452" cy="188" r="16" fill="#EF9F27"/>
        <path d="M452 188 L452 172 A16 16 0 0 1 466 196 Z" fill="#534AB7"/>
        <path d="M452 188 L466 196 A16 16 0 0 1 438 200 Z" fill="#1D9E75"/>
      </g>
    </g>

    <!-- Owly -->
    <g class="owl">
      <ellipse cx="580" cy="280" rx="28" ry="34" fill="#BA7517"/>
      <ellipse cx="580" cy="288" rx="18" ry="22" fill="#FAEEDA"/>
      <ellipse cx="580" cy="248" rx="26" ry="24" fill="#BA7517"/>
      <polygon points="566,228 570,210 576,228" fill="#854F0B"/>
      <polygon points="584,228 590,210 594,228" fill="#854F0B"/>
      <ellipse cx="571" cy="248" rx="10" ry="10" fill="white"/>
      <ellipse cx="589" cy="248" rx="10" ry="10" fill="white"/>
      <ellipse cx="572" cy="249" rx="6" ry="6" fill="#2C2C2A"/>
      <ellipse cx="590" cy="249" rx="6" ry="6" fill="#2C2C2A"/>
      <ellipse cx="573" cy="247" rx="2" ry="2" fill="white"/>
      <ellipse cx="591" cy="247" rx="2" ry="2" fill="white"/>
      <polygon points="580,256 575,263 585,263" fill="#EF9F27"/>
      <ellipse cx="552" cy="278" rx="14" ry="22" fill="#854F0B" transform="rotate(-15 552 278)"/>
      <ellipse cx="608" cy="278" rx="14" ry="22" fill="#854F0B" transform="rotate(15 608 278)"/>
    </g>

    </svg>
    <div class="ruan-msg">{e['msg']}</div>
    </div>
    """
    components.html(html, height=480)

# Main app
st.markdown("""
    <h1 style='text-align:center;color:#534AB7;font-family:Arial;'>Ruan 🤖</h1>
    <p style='text-align:center;color:#888;font-family:Arial;font-style:italic;'>
    Every big company has a data team. Every small business has a rough book.<br>
    <b style='color:#534AB7;'>Ruan closes that gap — in your language, in your city, for free.</b>
    </p>
    <hr style='border:1px solid #EEEDFE;'/>
""", unsafe_allow_html=True)

# Show Ruan based on session state
if "emotion" not in st.session_state:
    st.session_state.emotion = "happy"

show_ruan(st.session_state.emotion)

# Onboarding
st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    lang = st.selectbox(
        "🌐 Your language",
        ["English", "Kannada", "Hindi", "Tamil"]
    )

with col2:
    business = st.selectbox(
        "🏪 Your business",
        ["Medical Shop", "Kirana Store", "Textile Shop",
         "Shoe Showroom", "Fancy Store", "Vegetable Stall",
         "Pan Shop", "Hardware Store", "Other"]
    )

city = st.text_input(
    "📍 Your city",
    placeholder="e.g. Mysuru, Bangalore, Chennai"
)

if st.button("Let's Go with Ruan! →", use_container_width=True):
    if city:
        st.session_state.emotion = "excited"
        st.session_state.lang = lang
        st.session_state.business = business
        st.session_state.city = city
        st.rerun()
    else:
        st.session_state.emotion = "worried"
        st.rerun()

if "city" in st.session_state:
    st.success(f"🎉 Ruan is ready to help your "
               f"{st.session_state.business} "
               f"in {st.session_state.city}!")
    st.info("📂 Next step — upload your sales data!")
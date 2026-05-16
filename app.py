import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from core.analyst import (
    load_sales_data,
    analyse_sales,
    generate_ruan_message,
    check_profit_health,
    get_quick_wins
)

# ─── Page Config ───────────────────────────────────────────
st.set_page_config(
    page_title="Ruan — Your Business Friend",
    page_icon="🤖",
    layout="centered"
)

# ─── Custom CSS ────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #FAFAFA; }
    .stButton>button {
        background-color: #534AB7;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: 500;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #3C3489;
        color: white;
    }
    .stSelectbox>div>div {
        border-radius: 10px;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
    div[data-testid="stFileUploader"] {
        border: 2px dashed #534AB7;
        border-radius: 12px;
        padding: 16px;
    }
</style>
""", unsafe_allow_html=True)

# ─── Ruan Animated Character ───────────────────────────────
def show_ruan(emotion="happy"):
    emotions = {
        "happy": {
            "mouth": "M304 214 Q320 228 336 214",
            "browL": "M288 170 Q300 164 312 170",
            "browR": "M328 170 Q340 164 352 170",
            "msg": "Namaste! I am Ruan 🙏 Your personal business friend!",
            "color": "#EEEDFE"
        },
        "thinking": {
            "mouth": "M308 218 Q320 218 332 218",
            "browL": "M288 172 Q300 168 312 173",
            "browR": "M328 168 Q340 172 352 173",
            "msg": "Let me analyse your data... 🤔",
            "color": "#E6F1FB"
        },
        "excited": {
            "mouth": "M300 212 Q320 232 340 212",
            "browL": "M288 166 Q300 160 312 166",
            "browR": "M328 166 Q340 160 352 166",
            "msg": "I found something amazing! 🎉",
            "color": "#E1F5EE"
        },
        "worried": {
            "mouth": "M304 220 Q320 212 336 220",
            "browL": "M288 174 Q300 170 312 175",
            "browR": "M328 175 Q340 170 352 174",
            "msg": "Hmm, something needs attention... ⚠️",
            "color": "#FAEEDA"
        },
        "surprised": {
            "mouth": "M310 216 Q320 224 330 216",
            "browL": "M288 164 Q300 158 312 165",
            "browR": "M328 165 Q340 158 352 164",
            "msg": "Wow! Look at this insight! 😮",
            "color": "#E1F5EE"
        }
    }
    e = emotions.get(emotion, emotions["happy"])

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ background: transparent; }}
    @keyframes float {{
        0%,100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-8px); }}
    }}
    @keyframes blink {{
        0%,88%,100% {{ transform: scaleY(1); }}
        93% {{ transform: scaleY(0.08); }}
    }}
    @keyframes screenflash1 {{
        0%,100% {{ opacity: 1; }}
        50% {{ opacity: 0.55; }}
    }}
    @keyframes screenflash2 {{
        0%,100% {{ opacity: 1; }}
        40% {{ opacity: 0.6; }}
    }}
    @keyframes screenflash3 {{
        0%,100% {{ opacity: 1; }}
        60% {{ opacity: 0.5; }}
    }}
    @keyframes wiggle {{
        0%,100% {{ transform: rotate(-5deg); }}
        50% {{ transform: rotate(5deg); }}
    }}
    @keyframes pulse {{
        0%,100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.05); }}
    }}
    .ruan-wrap {{
        display: flex;
        flex-direction: column;
        align-items: center;
        background: linear-gradient(135deg, #F5F4FD 0%, #EEF5FF 100%);
        border-radius: 24px;
        padding: 20px 16px 16px;
        font-family: Arial, sans-serif;
        box-shadow: 0 4px 20px rgba(83,74,183,0.1);
    }}
    .ruan-body-g {{ animation: float 3s ease-in-out infinite; }}
    .ruan-eyes-g {{
        animation: blink 4s ease-in-out infinite;
        transform-origin: 320px 185px;
    }}
    .sc1 {{ animation: screenflash1 2s ease-in-out infinite; }}
    .sc2 {{ animation: screenflash2 2.5s ease-in-out infinite; }}
    .sc3 {{ animation: screenflash3 1.8s ease-in-out infinite; }}
    .owl-g {{
        animation: wiggle 3s ease-in-out infinite;
        transform-origin: 560px 270px;
    }}
    .ruan-msg {{
        background: {e['color']};
        border-radius: 16px;
        padding: 12px 24px;
        color: #3C3489;
        font-size: 15px;
        font-weight: 500;
        margin-top: 12px;
        text-align: center;
        animation: pulse 2s ease-in-out infinite;
        max-width: 480px;
    }}
    </style>
    </head>
    <body>
    <div class="ruan-wrap">
    <svg width="520" viewBox="0 0 680 420" xmlns="http://www.w3.org/2000/svg">

      <!-- ── RUAN BODY ── -->
      <g class="ruan-body-g">

        <!-- Body shirt -->
        <rect x="278" y="230" width="84" height="90" rx="20" fill="#FAC775"/>
        <rect x="278" y="248" width="84" height="8" rx="2" fill="#534AB7" opacity="0.3"/>
        <rect x="278" y="264" width="84" height="8" rx="2" fill="#534AB7" opacity="0.3"/>
        <rect x="278" y="280" width="84" height="8" rx="2" fill="#534AB7" opacity="0.2"/>

        <!-- Neck -->
        <rect x="307" y="214" width="26" height="22" rx="8" fill="#FAC775"/>

        <!-- Head -->
        <ellipse cx="320" cy="184" rx="52" ry="50" fill="#FAC775"/>

        <!-- Hair top -->
        <ellipse cx="320" cy="141" rx="50" ry="22" fill="#2C2C2A"/>
        <ellipse cx="278" cy="161" rx="15" ry="21" fill="#2C2C2A"/>
        <ellipse cx="362" cy="161" rx="15" ry="21" fill="#2C2C2A"/>
        <ellipse cx="296" cy="147" rx="19" ry="15" fill="#2C2C2A"/>
        <ellipse cx="344" cy="147" rx="19" ry="15" fill="#2C2C2A"/>

        <!-- Ears -->
        <ellipse cx="269" cy="187" rx="10" ry="12" fill="#FAC775"/>
        <ellipse cx="371" cy="187" rx="10" ry="12" fill="#FAC775"/>
        <ellipse cx="269" cy="187" rx="6" ry="8" fill="#EF9F27" opacity="0.3"/>
        <ellipse cx="371" cy="187" rx="6" ry="8" fill="#EF9F27" opacity="0.3"/>

        <!-- Eyes -->
        <g class="ruan-eyes-g">
          <ellipse cx="300" cy="184" rx="13" ry="14" fill="white"/>
          <ellipse cx="302" cy="185" rx="8" ry="9" fill="#2C2C2A"/>
          <ellipse cx="305" cy="182" rx="3" ry="3" fill="white"/>
          <ellipse cx="340" cy="184" rx="13" ry="14" fill="white"/>
          <ellipse cx="342" cy="185" rx="8" ry="9" fill="#2C2C2A"/>
          <ellipse cx="345" cy="182" rx="3" ry="3" fill="white"/>
        </g>

        <!-- Eyebrows -->
        <path d="{e['browL']}"
              fill="none" stroke="#2C2C2A"
              stroke-width="3" stroke-linecap="round"/>
        <path d="{e['browR']}"
              fill="none" stroke="#2C2C2A"
              stroke-width="3" stroke-linecap="round"/>

        <!-- Nose -->
        <ellipse cx="320" cy="200" rx="5" ry="4"
                 fill="#EF9F27" opacity="0.45"/>

        <!-- Mouth -->
        <path d="{e['mouth']}"
              fill="none" stroke="#2C2C2A"
              stroke-width="3" stroke-linecap="round"/>

        <!-- Cheeks -->
        <ellipse cx="282" cy="206" rx="12" ry="8"
                 fill="#F0997B" opacity="0.4"/>
        <ellipse cx="358" cy="206" rx="12" ry="8"
                 fill="#F0997B" opacity="0.4"/>

        <!-- Arms -->
        <rect x="232" y="234" width="50" height="18" rx="9"
              fill="#FAC775" transform="rotate(20 257 243)"/>
        <rect x="358" y="234" width="50" height="18" rx="9"
              fill="#FAC775" transform="rotate(-20 383 243)"/>

        <!-- Hands -->
        <circle cx="224" cy="256" r="10" fill="#FAC775"/>
        <circle cx="416" cy="256" r="10" fill="#FAC775"/>

        <!-- Legs -->
        <rect x="288" y="314" width="26" height="52" rx="12" fill="#534AB7"/>
        <rect x="326" y="314" width="26" height="52" rx="12" fill="#534AB7"/>

        <!-- Shoes -->
        <ellipse cx="301" cy="365" rx="20" ry="10" fill="#2C2C2A"/>
        <ellipse cx="339" cy="365" rx="20" ry="10" fill="#2C2C2A"/>

        <!-- ── DATA SCREENS ── -->

        <!-- Screen Left — bar chart -->
        <g class="sc1">
          <rect x="144" y="156" width="84" height="60"
                rx="8" fill="#E6F1FB"
                stroke="#378ADD" stroke-width="1.2"/>
          <rect x="150" y="164" width="30" height="4"
                rx="2" fill="#378ADD" opacity="0.6"/>
          <rect x="150" y="171" width="22" height="3"
                rx="1" fill="#378ADD" opacity="0.35"/>
          <!-- bars -->
          <rect x="152" y="202" width="8" height="10"
                rx="1" fill="#534AB7"/>
          <rect x="163" y="195" width="8" height="17"
                rx="1" fill="#1D9E75"/>
          <rect x="174" y="198" width="8" height="14"
                rx="1" fill="#BA7517"/>
          <rect x="185" y="191" width="8" height="21"
                rx="1" fill="#534AB7"/>
          <text x="186" y="154" font-size="9"
                fill="#0C447C" font-family="Arial"
                text-anchor="middle">sales</text>
          <!-- connector -->
          <line x1="228" y1="186" x2="268" y2="210"
                stroke="#7F77DD" stroke-width="1"
                stroke-dasharray="4,3" opacity="0.5"/>
        </g>

        <!-- Screen Top — trend line -->
        <g class="sc2">
          <rect x="266" y="64" width="108" height="64"
                rx="8" fill="#E1F5EE"
                stroke="#1D9E75" stroke-width="1.2"/>
          <rect x="274" y="72" width="38" height="4"
                rx="2" fill="#1D9E75" opacity="0.6"/>
          <polyline
            points="274,112 290,104 306,110 322,96 338,90 354,94"
            fill="none" stroke="#1D9E75"
            stroke-width="2" stroke-linecap="round"/>
          <text x="320" y="62" font-size="9"
                fill="#085041" font-family="Arial"
                text-anchor="middle">profit trend</text>
          <!-- connector -->
          <line x1="320" y1="128" x2="320" y2="136"
                stroke="#1D9E75" stroke-width="1"
                stroke-dasharray="4,3" opacity="0.5"/>
        </g>

        <!-- Screen Right — pie chart -->
        <g class="sc3">
          <rect x="408" y="146" width="84" height="60"
                rx="8" fill="#FAEEDA"
                stroke="#BA7517" stroke-width="1.2"/>
          <rect x="414" y="154" width="32" height="4"
                rx="2" fill="#BA7517" opacity="0.6"/>
          <circle cx="450" cy="186" r="17" fill="#EF9F27"/>
          <path d="M450 186 L450 169 A17 17 0 0 1 465 195 Z"
                fill="#534AB7"/>
          <path d="M450 186 L465 195 A17 17 0 0 1 436 200 Z"
                fill="#1D9E75"/>
          <text x="450" y="144" font-size="9"
                fill="#633806" font-family="Arial"
                text-anchor="middle">margin</text>
          <!-- connector -->
          <line x1="412" y1="176" x2="378" y2="210"
                stroke="#7F77DD" stroke-width="1"
                stroke-dasharray="4,3" opacity="0.5"/>
        </g>

        <!-- Name tag -->
        <rect x="282" y="380" width="76" height="24"
              rx="12" fill="#EEEDFE" stroke="#7F77DD" stroke-width="0.8"/>
        <text x="320" y="396" font-size="12" font-weight="bold"
              fill="#3C3489" font-family="Arial"
              text-anchor="middle">Ruan</text>

      </g><!-- end ruan-body-g -->

      <!-- ── OWLY ── -->
      <g class="owl-g">
        <!-- Body -->
        <ellipse cx="560" cy="282" rx="28" ry="34" fill="#BA7517"/>
        <!-- Belly -->
        <ellipse cx="560" cy="290" rx="18" ry="22" fill="#FAEEDA"/>
        <!-- Head -->
        <ellipse cx="560" cy="250" rx="26" ry="24" fill="#BA7517"/>
        <!-- Ear tufts -->
        <polygon points="546,230 550,211 556,230" fill="#854F0B"/>
        <polygon points="564,230 570,211 574,230" fill="#854F0B"/>
        <!-- Eyes -->
        <ellipse cx="551" cy="250" rx="10" ry="10" fill="white"/>
        <ellipse cx="569" cy="250" rx="10" ry="10" fill="white"/>
        <ellipse cx="552" cy="251" rx="6" ry="6" fill="#2C2C2A"/>
        <ellipse cx="570" cy="251" rx="6" ry="6" fill="#2C2C2A"/>
        <ellipse cx="553" cy="249" rx="2" ry="2" fill="white"/>
        <ellipse cx="571" cy="249" rx="2" ry="2" fill="white"/>
        <!-- Beak -->
        <polygon points="560,258 555,265 565,265" fill="#EF9F27"/>
        <!-- Wings -->
        <ellipse cx="532" cy="280" rx="14" ry="22"
                 fill="#854F0B" transform="rotate(-15 532 280)"/>
        <ellipse cx="588" cy="280" rx="14" ry="22"
                 fill="#854F0B" transform="rotate(15 588 280)"/>
        <!-- Feet -->
        <ellipse cx="551" cy="315" rx="10" ry="5" fill="#EF9F27"/>
        <ellipse cx="569" cy="315" rx="10" ry="5" fill="#EF9F27"/>
        <!-- Mini data screen on wing -->
        <rect x="590" y="260" width="38" height="28"
              rx="4" fill="#EEEDFE" stroke="#7F77DD" stroke-width="0.8"/>
        <rect x="594" y="265" width="15" height="2"
              rx="1" fill="#534AB7" opacity="0.6"/>
        <rect x="594" y="270" width="11" height="2"
              rx="1" fill="#534AB7" opacity="0.4"/>
        <rect x="594" y="275" width="13" height="2"
              rx="1" fill="#1D9E75" opacity="0.5"/>
        <!-- Owly label -->
        <text x="560" y="334" font-size="11"
              fill="#633806" font-family="Arial"
              text-anchor="middle">Owly</text>
      </g>

    </svg>

    <div class="ruan-msg">{e['msg']}</div>
    </div>
    </body>
    </html>
    """
    components.html(html, height=500)


# ─── Header ────────────────────────────────────────────────
st.markdown("""
    <h1 style='text-align:center;color:#534AB7;
    font-family:Arial;margin-bottom:4px;'>
        Ruan 🤖
    </h1>
    <p style='text-align:center;color:#888;
    font-family:Arial;font-size:15px;font-style:italic;'>
        Every big company has a data team.<br>
        Every small business has a rough book.<br>
        <b style='color:#534AB7;'>
        Ruan closes that gap — in your language,
        in your city, for free.
        </b>
    </p>
    <hr style='border:1px solid #EEEDFE;margin:16px 0;'/>
""", unsafe_allow_html=True)

# ─── Show Ruan ─────────────────────────────────────────────
if "emotion" not in st.session_state:
    st.session_state.emotion = "happy"

show_ruan(st.session_state.emotion)

# ─── Onboarding ────────────────────────────────────────────
if "city" not in st.session_state:
    st.markdown("### 👋 Let's get started!")

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

    if st.button("Let's Go with Ruan! →"):
        if city:
            st.session_state.emotion   = "excited"
            st.session_state.lang      = lang
            st.session_state.business  = business
            st.session_state.city      = city
            st.rerun()
        else:
            st.session_state.emotion = "worried"
            st.warning("Please enter your city name!")
            st.rerun()

# ─── Main App (after onboarding) ───────────────────────────
else:
    # Welcome banner
    st.markdown(f"""
        <div style='background:#EEEDFE;border-radius:12px;
        padding:12px 20px;margin-bottom:16px;
        display:flex;align-items:center;gap:12px;'>
            <span style='font-size:24px;'>🏪</span>
            <div>
                <p style='margin:0;font-weight:500;
                color:#3C3489;font-family:Arial;'>
                    {st.session_state.business} —
                    {st.session_state.city}
                </p>
                <p style='margin:0;font-size:13px;
                color:#534AB7;font-family:Arial;'>
                    Language: {st.session_state.lang}
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Reset button
    if st.button("🔄 Start Over"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    st.markdown("---")

    # ── Upload Section ──
    st.markdown("### 📂 Upload your sales data")
    st.caption("Supported formats: CSV, Excel (.xlsx, .xls)")

    uploaded_file = st.file_uploader(
        "Drag and drop your file here",
        type=["csv", "xlsx", "xls"],
        label_visibility="collapsed"
    )

    if uploaded_file:
        # Switch Ruan to thinking
        st.session_state.emotion = "thinking"

        with st.spinner("Ruan is reading your data..."):
            df = load_sales_data(uploaded_file)

        if df is None:
            st.session_state.emotion = "worried"
            st.error("Could not read file. Please check the format!")
            st.rerun()

        # Show raw data preview
        st.markdown("#### 📋 Your Data Preview")
        st.dataframe(df.head(10), use_container_width=True)
        st.caption(f"Total records: {len(df)} rows × {len(df.columns)} columns")

        st.markdown("---")

        # ── Run Analysis ──
        with st.spinner("Ruan is finding insights..."):
            insights = analyse_sales(df)

        if insights:
            st.session_state.emotion = "excited"
             

            # ── Health Check ──
            health = check_profit_health(
                insights.get('total_profit', 0),
                st.session_state.business,
                st.session_state.city,
                insights.get('profit_margin', 0)
            )

            st.markdown("### 🏥 Business Health Check")
            st.markdown(f"""
                <div style='background:{health["color"]};
                border-radius:14px;padding:18px 22px;
                margin:12px 0;'>
                    <h3 style='margin:0 0 8px;
                    font-family:Arial;'>
                        {health["emoji"]} {health["status"].title()}
                    </h3>
                    <p style='margin:0;font-size:15px;
                    font-family:Arial;color:#333;'>
                        {health["advice"]}
                    </p>
                </div>
            """, unsafe_allow_html=True)

            # ── Key Metrics ──
            st.markdown("### 📊 Key Numbers")
            m1, m2, m3, m4 = st.columns(4)
            with m1:
                st.metric(
                    "Total Revenue",
                    f"₹{insights.get('total_revenue', 0):,.0f}"
                )
            with m2:
                st.metric(
                    "Total Profit",
                    f"₹{insights.get('total_profit', 0):,.0f}"
                )
            with m3:
                st.metric(
                    "Profit Margin",
                    f"{insights.get('profit_margin', 0)}%"
                )
            with m4:
                st.metric(
                    "Loss Orders",
                    f"{insights.get('loss_orders', 0)}"
                )

            # ── Ruan's Message ──
            st.markdown("### 💬 Ruan Says")
            msg = generate_ruan_message(
                insights,
                st.session_state.business,
                st.session_state.city,
                st.session_state.lang
            )
            st.info(msg)

            # ── Owly's Wisdom ──
            st.markdown(f"""
                <div style='background:#FAEEDA;
                border-radius:14px;padding:16px 20px;
                margin:12px 0;border-left:4px solid #BA7517;'>
                    <p style='margin:0;font-size:14px;
                    font-weight:500;color:#633806;
                    font-family:Arial;'>
                        🦉 Owly says:
                    </p>
                    <p style='margin:6px 0 0;font-size:14px;
                    color:#854F0B;font-family:Arial;'>
                        Focus on your best product
                        <b>{insights.get('best_product','')}</b>
                        — it drives your highest profit.
                        Reduce stock of
                        <b>{insights.get('worst_product','')}</b>
                        — lowest returns.
                    </p>
                </div>
            """, unsafe_allow_html=True)

            # ── Quick Wins ──
            wins = get_quick_wins(insights)
            if wins:
                st.markdown("### 🎯 Ruan's Top 3 Actions")
                for i, win in enumerate(wins, 1):
                    st.markdown(f"""
                        <div style='background:#F5F4FD;
                        border-left:4px solid #534AB7;
                        border-radius:10px;
                        padding:12px 18px;margin:8px 0;
                        font-family:Arial;font-size:15px;
                        color:#333;'>
                            <b style='color:#534AB7;'>
                                {i}.
                            </b> {win}
                        </div>
                    """, unsafe_allow_html=True)

            # ── Best vs Worst ──
            st.markdown("### ⭐ Best vs Worst")
            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f"""
                    <div style='background:#E1F5EE;
                    border-radius:12px;padding:16px;
                    text-align:center;'>
                        <p style='font-size:13px;color:#085041;
                        margin:0;'>⭐ Best Product</p>
                        <p style='font-size:18px;font-weight:500;
                        color:#085041;margin:8px 0 4px;'>
                            {insights.get('best_product','N/A')}
                        </p>
                        <p style='font-size:13px;color:#1D9E75;
                        margin:0;'>
                            ₹{insights.get('best_product_profit',0):,.0f}
                        </p>
                    </div>
                """, unsafe_allow_html=True)
            with c2:
                st.markdown(f"""
                    <div style='background:#FCEBEB;
                    border-radius:12px;padding:16px;
                    text-align:center;'>
                        <p style='font-size:13px;color:#791F1F;
                        margin:0;'>⚠️ Needs Attention</p>
                        <p style='font-size:18px;font-weight:500;
                        color:#791F1F;margin:8px 0 4px;'>
                            {insights.get('worst_product','N/A')}
                        </p>
                        <p style='font-size:13px;color:#BA2222;
                        margin:0;'>
                            ₹{insights.get('worst_product_profit',0):,.0f}
                        </p>
                    </div>
                """, unsafe_allow_html=True)

            # ── Best Day ──
            if insights.get('best_day'):
                st.markdown("### 📅 Best & Worst Days")
                d1, d2 = st.columns(2)
                with d1:
                    st.success(
                        f"✅ Best Day: **{insights.get('best_day','N/A')}**"
                    )
                with d2:
                    st.error(
                        f"❌ Worst Day: **{insights.get('worst_day','N/A')}**"
                    )

            # ── Discount Warning ──
            if insights.get('discount_hurts'):
                st.markdown("### 🏷️ Discount Alert")
                st.warning(f"""
                    ⚠️ Your heavy discounts are hurting profits!

                    High discount orders:
                    ₹{insights.get('high_discount_profit',0):,.2f} avg profit

                    Low discount orders:
                    ₹{insights.get('low_discount_profit',0):,.2f} avg profit

                    Reduce discounts above 20% immediately!
                """)

        else:
            st.session_state.emotion = "worried"
            st.warning(
                "Could not find enough data to analyse. "
                "Please check your file has Sales and Profit columns."
            )
            st.rerun()

    # ── Footer ──
    st.markdown("---")
    st.markdown("""
        <p style='text-align:center;font-size:12px;
        color:#aaa;font-family:Arial;'>
            Ruan 🤖 — Built for India's small businesses<br>
            Your data never leaves your device. 100% private. 100% free.
        </p>
    """, unsafe_allow_html=True)
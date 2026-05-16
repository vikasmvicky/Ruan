import streamlit as st
import pandas as pd
from ui.ruan import show_ruan_cinematic, show_ruan_storytelling
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

# ─── Session State Init ─────────────────────────────────────
if "emotion" not in st.session_state:
    st.session_state.emotion = "happy"
if "messages" not in st.session_state:
    st.session_state.messages = []
if "insights" not in st.session_state:
    st.session_state.insights = None

# ─── Show Ruan ─────────────────────────────────────────────
show_ruan_cinematic(
    emotion=st.session_state.emotion,
    message={
        "happy":     "Namaste! I am Ruan 🙏 Your personal business friend!",
        "thinking":  "Let me analyse your data... 🤔",
        "excited":   "I found something amazing! 🎉",
        "worried":   "Hmm, something needs attention... ⚠️",
        "surprised": "Wow! Look at this insight! 😮"
    }.get(st.session_state.emotion, "Namaste! 🙏"),
    owly_message={
        "happy":     "Upload your data and let's find insights!",
        "thinking":  "Reading every row carefully...",
        "excited":   "Great numbers! Let me explain...",
        "worried":   "Don't worry — we will fix this together!",
        "surprised": "This is very interesting data!"
    }.get(st.session_state.emotion, "")
)

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

# ─── Main App ───────────────────────────────────────────────
else:
    # ── Welcome banner ──
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

    # ── Reset button ──
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
        st.session_state.emotion = "thinking"

        with st.spinner("Ruan is reading your data..."):
            df = load_sales_data(uploaded_file)

        if df is None:
            st.session_state.emotion = "worried"
            st.error(
                "Could not read file. "
                "Please check the format and try again!"
            )
            st.stop()

        # ── Data Preview ──
        st.markdown("#### 📋 Your Data Preview")
        st.dataframe(
            df.head(10).reset_index(drop=True),
            use_container_width=True
        )
        st.caption(
            f"Total records: "
            f"{len(df):,} rows × {len(df.columns)} columns"
        )

        st.markdown("---")

        # ── Run Analysis ──
        with st.spinner("Ruan is finding insights..."):
            insights = analyse_sales(df)
            st.session_state.insights = insights

        if not insights:
            st.session_state.emotion = "worried"
            st.warning(
                "Could not find enough data to analyse. "
                "Please check your file has Sales "
                "and Profit columns."
            )
            st.stop()

        # ── Cinematic Storytelling ──
        st.markdown("### 🎬 Ruan's Story")
        show_ruan_storytelling(
            insights,
            st.session_state.business,
            st.session_state.city
        )

        st.session_state.emotion = "excited"

        st.markdown("---")

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
                <h3 style='margin:0 0 8px;font-family:Arial;'>
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
                f"₹{insights.get('total_revenue',0):,.0f}"
            )
        with m2:
            st.metric(
                "Total Profit",
                f"₹{insights.get('total_profit',0):,.0f}"
            )
        with m3:
            st.metric(
                "Profit Margin",
                f"{insights.get('profit_margin',0)}%"
            )
        with m4:
            st.metric(
                "Loss Orders",
                f"{insights.get('loss_orders',0)}"
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
            margin:12px 0;
            border-left:4px solid #BA7517;'>
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
                        <b style='color:#534AB7;'>{i}.</b>
                        {win}
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
                    <p style='font-size:13px;color:#1D9E75;margin:0;'>
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
                    <p style='font-size:13px;color:#BA2222;margin:0;'>
                        ₹{insights.get('worst_product_profit',0):,.0f}
                    </p>
                </div>
            """, unsafe_allow_html=True)

        # ── Best & Worst Days ──
        if insights.get('best_day'):
            st.markdown("### 📅 Best & Worst Days")
            d1, d2 = st.columns(2)
            with d1:
                st.success(
                    f"✅ Best Day: "
                    f"**{insights.get('best_day','N/A')}**"
                )
            with d2:
                st.error(
                    f"❌ Worst Day: "
                    f"**{insights.get('worst_day','N/A')}**"
                )

        # ── Discount Warning ──
        if insights.get('discount_hurts'):
            st.markdown("### 🏷️ Discount Alert")
            st.warning(f"""
                ⚠️ Your heavy discounts are hurting profits!

                High discount orders:
                ₹{insights.get('high_discount_profit',0):,.2f}
                avg profit

                Low discount orders:
                ₹{insights.get('low_discount_profit',0):,.2f}
                avg profit

                Reduce discounts above 20% immediately!
            """)

        # ── Chat with Ruan ──
        st.markdown("---")
        st.markdown("### 💬 Ask Ruan Anything")
        st.caption(
            "Ask about your business in plain language"
        )

        # Chat history
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f"""
                    <div style='background:#F0F0F0;
                    border-radius:12px;padding:10px 16px;
                    margin:6px 0;text-align:right;
                    font-family:Arial;font-size:14px;'>
                        👤 {msg["content"]}
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div style='background:#EEEDFE;
                    border-radius:12px;padding:10px 16px;
                    margin:6px 0;font-family:Arial;
                    font-size:14px;color:#3C3489;'>
                        🤖 {msg["content"]}
                    </div>
                """, unsafe_allow_html=True)

        # ── Question Input ──
        question = st.text_input(
            "Ask Ruan",
            placeholder="e.g. Why am I losing money? "
                        "What should I order this week?",
            label_visibility="collapsed"
        )

        if st.button("Ask Ruan! 🤖", use_container_width=True):
            if question:
                st.session_state.messages.append({
                    "role": "user",
                    "content": question
                })
                with st.spinner("Ruan is thinking... 🤔"):
                    from core.llm import ask_ruan
                    response = ask_ruan(
                        question=question,
                        business=st.session_state.business,
                        city=st.session_state.city,
                        language=st.session_state.lang,
                        insights=insights
                    )
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })
                st.session_state.emotion = "excited"
                st.rerun()
            else:
                st.warning("Please type a question first!")

    # ── Footer ──
    st.markdown("---")
    st.markdown("""
        <p style='text-align:center;font-size:12px;
        color:#aaa;font-family:Arial;'>
            Ruan 🤖 — Built for India's small businesses<br>
            Your data never leaves your device.
            100% private. 100% free.
        </p>
    """, unsafe_allow_html=True)
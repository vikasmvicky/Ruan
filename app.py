import streamlit as st
import pandas as pd
from ui.ruan import show_ruan_cinematic, show_ruan_storytelling
from ui.styles import get_dark_theme
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
    layout="wide"
)

# ─── Apply Dark Theme ──────────────────────────────────────
st.markdown(get_dark_theme(), unsafe_allow_html=True)

# ─── Navigation ────────────────────────────────────────────
st.markdown("""
<div class="ruan-nav">
    <div class="nav-logo">Ruan<span>.</span></div>
    <div class="nav-links">
        <a class="nav-link" href="#">Home</a>
        <a class="nav-link" href="#">Analysis</a>
        <a class="nav-link" href="#">About</a>
    </div>
    <div class="badge">Free Forever</div>
</div>
""", unsafe_allow_html=True)

# ─── Session State ─────────────────────────────────────────
if "emotion" not in st.session_state:
    st.session_state.emotion = "happy"
if "messages" not in st.session_state:
    st.session_state.messages = []
if "insights" not in st.session_state:
    st.session_state.insights = None

# ─── Hero Section ──────────────────────────────────────────
if "city" not in st.session_state:
    st.markdown("""
    <div class="hero-section">
        <div class="badge" style="margin-bottom:24px;">
            🇮🇳 Built for India's 63M Small Businesses
        </div>
        <h1 class="hero-headline">
            Ruan Knows<br>
            <span class="highlight">Your Business</span>
        </h1>
        <p class="hero-sub">
            Every big company has a data team.
            Every small business has a rough book.
            Ruan closes that gap — in your language,
            in your city, for free.
        </p>
        <div class="stats-bar">
            <div class="stat-item">
                <div class="stat-number">63M+</div>
                <div class="stat-label">Small Businesses</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">₹0</div>
                <div class="stat-label">Forever Free</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">4</div>
                <div class="stat-label">Indian Languages</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">100%</div>
                <div class="stat-label">Private & Offline</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Ruan character ──
    st.markdown("<br><br>", unsafe_allow_html=True)
    show_ruan_cinematic(
        emotion="happy",
        message="Namaste! I am Ruan 🙏 Your personal business friend!",
        owly_message="Upload your data and let's find insights!"
    )

    # ── Features section ──
    st.markdown("""
    <div class="features-section">
        <p class="section-label">Why Ruan</p>
        <h2 class="section-title">
            Built for how Indian<br>businesses actually work
        </h2>
        <div class="cards-grid">
            <div class="feature-card">
                <div class="card-icon">📷</div>
                <div class="card-title">Photo your rough book</div>
                <div class="card-desc">
                    No CSV needed. Just take a photo of your
                    register. Ruan reads it automatically.
                </div>
            </div>
            <div class="feature-card">
                <div class="card-icon">🗣️</div>
                <div class="card-title">Speak in your language</div>
                <div class="card-desc">
                    Kannada, Hindi, Tamil, English.
                    Ruan understands and responds
                    in your language.
                </div>
            </div>
            <div class="feature-card">
                <div class="card-icon">🏙️</div>
                <div class="card-title">Knows your city</div>
                <div class="card-desc">
                    ₹20,000 profit in Mysuru ≠ Bangalore.
                    Ruan understands local economics
                    automatically.
                </div>
            </div>
            <div class="feature-card">
                <div class="card-icon">🧠</div>
                <div class="card-title">Remembers everything</div>
                <div class="card-desc">
                    Ask about last month. Last week.
                    Ruan remembers your entire
                    business history.
                </div>
            </div>
            <div class="feature-card">
                <div class="card-icon">🔒</div>
                <div class="card-title">100% private</div>
                <div class="card-desc">
                    Your data never leaves your device.
                    No cloud. No server.
                    No one can read your numbers.
                </div>
            </div>
            <div class="feature-card">
                <div class="card-icon">💰</div>
                <div class="card-title">Forever free</div>
                <div class="card-desc">
                    Not a trial. Not freemium.
                    Permanently free for every
                    small business in India.
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Onboarding ──
    st.markdown("""
    <div style='max-width:600px;margin:60px auto 0;padding:0 20px;'>
        <p class="section-label" style='text-align:center;'>
            Get Started
        </p>
        <h2 class="section-title">
            Tell Ruan about<br>your business
        </h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        lang = st.selectbox(
            "🌐 Your language",
            ["English", "Kannada", "Hindi", "Tamil"]
        )
        business = st.selectbox(
            "🏪 Your business type",
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
                st.warning("Please enter your city!")
                st.rerun()

# ─── Analysis Page ─────────────────────────────────────────
else:
    st.markdown("<div style='padding-top:80px;'></div>",
                unsafe_allow_html=True)

    # ── Top bar ──
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.markdown(f"""
            <div style='display:flex;align-items:center;
            gap:12px;margin-bottom:8px;'>
                <span style='font-size:20px;'>🏪</span>
                <div>
                    <p style='margin:0;font-weight:700;
                    font-size:18px;color:#FFFFFF;'>
                        {st.session_state.business}
                    </p>
                    <p style='margin:0;font-size:13px;
                    color:rgba(255,255,255,0.4);'>
                        📍 {st.session_state.city} •
                        🌐 {st.session_state.lang}
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        if st.button("← Start Over"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── Ruan character ──
    show_ruan_cinematic(
        emotion=st.session_state.emotion,
        message={
            "happy":     "Namaste! Upload your data "
                         "and I'll find insights! 🙏",
            "thinking":  "Let me analyse your data... 🤔",
            "excited":   "I found something amazing! 🎉",
            "worried":   "Something needs attention... ⚠️",
            "surprised": "Wow! Look at this! 😮"
        }.get(st.session_state.emotion, "Namaste! 🙏"),
        owly_message={
            "happy":     "Upload your file — "
                         "CSV or Excel both work!",
            "thinking":  "Reading every row carefully...",
            "excited":   "Great numbers! Let me explain...",
            "worried":   "Don't worry — we will fix this!",
            "surprised": "This is very interesting data!"
        }.get(st.session_state.emotion, "")
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Upload ──
    st.markdown("""
        <p class='section-label'>Step 1</p>
        <h3 style='color:#FFFFFF;font-weight:700;
        margin-bottom:16px;'>Upload your sales data</h3>
    """, unsafe_allow_html=True)
    st.caption("Supported: CSV, Excel (.xlsx, .xls)")

    uploaded_file = st.file_uploader(
        "Upload",
        type=["csv", "xlsx", "xls"],
        label_visibility="collapsed"
    )

    if uploaded_file:
        st.session_state.emotion = "thinking"

        with st.spinner("Ruan is reading your data..."):
            df = load_sales_data(uploaded_file)

        if df is None:
            st.session_state.emotion = "worried"
            st.error("Could not read file. Please check format!")
            st.stop()

        st.markdown("""
            <p class='section-label'
            style='margin-top:32px;'>Your Data</p>
        """, unsafe_allow_html=True)
        st.dataframe(
            df.head(10).reset_index(drop=True),
            use_container_width=True
        )
        st.caption(
            f"✅ {len(df):,} rows × "
            f"{len(df.columns)} columns loaded"
        )

        st.markdown("<hr>", unsafe_allow_html=True)

        # ── Analysis ──
        with st.spinner("Ruan is finding insights..."):
            insights = analyse_sales(df)
            st.session_state.insights = insights

        if not insights:
            st.session_state.emotion = "worried"
            st.warning(
                "Could not analyse. Check your file has "
                "Sales and Profit columns."
            )
            st.stop()

        # ── Cinematic story ──
        st.markdown("""
            <p class='section-label'>Ruan's Story</p>
            <h3 style='color:#FFFFFF;font-weight:700;
            margin-bottom:16px;'>
                Here's what I found in your data
            </h3>
        """, unsafe_allow_html=True)

        show_ruan_storytelling(
            insights,
            st.session_state.business,
            st.session_state.city
        )

        st.session_state.emotion = "excited"
        st.markdown("<hr>", unsafe_allow_html=True)

        # ── Health Check ──
        health = check_profit_health(
            insights.get('total_profit', 0),
            st.session_state.business,
            st.session_state.city,
            insights.get('profit_margin', 0)
        )

        st.markdown(f"""
            <div class='insight-card' style='
            border-left:4px solid
            {"#1D9E75" if health["status"]=="healthy"
             else "#BA7517" if health["status"]=="warning"
             else "#791F1F"};'>
                <p style='margin:0 0 8px;font-size:20px;'>
                    {health["emoji"]}
                    <span style='font-size:16px;
                    font-weight:700;color:#FFFFFF;'>
                        Business Health —
                        {health["status"].title()}
                    </span>
                </p>
                <p style='margin:0;font-size:14px;
                color:rgba(255,255,255,0.6);'>
                    {health["advice"]}
                </p>
            </div>
        """, unsafe_allow_html=True)

        # ── Metrics ──
        st.markdown("""
            <p class='section-label'
            style='margin-top:32px;'>Key Numbers</p>
        """, unsafe_allow_html=True)

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

        # ── Ruan message ──
        st.markdown("""
            <p class='section-label'
            style='margin-top:32px;'>Ruan Says</p>
        """, unsafe_allow_html=True)
        msg = generate_ruan_message(
            insights,
            st.session_state.business,
            st.session_state.city,
            st.session_state.lang
        )
        st.info(msg)

        # ── Owly wisdom ──
        st.markdown(f"""
            <div class='insight-card'
            style='border-left:4px solid #BA7517;
            margin-top:8px;'>
                <p style='margin:0 0 6px;font-size:15px;
                font-weight:600;color:#EF9F27;'>
                    🦉 Owly's Wisdom
                </p>
                <p style='margin:0;font-size:14px;
                color:rgba(255,255,255,0.6);'>
                    Focus on
                    <b style='color:#FFFFFF;'>
                        {insights.get('best_product','')}
                    </b>
                    — your highest profit product.
                    Reduce stock of
                    <b style='color:#FFFFFF;'>
                        {insights.get('worst_product','')}
                    </b>
                    — lowest returns.
                </p>
            </div>
        """, unsafe_allow_html=True)

        # ── Quick wins ──
        wins = get_quick_wins(insights)
        if wins:
            st.markdown("""
                <p class='section-label'
                style='margin-top:32px;'>
                    Top 3 Actions
                </p>
                <h3 style='color:#FFFFFF;font-weight:700;
                margin-bottom:16px;'>
                    Ruan's recommendations for you
                </h3>
            """, unsafe_allow_html=True)
            for i, win in enumerate(wins, 1):
                st.markdown(f"""
                    <div class='insight-card'>
                        <span style='color:#7F77DD;
                        font-weight:700;'>{i}.</span>
                        <span style='color:rgba(255,255,255,0.8);
                        font-size:14px;'> {win}</span>
                    </div>
                """, unsafe_allow_html=True)

        # ── Best vs Worst ──
        st.markdown("""
            <p class='section-label'
            style='margin-top:32px;'>Performance</p>
            <h3 style='color:#FFFFFF;font-weight:700;
            margin-bottom:16px;'>Best vs Worst</h3>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"""
                <div class='insight-card'
                style='border-left:4px solid #1D9E75;
                text-align:center;'>
                    <p style='font-size:12px;color:#1D9E75;
                    margin:0;text-transform:uppercase;
                    letter-spacing:1px;'>⭐ Best Product</p>
                    <p style='font-size:20px;font-weight:700;
                    color:#FFFFFF;margin:8px 0 4px;'>
                        {insights.get('best_product','N/A')}
                    </p>
                    <p style='font-size:14px;color:#1D9E75;
                    margin:0;'>
                        ₹{insights.get(
                            'best_product_profit',0):,.0f}
                    </p>
                </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
                <div class='insight-card'
                style='border-left:4px solid #791F1F;
                text-align:center;'>
                    <p style='font-size:12px;color:#EF4444;
                    margin:0;text-transform:uppercase;
                    letter-spacing:1px;'>⚠️ Needs Attention</p>
                    <p style='font-size:20px;font-weight:700;
                    color:#FFFFFF;margin:8px 0 4px;'>
                        {insights.get('worst_product','N/A')}
                    </p>
                    <p style='font-size:14px;color:#EF4444;
                    margin:0;'>
                        ₹{insights.get(
                            'worst_product_profit',0):,.0f}
                    </p>
                </div>
            """, unsafe_allow_html=True)

        # ── Best worst days ──
        if insights.get('best_day'):
            st.markdown("""
                <p class='section-label'
                style='margin-top:32px;'>Timing</p>
            """, unsafe_allow_html=True)
            d1, d2 = st.columns(2)
            with d1:
                st.markdown(f"""
                    <div class='insight-card'
                    style='border-left:4px solid #1D9E75;
                    text-align:center;'>
                        <p style='color:#1D9E75;margin:0;
                        font-size:12px;text-transform:uppercase;
                        letter-spacing:1px;'>
                            ✅ Best Day
                        </p>
                        <p style='color:#FFFFFF;font-size:22px;
                        font-weight:700;margin:8px 0 0;'>
                            {insights.get('best_day','N/A')}
                        </p>
                    </div>
                """, unsafe_allow_html=True)
            with d2:
                st.markdown(f"""
                    <div class='insight-card'
                    style='border-left:4px solid #791F1F;
                    text-align:center;'>
                        <p style='color:#EF4444;margin:0;
                        font-size:12px;text-transform:uppercase;
                        letter-spacing:1px;'>
                            ❌ Worst Day
                        </p>
                        <p style='color:#FFFFFF;font-size:22px;
                        font-weight:700;margin:8px 0 0;'>
                            {insights.get('worst_day','N/A')}
                        </p>
                    </div>
                """, unsafe_allow_html=True)

        # ── Discount warning ──
        if insights.get('discount_hurts'):
            st.markdown("""
                <p class='section-label'
                style='margin-top:32px;'>Alert</p>
            """, unsafe_allow_html=True)
            st.warning(
                f"⚠️ Heavy discounts are hurting profits! "
                f"High discount avg: "
                f"₹{insights.get('high_discount_profit',0):,.2f} "
                f"vs Low discount avg: "
                f"₹{insights.get('low_discount_profit',0):,.2f}"
            )

        # ── Chat ──
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("""
            <p class='section-label'>Ask Ruan</p>
            <h3 style='color:#FFFFFF;font-weight:700;
            margin-bottom:8px;'>
                Ask anything about your business
            </h3>
            <p style='color:rgba(255,255,255,0.4);
            font-size:13px;margin-bottom:20px;'>
                In plain language — no technical terms needed
            </p>
        """, unsafe_allow_html=True)

        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f"""
                    <div class='chat-user'>
                        👤 {msg["content"]}
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class='chat-ruan'>
                        🤖 {msg["content"]}
                    </div>
                """, unsafe_allow_html=True)

        question = st.text_input(
            "Question",
            placeholder="e.g. Why am I losing money? "
                        "What should I stock more of?",
            label_visibility="collapsed"
        )

        if st.button("Ask Ruan! 🤖", use_container_width=True):
            if question:
                st.session_state.messages.append({
                    "role": "user",
                    "content": question
                })
                with st.spinner("Ruan is thinking... 🤔"):
                    response = (
                        "I am still getting my voice ready! "
                        "Come back soon — LLM is being "
                        "connected! 🤖"
                    )
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })
                st.session_state.emotion = "excited"
                st.rerun()
            else:
                st.warning("Please type a question!")

    # ── Footer ──
    st.markdown("""
        <div style='text-align:center;padding:60px 20px;
        border-top:1px solid rgba(255,255,255,0.06);
        margin-top:60px;'>
            <p style='font-size:22px;font-weight:800;
            color:#FFFFFF;margin:0 0 8px;'>Ruan.</p>
            <p style='font-size:13px;
            color:rgba(255,255,255,0.3);margin:0;'>
                Built for India's small businesses.
                Your data never leaves your device.
                100% private. 100% free. Forever.
            </p>
        </div>
    """, unsafe_allow_html=True)
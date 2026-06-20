import streamlit as st
import pandas as pd
from ui.theme import (
    get_nature_theme,
    get_forest_background,
    get_ruan_widget
)
from ui.ruan import show_ruan_cinematic, show_ruan_storytelling
from core.analyst import (
    load_sales_data,
    smart_analyse,
    generate_ruan_message,
    check_profit_health,
    get_quick_wins,
    handle_no_data_fallback,
    save_vendor_data,
    load_vendor_history
)
from core.llm import ask_ruan
from core.memory import (
    save_analysis_to_memory,
    save_question_to_memory,
    get_vendor_memory_summary,
    clear_vendor_memory
)
from core.charts import (
    revenue_profit_chart,
    daily_trend_chart,
    product_performance_chart,
    profit_margin_gauge,
    day_performance_chart
)
from core.data_entry import (
    ocr_to_dataframe,
    extract_sale_from_text,
    save_conversational_entry,
    get_vendor_entries_as_df,
    export_entries_to_excel
)

# ─── Page Config ───────────────────────────────────────────
st.set_page_config(
    page_title="Ruan — Your Business Friend",
    page_icon="🤖",
    layout="wide"
)

# ─── Apply Nature Theme ────────────────────────────────────
st.markdown(get_nature_theme(), unsafe_allow_html=True)

# ─── Fix input text color ──────────────────────────────────
st.markdown("""
<style>
.stTextInput > div > div > input {
    color: #000000 !important;
    background: rgba(255,255,255,0.95) !important;
    border: 1px solid rgba(74,210,149,0.3) !important;
    border-radius: 12px !important;
    caret-color: #1A1A1A !important;
}
.stTextInput > div > div > input::placeholder {
    color: rgba(0,0,0,0.4) !important;
}
.stTextInput > div > div > input:focus {
    border-color: rgba(74,210,149,0.7) !important;
    box-shadow: 0 0 0 2px rgba(74,210,149,0.15) !important;
}
.stSelectbox > div > div {
    color: #FFFFFF !important;
    background: rgba(74,210,149,0.04) !important;
    border: 1px solid rgba(74,210,149,0.15) !important;
    border-radius: 12px !important;
}
.stRadio > div {
    background: rgba(74,210,149,0.04) !important;
    border-radius: 12px !important;
    padding: 8px 12px !important;
}
.stRadio label {
    color: rgba(255,255,255,0.8) !important;
}
.stSpinner > div {
    border-top-color: #4AD295 !important;
}
.stCaption {
    color: rgba(255,255,255,0.35) !important;
}
/* Fix plotly chart background */
.js-plotly-plot {
    background: transparent !important;
}
</style>
""", unsafe_allow_html=True)

# ─── Forest Background ─────────────────────────────────────
st.markdown(get_forest_background(), unsafe_allow_html=True)

# ─── Session State ─────────────────────────────────────────
if "emotion" not in st.session_state:
    st.session_state.emotion = "happy"
if "messages" not in st.session_state:
    st.session_state.messages = []
if "insights" not in st.session_state:
    st.session_state.insights = None
if "response_style" not in st.session_state:
    st.session_state.response_style = "detailed"
if "df_loaded" not in st.session_state:
    st.session_state.df_loaded = None

# ─── Floating Ruan Widget ──────────────────────────────────
st.markdown(
    get_ruan_widget(emotion=st.session_state.emotion),
    unsafe_allow_html=True
)

# ─── Navigation ────────────────────────────────────────────
st.markdown("""
<div class="ruan-nav">
    <div class="nav-logo">Ruan<span>.</span></div>
    <div class="nav-links">
        <a class="nav-link" href="#ruan-top">Home</a>
        <a class="nav-link" href="#step-1">Analysis</a>
        <a class="nav-link"
           href="https://github.com/vikasmvicky/ruan"
           target="_blank">GitHub</a>
    </div>
    <div class="badge">Free Forever</div>
</div>
<div id="ruan-top"></div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# HERO / ONBOARDING
# ══════════════════════════════════════════════════════════
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

    # ── Features ──
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
                    Rs 20,000 profit in Mysuru is not the same
                    as Bangalore. Ruan knows your local
                    economics automatically.
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

    # ── Onboarding form ──
    st.markdown("""
    <div style='max-width:600px;margin:60px auto 0;
    padding:0 20px;position:relative;z-index:1;'>
        <p class="section-label" style='text-align:center;'>
            Get Started
        </p>
        <h2 class="section-title">
            Tell Ruan about your business
        </h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        vendor_name = st.text_input(
            "Your name",
            placeholder="e.g. Ramesh, Suresh, Priya"
        )
        lang = st.selectbox(
            "Your language",
            ["English", "Kannada", "Hindi", "Tamil"]
        )
        business = st.selectbox(
            "Your business type",
            ["Medical Shop", "Kirana Store",
             "Textile Shop", "Shoe Showroom",
             "Fancy Store", "Vegetable Stall",
             "Pan Shop", "Hardware Store", "Other"]
        )
        city = st.text_input(
            "Your city",
            placeholder="e.g. Mysuru, Bangalore, Chennai"
        )

        if st.button("Let's Go with Ruan! →"):
            if city and vendor_name:
                st.session_state.emotion = "excited"
                st.session_state.lang = lang
                st.session_state.business = business
                st.session_state.city = city
                st.session_state.vendor = vendor_name
                st.rerun()
            else:
                st.session_state.emotion = "worried"
                st.warning(
                    "Please enter your name and city!"
                )
                st.rerun()

    st.markdown("""
        <div style='text-align:center;padding:40px 20px;
        position:relative;z-index:1;'>
            <p style='font-size:13px;
            color:rgba(255,255,255,0.2);'>
                Ruan — Built for India.
                Built for Ramesh. Built to win.
            </p>
        </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# ANALYSIS PAGE
# ══════════════════════════════════════════════════════════
else:
    st.markdown(
        "<div style='padding-top:90px;'></div>",
        unsafe_allow_html=True
    )

    # ── Top bar ──
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.markdown(f"""
            <div style='display:flex;align-items:center;
            gap:12px;margin-bottom:8px;
            position:relative;z-index:1;'>
                <span style='font-size:22px;'>🏪</span>
                <div>
                    <p style='margin:0;font-weight:700;
                    font-size:18px;color:#FFFFFF;'>
                        {st.session_state.get('vendor','')}'s
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

    # ── Past history ──
    history = load_vendor_history(
        st.session_state.get('vendor', 'unknown')
    )
    if history and history.get('insights'):
        past = history['insights']
        st.markdown(f"""
            <div class='insight-card'
            style='border-left:4px solid #4AD295;
            margin-bottom:16px;'>
                <p style='color:#4AD295;font-size:12px;
                font-weight:600;margin:0 0 6px;
                text-transform:uppercase;letter-spacing:1px;'>
                    📚 Previous Analysis Found
                </p>
                <p style='color:rgba(255,255,255,0.6);
                font-size:13px;margin:0;'>
                    Last time your {history['business']}
                    had profit margin of
                    <b style='color:#FFFFFF;'>
                        {past.get('profit_margin',0)}%
                    </b>
                    and total profit of
                    <b style='color:#FFFFFF;'>
                        Rs {past.get('total_profit',0):,.0f}
                    </b>
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── Upload section ──
    st.markdown("""
        <div id="step-1"></div>
        <p class='section-label'
        style='position:relative;z-index:1;'>
            Step 1
        </p>
        <h3 style='color:#FFFFFF;font-weight:700;
        margin-bottom:16px;position:relative;z-index:1;'>
            Upload your sales data
        </h3>
        <p style='color:rgba(255,255,255,0.35);
        font-size:13px;margin-bottom:20px;'>
            CSV, Excel (.xlsx, .xls) — or no data?
            Ruan will still help you!
        </p>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs([
        "📁 Upload File",
        "📷 Photo of Register",
        "💬 Tell Ruan"
    ])

    uploaded_file = None

    with tab1:
        uploaded_file = st.file_uploader(
            "Upload",
            type=["csv", "xlsx", "xls"],
            label_visibility="collapsed"
        )

    with tab2:
        st.caption("Take a photo of your handwritten register")
        photo_file = st.file_uploader(
            "Upload photo",
            type=["jpg", "jpeg", "png"],
            label_visibility="collapsed",
            key="photo_upload"
        )

        if photo_file:
            with st.spinner("Ruan is reading your handwriting... 🔍"):
                ocr_df, raw_text = ocr_to_dataframe(photo_file)

            if ocr_df is not None:
                st.success(f"Found {len(ocr_df)} items!")
                st.dataframe(ocr_df, use_container_width=True)
                if st.button("✅ Use this data"):
                    # Convert to standard format for analysis
                    ocr_df['Sales'] = ocr_df['Quantity'] * ocr_df['Price']
                    ocr_df['Profit'] = ocr_df['Sales'] * 0.2  # estimate
                    uploaded_file = "ocr_data"
                    st.session_state.ocr_df = ocr_df
            else:
                st.warning(raw_text or "Could not read the image clearly. Try better lighting!")

    with tab3:
        st.caption(
            "Speak or type what you sold today — "
            "in any language!"
        )

        from core.voice import transcribe_audio

        # Voice recorder
        audio_value = st.audio_input(
            "🎤 Speak your sale",
            key="voice_recorder"
        )

        voice_text = ""
        if audio_value is not None:
            with st.spinner("Ruan is listening... 🎧"):
                audio_bytes = audio_value.read()
                transcribed, error = transcribe_audio(audio_bytes)

            if transcribed:
                st.success(f"🎤 Heard: \"{transcribed}\"")
                voice_text = transcribed
            else:
                st.warning(f"Could not understand audio: {error}")

        st.markdown("**Or type it:**")

        sale_text = st.text_input(
            "Tell Ruan",
            value=voice_text,
            placeholder="e.g. Aaj maine 50 Crocin becha 15 rupaye mein",
            label_visibility="collapsed",
            key="conversational_entry"
        )

        if st.button("Add Sale 💬", key="add_sale_btn"):
            if sale_text:
                with st.spinner("Understanding..."):
                    extracted = extract_sale_from_text(
                        sale_text, None,
                        st.session_state.get('vendor', 'friend'),
                        st.session_state.business,
                        st.session_state.city
                    )

                if extracted and extracted.get('found'):
                    save_conversational_entry(
                        st.session_state.get('vendor', 'unknown'),
                        extracted['item'],
                        extracted['quantity'],
                        extracted['price']
                    )
                    st.success(
                        f"✅ Added: {extracted['quantity']} x "
                        f"{extracted['item']} at "
                        f"Rs {extracted['price']} each"
                    )
                else:
                    st.warning(
                        "Couldn't understand that. Try: "
                        "'sold 50 Crocin at 15 rupees'"
                    )

        # Show entries so far
        entries_df = get_vendor_entries_as_df(
            st.session_state.get('vendor', 'unknown')
        )
        if entries_df is not None:
            st.markdown("##### Your entries so far:")
            st.dataframe(entries_df, use_container_width=True)

            if st.button("📊 Analyse my entries"):
                uploaded_file = "conversational_data"
                st.session_state.conv_df = entries_df

    # ── No data button ──
    col_a, col_b = st.columns([1, 1])
    with col_a:
        no_data_clicked = st.button(
            "📊 I have no data yet — show me industry averages",
            use_container_width=True
        )

    # ── Handle no data ──
    if no_data_clicked:
        st.session_state.emotion = "happy"
        fallback = handle_no_data_fallback(
            st.session_state.business,
            st.session_state.city
        )
        st.markdown(f"""
            <div class='insight-card'
            style='border-left:4px solid #4AD295;
            margin-top:24px;'>
                <p style='color:#4AD295;font-size:15px;
                font-weight:600;margin:0 0 8px;'>
                    🤖 No problem! Here's what to aim for
                </p>
                <p style='color:rgba(255,255,255,0.6);
                font-size:14px;margin:0;'>
                    {fallback['message']}
                </p>
            </div>
        """, unsafe_allow_html=True)
        f1, f2, f3 = st.columns(3)
        with f1:
            st.metric(
                "Target Margin",
                f"{fallback['avg_margin_low']}"
                f"-{fallback['avg_margin_high']}%"
            )
        with f2:
            st.metric(
                "Min Monthly Profit",
                f"Rs {fallback['min_viable_profit']:,}"
            )
        with f3:
            st.metric(
                "Typical Rent",
                f"Rs {fallback['typical_rent']:,}"
            )
        st.markdown("""
            <p class='section-label' style='margin-top:24px;'>
                Ruan's Tips to Get Started
            </p>
        """, unsafe_allow_html=True)
        for tip in fallback.get('tips', []):
            st.markdown(f"""
                <div class='insight-card'>
                    <span style='color:#4AD295;'>💡</span>
                    <span style='color:rgba(255,255,255,0.7);
                    font-size:14px;'> {tip}</span>
                </div>
            """, unsafe_allow_html=True)

    # ── Handle file upload ──
    if uploaded_file:
        st.markdown(
            get_ruan_widget(
                emotion="thinking",
                message="Reading your data... 🤔",
                owly_msg="Scanning every row carefully..."
            ),
            unsafe_allow_html=True
        )

        with st.spinner("Ruan is reading your data..."):
            if uploaded_file == "ocr_data":
                df = st.session_state.ocr_df
            elif uploaded_file == "conversational_data":
                df = st.session_state.conv_df.copy()
                df['Sales'] = df['Quantity'] * df['Price']
                df['Profit'] = df['Sales'] * 0.2
            else:
                df = load_sales_data(uploaded_file)

        if df is None:
            st.session_state.emotion = "worried"
            st.error(
                "Could not read file. "
                "Please check format and try again!"
            )
            st.stop()

        # Save df to session
        st.session_state.df_loaded = df

        # ── Data preview ──
        st.markdown("""
            <p class='section-label' style='margin-top:32px;'>
                Your Data
            </p>
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

        # ── Smart analysis ──
        with st.spinner("Ruan is finding insights..."):
            result = smart_analyse(
                df,
                st.session_state.business,
                st.session_state.city
            )

        # ── Handle results ──
        if result["status"] == "empty":
            st.session_state.emotion = "worried"
            st.warning(result['message'])
            fallback = result.get('fallback', {})
            if fallback:
                f1, f2, f3 = st.columns(3)
                with f1:
                    st.metric(
                        "Target Margin",
                        f"{fallback.get('avg_margin_low',0)}"
                        f"-{fallback.get('avg_margin_high',0)}%"
                    )
                with f2:
                    st.metric(
                        "Min Monthly Profit",
                        f"Rs {fallback.get('min_viable_profit',0):,}"
                    )
                with f3:
                    st.metric(
                        "Typical Rent",
                        f"Rs {fallback.get('typical_rent',0):,}"
                    )
            st.stop()

        elif result["status"] == "no_data":
            st.session_state.emotion = "worried"
            detection = result.get('detection', {})
            found = detection.get('found_cols', [])
            missing = detection.get('missing_cols', [])

            found_tags = "".join([
                f"<span style='background:rgba(74,210,149,0.1);"
                f"border:1px solid rgba(74,210,149,0.3);"
                f"color:#4AD295;font-size:11px;padding:3px 8px;"
                f"border-radius:20px;margin:3px;"
                f"display:inline-block;'>✅ {f}</span>"
                for f in found
            ])
            missing_tags = "".join([
                f"<span style='background:rgba(186,117,23,0.1);"
                f"border:1px solid rgba(186,117,23,0.3);"
                f"color:#EF9F27;font-size:11px;padding:3px 8px;"
                f"border-radius:20px;margin:3px;"
                f"display:inline-block;'>❌ Missing: {m}</span>"
                for m in missing
            ])
            st.markdown(f"""
                <div class='insight-card'
                style='border-left:4px solid #BA7517;'>
                    <p style='color:#EF9F27;font-weight:600;
                    margin:0 0 8px;'>
                        🤔 Ruan couldn't recognise this data
                    </p>
                    <p style='color:rgba(255,255,255,0.6);
                    font-size:14px;margin:0 0 12px;'>
                        {result['message']}
                    </p>
                    {found_tags}{missing_tags}
                </div>
            """, unsafe_allow_html=True)
            fallback = result.get('fallback', {})
            if fallback:
                st.markdown("""
                    <p class='section-label'
                    style='margin-top:24px;'>
                        Industry Averages for You
                    </p>
                """, unsafe_allow_html=True)
                f1, f2, f3 = st.columns(3)
                with f1:
                    st.metric(
                        "Target Margin",
                        f"{fallback.get('avg_margin_low',0)}"
                        f"-{fallback.get('avg_margin_high',0)}%"
                    )
                with f2:
                    st.metric(
                        "Min Monthly Profit",
                        f"Rs {fallback.get('min_viable_profit',0):,}"
                    )
                with f3:
                    st.metric(
                        "Typical Rent",
                        f"Rs {fallback.get('typical_rent',0):,}"
                    )
                for tip in fallback.get('tips', []):
                    st.markdown(f"""
                        <div class='insight-card'>
                            <span style='color:#4AD295;'>💡</span>
                            <span style='color:rgba(255,255,255,0.7);
                            font-size:14px;'> {tip}</span>
                        </div>
                    """, unsafe_allow_html=True)
            st.stop()

        elif result["status"] == "guessed":
            st.warning(
                "⚠️ Ruan made a best-guess analysis "
                "— data format was unusual."
            )
            insights = result.get('insights', {})
        else:
            insights = result.get('insights', {})

        # Save insights to session
        st.session_state.insights = insights

        # Save vendor data
        save_vendor_data(
            st.session_state.get('vendor', 'unknown'),
            st.session_state.city,
            st.session_state.business,
            insights
        )
        # Save to RAG memory
        save_analysis_to_memory(
            st.session_state.get('vendor', 'unknown'),
            st.session_state.business,
            st.session_state.city,
            insights
        )

        # Update widget
        st.markdown(
            get_ruan_widget(
                emotion="excited",
                message="I found amazing insights! 🎉",
                owly_msg="Scroll down to see everything!"
            ),
            unsafe_allow_html=True
        )

        # ── Cinematic storytelling ──
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

        # ── Health check ──
        health = check_profit_health(
            insights.get('total_profit', 0),
            st.session_state.business,
            st.session_state.city,
            insights.get('profit_margin', 0)
        )

        st.markdown(f"""
            <div class='insight-card' style='
            background:{health["color"]};
            border-left:4px solid {health["border"]};'>
                <p style='margin:0 0 8px;'>
                    <span style='font-size:20px;'>
                        {health["emoji"]}
                    </span>
                    <span style='font-size:16px;
                    font-weight:700;color:#FFFFFF;
                    margin-left:8px;'>
                        Business Health —
                        {health["status"].title()}
                    </span>
                </p>
                <p style='margin:0;font-size:14px;
                color:rgba(255,255,255,0.7);'>
                    {health["advice"]}
                </p>
            </div>
        """, unsafe_allow_html=True)

        # ── Key metrics ──
        st.markdown("""
            <p class='section-label'
            style='margin-top:32px;'>Key Numbers</p>
        """, unsafe_allow_html=True)

        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric(
                "Total Revenue",
                f"Rs {insights.get('total_revenue',0):,.0f}"
            )
        with m2:
            st.metric(
                "Total Profit",
                f"Rs {insights.get('total_profit',0):,.0f}"
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

        # ══════════════════════════════════════════════════
        # CHARTS — only shown after data is loaded
        # ══════════════════════════════════════════════════
        st.markdown("""
            <p class='section-label'
            style='margin-top:32px;'>Visual Insights</p>
            <h3 style='color:#FFFFFF;font-weight:700;
            margin-bottom:16px;'>
                Your business in charts
            </h3>
        """, unsafe_allow_html=True)

        # Row 1 — Revenue + Margin gauge
        ch1, ch2 = st.columns([3, 2])
        with ch1:
            fig1 = revenue_profit_chart(insights)
            if fig1:
                st.plotly_chart(
                    fig1,
                    use_container_width=True,
                    config={'displayModeBar': False}
                )
        with ch2:
            fig4 = profit_margin_gauge(
                insights.get('profit_margin', 0),
                st.session_state.business
            )
            if fig4:
                st.plotly_chart(
                    fig4,
                    use_container_width=True,
                    config={'displayModeBar': False}
                )

        # Row 2 — Daily trend
        fig2 = daily_trend_chart(df)
        if fig2:
            st.plotly_chart(
                fig2,
                use_container_width=True,
                config={'displayModeBar': False}
            )

        # Row 3 — Products + Days
        ch3, ch4 = st.columns(2)
        with ch3:
            fig3 = product_performance_chart(df)
            if fig3:
                st.plotly_chart(
                    fig3,
                    use_container_width=True,
                    config={'displayModeBar': False}
                )
        with ch4:
            fig5 = day_performance_chart(df)
            if fig5:
                st.plotly_chart(
                    fig5,
                    use_container_width=True,
                    config={'displayModeBar': False}
                )

        st.markdown("<hr>", unsafe_allow_html=True)

        # ── Ruan message ──
        st.markdown("""
            <p class='section-label'>Ruan Says</p>
        """, unsafe_allow_html=True)
        msg = generate_ruan_message(
            insights,
            st.session_state.business,
            st.session_state.city,
            st.session_state.lang
        )
        st.info(msg)

        # ── Owly wisdom ──
        best_product = insights.get('best_product', 'N/A')
        worst_product = insights.get('worst_product', 'N/A')
        st.markdown(f"""
            <div class='insight-card'
            style='border-left:4px solid #BA7517;'>
                <p style='margin:0 0 6px;font-size:15px;
                font-weight:600;color:#EF9F27;'>
                    🦉 Owly's Wisdom
                </p>
                <p style='margin:0;font-size:14px;
                color:rgba(255,255,255,0.6);'>
                    Focus on
                    <b style='color:#FFFFFF;'>
                        {best_product}
                    </b>
                    — your highest profit product.
                    Reduce stock of
                    <b style='color:#FFFFFF;'>
                        {worst_product}
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
                style='margin-top:32px;'>Top Actions</p>
                <h3 style='color:#FFFFFF;font-weight:700;
                margin-bottom:16px;'>
                    Ruan's recommendations for you
                </h3>
            """, unsafe_allow_html=True)
            for i, win in enumerate(wins, 1):
                st.markdown(f"""
                    <div class='insight-card'>
                        <span style='color:#4AD295;
                        font-weight:700;'>{i}.</span>
                        <span style='color:rgba(255,255,255,0.8);
                        font-size:14px;'> {win}</span>
                    </div>
                """, unsafe_allow_html=True)

        # ── Best vs worst ──
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
                style='border-left:4px solid #4AD295;
                text-align:center;'>
                    <p style='font-size:11px;color:#4AD295;
                    margin:0;text-transform:uppercase;
                    letter-spacing:1px;'>⭐ Best Product</p>
                    <p style='font-size:20px;font-weight:700;
                    color:#FFFFFF;margin:8px 0 4px;'>
                        {best_product}
                    </p>
                    <p style='font-size:14px;
                    color:#4AD295;margin:0;'>
                        Rs {insights.get('best_product_profit',0):,.0f}
                    </p>
                </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
                <div class='insight-card'
                style='border-left:4px solid #791F1F;
                text-align:center;'>
                    <p style='font-size:11px;color:#EF4444;
                    margin:0;text-transform:uppercase;
                    letter-spacing:1px;'>⚠️ Needs Attention</p>
                    <p style='font-size:20px;font-weight:700;
                    color:#FFFFFF;margin:8px 0 4px;'>
                        {worst_product}
                    </p>
                    <p style='font-size:14px;
                    color:#EF4444;margin:0;'>
                        Rs {insights.get('worst_product_profit',0):,.0f}
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
                    style='border-left:4px solid #4AD295;
                    text-align:center;'>
                        <p style='color:#4AD295;margin:0;
                        font-size:11px;text-transform:uppercase;
                        letter-spacing:1px;'>✅ Best Day</p>
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
                        font-size:11px;text-transform:uppercase;
                        letter-spacing:1px;'>❌ Worst Day</p>
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
                f"Rs {insights.get('high_discount_profit',0):,.2f}"
                f" vs Low discount avg: "
                f"Rs {insights.get('low_discount_profit',0):,.2f}"
            )

        # ── Chat section ──
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("""
            <p class='section-label'>Ask Ruan</p>
            <h3 style='color:#FFFFFF;font-weight:700;
            margin-bottom:8px;'>
                Ask anything about your business
            </h3>
            <p style='color:rgba(255,255,255,0.35);
            font-size:13px;margin-bottom:16px;'>
                In plain language — no technical terms needed
            </p>
        """, unsafe_allow_html=True)

        # ── Response style toggle ──
        response_style = st.radio(
            "Response style",
            ["💬 Detailed — explain why too",
             "⚡ Simple — just tell me what to do"],
            horizontal=True,
            label_visibility="collapsed"
        )
        st.session_state.response_style = (
            "simple" if "Simple" in response_style
            else "detailed"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # Chat history
        for chat_msg in st.session_state.messages:
            if chat_msg["role"] == "user":
                st.markdown(f"""
                    <div class='chat-user'>
                        👤 {chat_msg["content"]}
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class='chat-ruan'>
                        🤖 {chat_msg["content"]}
                    </div>
                """, unsafe_allow_html=True)

        # ── Question input ──
        question = st.text_input(
            "Ask Ruan anything",
            placeholder=(
                "e.g. Why am I losing money? "
                "What should I stock? "
                "ನನ್ನ ಅಂಗಡಿ ಹೇಗೆ ಸುಧಾರಿಸಲಿ?"
            ),
            label_visibility="collapsed"
        )

        if st.button("Ask Ruan! 🤖", use_container_width=True):
            if question:
                st.session_state.messages.append({
                    "role": "user",
                    "content": question
                })
                with st.spinner("Ruan is thinking... 🤔"):
                    response = ask_ruan(
                        question=question,
                        vendor=st.session_state.get('vendor', 'friend'),
                        business=st.session_state.business,
                        city=st.session_state.city,
                        language=st.session_state.lang,
                        insights=st.session_state.insights,
                        response_style=st.session_state.get(
                            'response_style', 'detailed')
                    )
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })
                # Save Q&A to memory
                save_question_to_memory(
                    st.session_state.get('vendor', 'unknown'),
                    question,
                    response
                )
                st.session_state.emotion = "excited"
                st.rerun()
            else:
                st.warning("Please type a question!")

        # ── Memory timeline ──
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("""
            <p class='section-label'>Sacred Timeline</p>
            <h3 style='color:#FFFFFF;font-weight:700;
            margin-bottom:16px;'>
                Ruan's memory of your business
            </h3>
        """, unsafe_allow_html=True)

        memory_summary = get_vendor_memory_summary(
            st.session_state.get('vendor', 'unknown')
        )

        if memory_summary and memory_summary['total_memories'] > 0:
            st.markdown(f"""
                <div class='insight-card'
                style='border-left:4px solid #4AD295;'>
                    <p style='color:#4AD295;font-size:13px;
                    font-weight:600;margin:0 0 8px;
                    text-transform:uppercase;letter-spacing:1px;'>
                        🧠 Memory Active
                    </p>
                    <p style='color:rgba(255,255,255,0.6);
                    font-size:13px;margin:0;'>
                        Ruan remembers
                        <b style='color:#FFFFFF;'>
                            {memory_summary['total_memories']}
                        </b>
                        interactions from your business history.
                        <b style='color:#FFFFFF;'>
                            {memory_summary['analysis_count']}
                        </b>
                        data analyses stored.
                    </p>
                </div>
            """, unsafe_allow_html=True)

            # Show timeline entries
            entries = memory_summary.get('entries', [])
            if entries:
                for entry in entries[-3:]:
                    profit = entry.get('profit', '0')
                    margin = entry.get('margin', '0')
                    date = entry.get('date', 'Unknown')
                    st.markdown(f"""
                        <div class='insight-card'
                        style='margin:6px 0;'>
                            <p style='color:rgba(255,255,255,0.4);
                            font-size:11px;margin:0 0 4px;
                            text-transform:uppercase;
                            letter-spacing:0.5px;'>
                                📅 {date}
                            </p>
                            <p style='color:rgba(255,255,255,0.7);
                            font-size:13px;margin:0;'>
                                Profit:
                                <b style='color:#4AD295;'>
                                    Rs {float(profit):,.0f}
                                </b>
                                • Margin:
                                <b style='color:#4AD295;'>
                                    {margin}%
                                </b>
                            </p>
                        </div>
                    """, unsafe_allow_html=True)

            # Clear memory button
            if st.button(
                "🗑️ Clear Memory",
                use_container_width=False
            ):
                clear_vendor_memory(
                    st.session_state.get('vendor', 'unknown')
                )
                st.success("Memory cleared! Fresh start. ✅")
                st.rerun()

        else:
            st.markdown(f"""
                <div class='insight-card'
                style='border-left:4px solid rgba(255,255,255,0.1);'>
                    <p style='color:rgba(255,255,255,0.4);
                    font-size:13px;margin:0;'>
                        🧠 No memories yet.
                        Upload data and Ruan will start
                        building your business timeline.
                    </p>
                </div>
            """, unsafe_allow_html=True)

    # ── Footer ──
    st.markdown("""
        <div style='text-align:center;
        padding:60px 20px;
        border-top:1px solid rgba(74,210,149,0.06);
        margin-top:60px;position:relative;z-index:1;'>
            <p style='font-size:22px;font-weight:800;
            color:#FFFFFF;margin:0 0 8px;'>Ruan.</p>
            <p style='font-size:13px;
            color:rgba(255,255,255,0.25);margin:0;'>
                Built for India's small businesses.
                Your data never leaves your device.
                100% private. 100% free. Forever.
            </p>
        </div>
    """, unsafe_allow_html=True)
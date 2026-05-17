def get_dark_theme():
    return """
<style>
    /* ── Import Font ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    /* ── Global Dark Theme ── */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
    }

    .stApp {
        background: #08080F;
        color: #FFFFFF;
    }

    /* ── Hide Streamlit default elements ── */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    .stDeployButton { display: none; }

    /* ── Main container ── */
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    /* ── Hero Section ── */
    .hero-section {
        background: linear-gradient(
            135deg,
            #08080F 0%,
            #0D0D1F 40%,
            #0A0A1A 100%
        );
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 40px 20px;
        position: relative;
        overflow: hidden;
    }

    /* ── Glow effects ── */
    .hero-section::before {
        content: '';
        position: absolute;
        top: -200px;
        left: 50%;
        transform: translateX(-50%);
        width: 600px;
        height: 600px;
        background: radial-gradient(
            circle,
            rgba(83,74,183,0.15) 0%,
            transparent 70%
        );
        pointer-events: none;
    }

    .hero-section::after {
        content: '';
        position: absolute;
        bottom: -100px;
        right: -100px;
        width: 400px;
        height: 400px;
        background: radial-gradient(
            circle,
            rgba(29,158,117,0.08) 0%,
            transparent 70%
        );
        pointer-events: none;
    }

    /* ── Nav ── */
    .ruan-nav {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 999;
        background: rgba(8,8,15,0.85);
        backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(255,255,255,0.06);
        padding: 16px 40px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .nav-logo {
        font-size: 22px;
        font-weight: 800;
        color: #FFFFFF;
        letter-spacing: -0.5px;
    }

    .nav-logo span {
        color: #7F77DD;
    }

    .nav-links {
        display: flex;
        gap: 32px;
    }

    .nav-link {
        font-size: 14px;
        font-weight: 500;
        color: rgba(255,255,255,0.6);
        text-decoration: none;
        transition: color 0.2s;
    }

    .nav-link:hover { color: #FFFFFF; }

    /* ── Hero headline ── */
    .hero-headline {
        font-size: clamp(36px, 6vw, 72px);
        font-weight: 900;
        line-height: 1.05;
        text-align: center;
        letter-spacing: -2px;
        margin: 0 0 20px;
        color: #FFFFFF;
    }

    .hero-headline .highlight {
        background: linear-gradient(
            135deg,
            #7F77DD 0%,
            #1D9E75 100%
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .hero-sub {
        font-size: clamp(15px, 2vw, 18px);
        color: rgba(255,255,255,0.5);
        text-align: center;
        max-width: 540px;
        line-height: 1.6;
        margin: 0 0 40px;
    }

    /* ── CTA Button ── */
    .cta-btn {
        display: inline-block;
        background: linear-gradient(135deg, #534AB7, #7F77DD);
        color: white !important;
        padding: 16px 40px;
        border-radius: 50px;
        font-size: 16px;
        font-weight: 600;
        text-decoration: none;
        border: none;
        cursor: pointer;
        box-shadow: 0 8px 32px rgba(83,74,183,0.4);
        transition: all 0.3s;
        letter-spacing: 0.3px;
    }

    .cta-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 40px rgba(83,74,183,0.6);
    }

    /* ── Stats bar ── */
    .stats-bar {
        display: flex;
        gap: 48px;
        margin-top: 60px;
        padding-top: 40px;
        border-top: 1px solid rgba(255,255,255,0.08);
    }

    .stat-item {
        text-align: center;
    }

    .stat-number {
        font-size: 28px;
        font-weight: 800;
        color: #FFFFFF;
        letter-spacing: -1px;
    }

    .stat-label {
        font-size: 12px;
        color: rgba(255,255,255,0.4);
        margin-top: 4px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* ── Feature cards ── */
    .features-section {
        background: #0D0D1F;
        padding: 80px 40px;
    }

    .section-label {
        font-size: 12px;
        font-weight: 600;
        color: #7F77DD;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-align: center;
        margin-bottom: 16px;
    }

    .section-title {
        font-size: clamp(28px, 4vw, 42px);
        font-weight: 800;
        color: #FFFFFF;
        text-align: center;
        letter-spacing: -1px;
        margin-bottom: 48px;
        line-height: 1.1;
    }

    .cards-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
        max-width: 1100px;
        margin: 0 auto;
    }

    .feature-card {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 20px;
        padding: 28px;
        transition: all 0.3s;
    }

    .feature-card:hover {
        background: rgba(83,74,183,0.08);
        border-color: rgba(83,74,183,0.3);
        transform: translateY(-4px);
    }

    .card-icon {
        font-size: 28px;
        margin-bottom: 16px;
    }

    .card-title {
        font-size: 17px;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 8px;
    }

    .card-desc {
        font-size: 14px;
        color: rgba(255,255,255,0.5);
        line-height: 1.6;
    }

    /* ── Analysis section ── */
    .analysis-section {
        background: #08080F;
        padding: 80px 40px;
        max-width: 900px;
        margin: 0 auto;
    }

    /* ── Upload area ── */
    div[data-testid="stFileUploader"] {
        background: rgba(255,255,255,0.02) !important;
        border: 2px dashed rgba(83,74,183,0.4) !important;
        border-radius: 20px !important;
        padding: 32px !important;
    }

    div[data-testid="stFileUploader"]:hover {
        border-color: rgba(83,74,183,0.8) !important;
        background: rgba(83,74,183,0.05) !important;
    }

    /* ── Streamlit overrides for dark ── */
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 12px !important;
        color: white !important;
    }

    .stTextInput > div > div > input {
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 12px !important;
        color: white !important;
    }

    .stTextInput > div > div > input::placeholder {
        color: rgba(255,255,255,0.3) !important;
    }

    /* ── Buttons ── */
    .stButton > button {
        background: linear-gradient(
            135deg, #534AB7, #7F77DD
        ) !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 14px 32px !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        letter-spacing: 0.3px !important;
        box-shadow: 0 8px 24px rgba(83,74,183,0.35) !important;
        transition: all 0.3s !important;
        width: 100% !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 32px rgba(83,74,183,0.5) !important;
    }

    /* ── Metrics dark ── */
    div[data-testid="metric-container"] {
        background: rgba(255,255,255,0.03) !important;
        border: 1px solid rgba(255,255,255,0.07) !important;
        border-radius: 16px !important;
        padding: 20px !important;
    }

    div[data-testid="metric-container"] label {
        color: rgba(255,255,255,0.5) !important;
        font-size: 12px !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }

    div[data-testid="metric-container"] [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }

    /* ── Dataframe dark ── */
    .stDataFrame {
        border-radius: 16px !important;
        overflow: hidden !important;
        border: 1px solid rgba(255,255,255,0.07) !important;
    }

    /* ── Info/success/warning boxes ── */
    .stInfo {
        background: rgba(83,74,183,0.15) !important;
        border: 1px solid rgba(83,74,183,0.3) !important;
        border-radius: 16px !important;
        color: #FFFFFF !important;
    }

    .stSuccess {
        background: rgba(29,158,117,0.15) !important;
        border: 1px solid rgba(29,158,117,0.3) !important;
        border-radius: 16px !important;
        color: #FFFFFF !important;
    }

    .stWarning {
        background: rgba(186,117,23,0.15) !important;
        border: 1px solid rgba(186,117,23,0.3) !important;
        border-radius: 16px !important;
        color: #FFFFFF !important;
    }

    .stError {
        background: rgba(121,31,31,0.15) !important;
        border: 1px solid rgba(121,31,31,0.3) !important;
        border-radius: 16px !important;
        color: #FFFFFF !important;
    }

    /* ── Spinner ── */
    .stSpinner > div {
        border-top-color: #7F77DD !important;
    }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar {
        width: 6px;
    }
    ::-webkit-scrollbar-track {
        background: #08080F;
    }
    ::-webkit-scrollbar-thumb {
        background: rgba(83,74,183,0.4);
        border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(83,74,183,0.7);
    }

    /* ── Section headings ── */
    h1, h2, h3, h4 {
        color: #FFFFFF !important;
        font-family: 'Inter', sans-serif !important;
    }

    /* ── Caption text ── */
    .stCaption {
        color: rgba(255,255,255,0.4) !important;
    }

    /* ── Insight cards dark ── */
    .insight-card {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 16px;
        padding: 20px 24px;
        margin: 8px 0;
        transition: all 0.3s;
    }

    .insight-card:hover {
        border-color: rgba(83,74,183,0.3);
        background: rgba(83,74,183,0.05);
    }

    /* ── Chat bubbles dark ── */
    .chat-user {
        background: rgba(83,74,183,0.2);
        border: 1px solid rgba(83,74,183,0.3);
        border-radius: 16px 16px 4px 16px;
        padding: 12px 18px;
        margin: 8px 0;
        color: #FFFFFF;
        font-size: 14px;
        text-align: right;
    }

    .chat-ruan {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px 16px 16px 4px;
        padding: 12px 18px;
        margin: 8px 0;
        color: rgba(255,255,255,0.85);
        font-size: 14px;
    }

    /* ── Tagline ── */
    .tagline {
        font-size: 13px;
        color: rgba(255,255,255,0.35);
        text-align: center;
        letter-spacing: 0.3px;
        margin-top: 8px;
    }

    /* ── Divider ── */
    hr {
        border-color: rgba(255,255,255,0.06) !important;
        margin: 40px 0 !important;
    }

    /* ── Badge ── */
    .badge {
        display: inline-block;
        background: rgba(83,74,183,0.2);
        border: 1px solid rgba(83,74,183,0.4);
        color: #9B95E8;
        font-size: 11px;
        font-weight: 600;
        padding: 4px 12px;
        border-radius: 20px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
</style>
"""
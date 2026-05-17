def get_nature_theme():
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* ── Global ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}

/* ── Hide Streamlit defaults ── */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }
.stDeployButton { display: none; }

/* ── Main background — deep forest ── */
.stApp {
    background: #060D0A;
    color: #FFFFFF;
    min-height: 100vh;
}

.main .block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ── Animated forest background ── */
.forest-bg {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    z-index: 0;
    overflow: hidden;
    pointer-events: none;
}

/* ── Firefly particles ── */
@keyframes firefly {
    0%   { transform: translate(0,0) scale(1); opacity:0; }
    20%  { opacity: 0.8; }
    80%  { opacity: 0.6; }
    100% { transform: translate(var(--tx), var(--ty)) scale(0.5); opacity:0; }
}

@keyframes glow-pulse {
    0%,100% { box-shadow: 0 0 4px 2px rgba(74,210,149,0.6); }
    50%      { box-shadow: 0 0 12px 6px rgba(74,210,149,0.9); }
}

.firefly {
    position: absolute;
    width: 4px; height: 4px;
    border-radius: 50%;
    background: #4AD295;
    animation: firefly var(--dur) ease-in-out infinite,
               glow-pulse 2s ease-in-out infinite;
}

/* ── Forest trees silhouette ── */
.forest-silhouette {
    position: fixed;
    bottom: 0; left: 0;
    width: 100%; height: 35%;
    background: linear-gradient(
        to top,
        #030806 0%,
        #060D0A 60%,
        transparent 100%
    );
    z-index: 0;
    pointer-events: none;
}

/* ── Navbar ── */
.ruan-nav {
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 999;
    background: rgba(6,13,10,0.85);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(74,210,149,0.1);
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

.nav-logo span { color: #4AD295; }

.nav-links {
    display: flex;
    gap: 32px;
}

.nav-link {
    font-size: 14px;
    font-weight: 500;
    color: rgba(255,255,255,0.5);
    text-decoration: none;
}

.nav-link:hover { color: #4AD295; }

/* ── Badge ── */
.badge {
    display: inline-block;
    background: rgba(74,210,149,0.1);
    border: 1px solid rgba(74,210,149,0.3);
    color: #4AD295;
    font-size: 11px;
    font-weight: 600;
    padding: 4px 12px;
    border-radius: 20px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

/* ── Hero ── */
.hero-section {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 120px 20px 60px;
    position: relative;
    z-index: 1;
}

/* ── Green glow behind hero ── */
.hero-section::before {
    content: '';
    position: absolute;
    top: 20%;
    left: 50%;
    transform: translateX(-50%);
    width: 700px;
    height: 400px;
    background: radial-gradient(
        ellipse,
        rgba(74,210,149,0.06) 0%,
        transparent 70%
    );
    pointer-events: none;
}

/* ── Hero headline ── */
.hero-headline {
    font-size: clamp(36px,6vw,72px);
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
        #4AD295 0%,
        #2DB87E 50%,
        #89D4B0 100%
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-sub {
    font-size: clamp(15px,2vw,18px);
    color: rgba(255,255,255,0.45);
    text-align: center;
    max-width: 540px;
    line-height: 1.6;
    margin: 0 0 40px;
}

/* ── Stats ── */
.stats-bar {
    display: flex;
    gap: 48px;
    margin-top: 60px;
    padding-top: 40px;
    border-top: 1px solid rgba(74,210,149,0.1);
}

.stat-number {
    font-size: 28px;
    font-weight: 800;
    color: #4AD295;
    letter-spacing: -1px;
}

.stat-label {
    font-size: 11px;
    color: rgba(255,255,255,0.35);
    margin-top: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    text-align: center;
}

/* ── Feature cards ── */
.features-section {
    background: rgba(10,20,15,0.9);
    padding: 80px 40px;
    position: relative;
    z-index: 1;
    border-top: 1px solid rgba(74,210,149,0.08);
}

.section-label {
    font-size: 11px;
    font-weight: 600;
    color: #4AD295;
    text-transform: uppercase;
    letter-spacing: 2px;
    text-align: center;
    margin-bottom: 16px;
}

.section-title {
    font-size: clamp(28px,4vw,42px);
    font-weight: 800;
    color: #FFFFFF;
    text-align: center;
    letter-spacing: -1px;
    margin-bottom: 48px;
    line-height: 1.1;
}

.cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit,minmax(260px,1fr));
    gap: 16px;
    max-width: 1100px;
    margin: 0 auto;
}

.feature-card {
    background: rgba(74,210,149,0.03);
    border: 1px solid rgba(74,210,149,0.08);
    border-radius: 20px;
    padding: 28px;
    transition: all 0.3s;
}

.feature-card:hover {
    background: rgba(74,210,149,0.07);
    border-color: rgba(74,210,149,0.25);
    transform: translateY(-4px);
    box-shadow: 0 8px 32px rgba(74,210,149,0.1);
}

.card-icon { font-size: 28px; margin-bottom: 14px; }

.card-title {
    font-size: 16px;
    font-weight: 700;
    color: #FFFFFF;
    margin-bottom: 8px;
}

.card-desc {
    font-size: 13px;
    color: rgba(255,255,255,0.45);
    line-height: 1.6;
}

/* ── Analysis section ── */
.analysis-wrap {
    position: relative;
    z-index: 1;
    padding: 80px 40px;
    max-width: 900px;
    margin: 0 auto;
}

/* ── Upload area ── */
div[data-testid="stFileUploader"] {
    background: rgba(74,210,149,0.03) !important;
    border: 2px dashed rgba(74,210,149,0.25) !important;
    border-radius: 20px !important;
    padding: 32px !important;
    transition: all 0.3s !important;
}

div[data-testid="stFileUploader"]:hover {
    border-color: rgba(74,210,149,0.6) !important;
    background: rgba(74,210,149,0.06) !important;
    box-shadow: 0 0 30px rgba(74,210,149,0.1) !important;
}

/* ── Inputs ── */
.stSelectbox > div > div {
    background: rgba(74,210,149,0.04) !important;
    border: 1px solid rgba(74,210,149,0.15) !important;
    border-radius: 12px !important;
    color: white !important;
}

.stTextInput > div > div > input {
    background: rgba(74,210,149,0.04) !important;
    border: 1px solid rgba(74,210,149,0.15) !important;
    border-radius: 12px !important;
    color: white !important;
}

.stTextInput > div > div > input::placeholder {
    color: rgba(255,255,255,0.25) !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(
        135deg,
        #1D9E75,
        #4AD295
    ) !important;
    color: #060D0A !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 14px 32px !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    letter-spacing: 0.3px !important;
    box-shadow: 0 8px 24px rgba(74,210,149,0.3) !important;
    transition: all 0.3s !important;
    width: 100% !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 12px 32px rgba(74,210,149,0.5) !important;
}

/* ── Metrics ── */
div[data-testid="metric-container"] {
    background: rgba(74,210,149,0.04) !important;
    border: 1px solid rgba(74,210,149,0.12) !important;
    border-radius: 16px !important;
    padding: 20px !important;
}

div[data-testid="metric-container"] label {
    color: rgba(255,255,255,0.4) !important;
    font-size: 11px !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}

div[data-testid="metric-container"]
[data-testid="stMetricValue"] {
    color: #4AD295 !important;
    font-weight: 800 !important;
}

/* ── Dataframe ── */
.stDataFrame {
    border-radius: 16px !important;
    overflow: hidden !important;
    border: 1px solid rgba(74,210,149,0.1) !important;
}

/* ── Alert boxes ── */
.stInfo {
    background: rgba(74,210,149,0.08) !important;
    border: 1px solid rgba(74,210,149,0.2) !important;
    border-radius: 16px !important;
    color: #FFFFFF !important;
}

.stSuccess {
    background: rgba(29,158,117,0.12) !important;
    border: 1px solid rgba(29,158,117,0.3) !important;
    border-radius: 16px !important;
    color: #FFFFFF !important;
}

.stWarning {
    background: rgba(186,117,23,0.12) !important;
    border: 1px solid rgba(186,117,23,0.3) !important;
    border-radius: 16px !important;
    color: #FFFFFF !important;
}

.stError {
    background: rgba(121,31,31,0.12) !important;
    border: 1px solid rgba(121,31,31,0.3) !important;
    border-radius: 16px !important;
    color: #FFFFFF !important;
}

/* ── Insight cards ── */
.insight-card {
    background: rgba(74,210,149,0.03);
    border: 1px solid rgba(74,210,149,0.1);
    border-radius: 16px;
    padding: 20px 24px;
    margin: 8px 0;
    transition: all 0.3s;
}

.insight-card:hover {
    border-color: rgba(74,210,149,0.3);
    background: rgba(74,210,149,0.06);
    box-shadow: 0 4px 20px rgba(74,210,149,0.08);
}

/* ── Chat bubbles ── */
.chat-user {
    background: rgba(74,210,149,0.1);
    border: 1px solid rgba(74,210,149,0.2);
    border-radius: 16px 16px 4px 16px;
    padding: 12px 18px;
    margin: 8px 0;
    color: #FFFFFF;
    font-size: 14px;
    text-align: right;
}

.chat-ruan {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px 16px 16px 4px;
    padding: 12px 18px;
    margin: 8px 0;
    color: rgba(255,255,255,0.8);
    font-size: 14px;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #060D0A; }
::-webkit-scrollbar-thumb {
    background: rgba(74,210,149,0.3);
    border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover {
    background: rgba(74,210,149,0.6);
}

/* ── Headings ── */
h1,h2,h3,h4 {
    color: #FFFFFF !important;
    font-family: 'Inter', sans-serif !important;
}

.stCaption {
    color: rgba(255,255,255,0.35) !important;
}

hr {
    border-color: rgba(74,210,149,0.08) !important;
    margin: 40px 0 !important;
}

/* ── Floating Ruan widget ── */
@keyframes widget-float {
    0%,100% { transform: translateY(0px); }
    50%      { transform: translateY(-8px); }
}

@keyframes widget-glow {
    0%,100% {
        box-shadow: 0 8px 32px rgba(74,210,149,0.2);
    }
    50% {
        box-shadow: 0 8px 48px rgba(74,210,149,0.5);
    }
}

@keyframes slide-in-right {
    from {
        transform: translateX(120px);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 1;
    }
}

.ruan-widget {
    position: fixed;
    bottom: 24px;
    right: 24px;
    z-index: 998;
    background: rgba(6,13,10,0.92);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(74,210,149,0.2);
    border-radius: 24px;
    padding: 16px;
    width: 220px;
    animation: widget-float 3s ease-in-out infinite,
               widget-glow 3s ease-in-out infinite,
               slide-in-right 0.5s ease-out;
    cursor: pointer;
    transition: width 0.3s, padding 0.3s;
}

.ruan-widget:hover {
    border-color: rgba(74,210,149,0.5);
    width: 260px;
}

.widget-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
}

.widget-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #4AD295;
    animation: glow-pulse 2s ease-in-out infinite;
}

.widget-name {
    font-size: 13px;
    font-weight: 700;
    color: #4AD295;
}

.widget-status {
    font-size: 11px;
    color: rgba(255,255,255,0.4);
    margin-left: auto;
}

.widget-msg {
    font-size: 12px;
    color: rgba(255,255,255,0.7);
    line-height: 1.5;
    padding: 8px 10px;
    background: rgba(74,210,149,0.06);
    border-radius: 10px;
    border-left: 2px solid #4AD295;
}

.owly-msg {
    font-size: 11px;
    color: rgba(255,255,255,0.45);
    line-height: 1.5;
    padding: 6px 10px;
    background: rgba(186,117,23,0.06);
    border-radius: 10px;
    border-left: 2px solid #BA7517;
    margin-top: 6px;
}
</style>

<script>
// ── Firefly particles ──
function createFireflies() {
    const container = document.querySelector('.forest-bg');
    if (!container) return;
    for (let i = 0; i < 35; i++) {
        const ff = document.createElement('div');
        ff.className = 'firefly';
        ff.style.cssText = `
            left: ${Math.random()*100}%;
            top: ${Math.random()*100}%;
            --tx: ${(Math.random()-0.5)*200}px;
            --ty: ${-Math.random()*300-50}px;
            --dur: ${Math.random()*6+4}s;
            animation-delay: ${Math.random()*8}s;
            width: ${Math.random()*3+2}px;
            height: ${Math.random()*3+2}px;
            background: ${Math.random()>0.5
                ? '#4AD295'
                : '#89D4B0'};
        `;
        container.appendChild(ff);
    }
}
setTimeout(createFireflies, 500);
</script>
"""


def get_forest_background():
    """Animated forest background with fireflies"""
    return """
<div class="forest-bg" id="forestBg"></div>
<div class="forest-silhouette"></div>
"""


def get_ruan_widget(emotion="happy", message="", owly_msg=""):
    """Floating Ruan companion widget"""

    emotions = {
        "happy":     ("🤖", "Ready to help!"),
        "thinking":  ("🤔", "Analysing..."),
        "excited":   ("🎉", "Found insights!"),
        "worried":   ("⚠️", "Needs attention"),
        "surprised": ("😮", "Interesting!"),
    }

    emoji, status = emotions.get(
        emotion, emotions["happy"]
    )

    ruan_msg = message or {
        "happy":     "Namaste! Upload your data 🙏",
        "thinking":  "Reading your data carefully...",
        "excited":   "Amazing insights found! 🎉",
        "worried":   "Something needs your attention!",
        "surprised": "Wow this is interesting!",
    }.get(emotion, "How can I help?")

    owly_message = owly_msg or {
        "happy":     "Upload CSV or Excel to begin",
        "thinking":  "Scanning every row...",
        "excited":   "Scroll down to see all insights!",
        "worried":   "Let's find what's costing you",
        "surprised": "Look at these numbers!",
    }.get(emotion, "")

    return f"""
<div class="ruan-widget" title="Click to talk to Ruan">
    <div class="widget-header">
        <div class="widget-dot"></div>
        <span class="widget-name">{emoji} Ruan</span>
        <span class="widget-status">{status}</span>
    </div>
    <div class="widget-msg">{ruan_msg}</div>
    {f'<div class="owly-msg">🦉 {owly_message}</div>'
     if owly_message else ''}
</div>
"""
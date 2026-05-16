import streamlit as st
import streamlit.components.v1 as components
import time

def show_ruan_cinematic(emotion="happy", message="", owly_message=""):
    """Full cinematic Ruan + Owly experience"""

    emotions = {
        "happy": {
            "mouth": "M304 214 Q320 228 336 214",
            "browL": "M288 170 Q300 164 312 170",
            "browR": "M328 170 Q340 164 352 170",
            "color": "#EEEDFE",
            "ruanAnim": "float",
        },
        "thinking": {
            "mouth": "M308 218 Q320 218 332 218",
            "browL": "M288 172 Q300 168 312 173",
            "browR": "M328 168 Q340 172 352 173",
            "color": "#E6F1FB",
            "ruanAnim": "thinking",
        },
        "excited": {
            "mouth": "M300 212 Q320 232 340 212",
            "browL": "M288 166 Q300 160 312 166",
            "browR": "M328 166 Q340 160 352 166",
            "color": "#E1F5EE",
            "ruanAnim": "jump",
        },
        "worried": {
            "mouth": "M304 220 Q320 212 336 220",
            "browL": "M288 174 Q300 170 312 175",
            "browR": "M328 175 Q340 170 352 174",
            "color": "#FAEEDA",
            "ruanAnim": "float",
        },
        "surprised": {
            "mouth": "M310 216 Q320 224 330 216",
            "browL": "M288 164 Q300 158 312 165",
            "browR": "M328 165 Q340 158 352 164",
            "color": "#E1F5EE",
            "ruanAnim": "jump",
        }
    }

    e = emotions.get(emotion, emotions["happy"])

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    * {{ margin:0; padding:0; box-sizing:border-box; }}
    body {{ background:transparent; font-family:Arial,sans-serif; }}

    @keyframes float {{
        0%,100%{{transform:translateY(0px)}}
        50%{{transform:translateY(-10px)}}
    }}
    @keyframes jump {{
        0%,100%{{transform:translateY(0px) rotate(0deg)}}
        25%{{transform:translateY(-20px) rotate(-5deg)}}
        75%{{transform:translateY(-15px) rotate(5deg)}}
    }}
    @keyframes thinking {{
        0%,100%{{transform:translateY(0px) rotate(0deg)}}
        50%{{transform:translateY(-4px) rotate(3deg)}}
    }}
    @keyframes blink {{
        0%,88%,100%{{transform:scaleY(1)}}
        93%{{transform:scaleY(0.08)}}
    }}
    @keyframes screenflash1 {{
        0%,100%{{opacity:1}} 50%{{opacity:0.4}}
    }}
    @keyframes screenflash2 {{
        0%,100%{{opacity:1}} 40%{{opacity:0.5}}
    }}
    @keyframes screenflash3 {{
        0%,100%{{opacity:1}} 60%{{opacity:0.3}}
    }}
    @keyframes owlyfly {{
        0%{{transform:translate(0px,0px) rotate(0deg)}}
        25%{{transform:translate(-30px,-20px) rotate(-10deg)}}
        50%{{transform:translate(0px,-35px) rotate(0deg)}}
        75%{{transform:translate(30px,-20px) rotate(10deg)}}
        100%{{transform:translate(0px,0px) rotate(0deg)}}
    }}
    @keyframes owlywiggle {{
        0%,100%{{transform:rotate(-5deg)}}
        50%{{transform:rotate(5deg)}}
    }}
    @keyframes pulse {{
        0%,100%{{transform:scale(1)}}
        50%{{transform:scale(1.04)}}
    }}
    @keyframes fadein {{
        from{{opacity:0;transform:translateY(10px)}}
        to{{opacity:1;transform:translateY(0)}}
    }}
    @keyframes screenspin {{
        0%,100%{{opacity:1;transform:rotate(0deg)}}
        50%{{opacity:0.6;transform:rotate(3deg)}}
    }}

    .wrap {{
        background: linear-gradient(135deg,#F5F4FD 0%,#EEF5FF 100%);
        border-radius: 24px;
        padding: 20px 16px 16px;
        box-shadow: 0 4px 24px rgba(83,74,183,0.12);
        display: flex;
        flex-direction: column;
        align-items: center;
    }}

    .ruan-g {{
        animation: {e['ruanAnim']} 2.5s ease-in-out infinite;
    }}
    .eyes-g {{
        animation: blink 4s ease-in-out infinite;
        transform-origin: 320px 184px;
    }}
    .sc1 {{ animation: screenflash1 1.8s ease-in-out infinite; }}
    .sc2 {{ animation: screenflash2 2.2s ease-in-out infinite; }}
    .sc3 {{ animation: screenflash3 1.5s ease-in-out infinite; }}

    .owly-fly {{
        animation: owlyfly 4s ease-in-out infinite;
        transform-origin: 560px 270px;
    }}
    .owly-wiggle {{
        animation: owlywiggle 3s ease-in-out infinite;
        transform-origin: 560px 270px;
    }}

    .speech-ruan {{
        background: {e['color']};
        border-radius: 18px 18px 18px 4px;
        padding: 14px 20px;
        color: #3C3489;
        font-size: 15px;
        font-weight: 500;
        margin: 10px 0 6px;
        animation: fadein 0.5s ease-out, pulse 3s ease-in-out infinite;
        max-width: 500px;
        text-align: center;
        line-height: 1.5;
    }}

    .speech-owly {{
        background: #FAEEDA;
        border-radius: 18px 18px 4px 18px;
        padding: 12px 20px;
        color: #633806;
        font-size: 13px;
        font-weight: 500;
        margin: 4px 0 8px;
        animation: fadein 0.8s ease-out;
        max-width: 500px;
        text-align: center;
        line-height: 1.5;
    }}

    .chars {{
        display: flex;
        align-items: flex-end;
        justify-content: center;
        gap: 0px;
    }}
    </style>
    </head>
    <body>
    <div class="wrap">

    <div class="chars">
    <svg width="560" viewBox="0 0 680 420"
         xmlns="http://www.w3.org/2000/svg">

      <!-- ── RUAN ── -->
      <g class="ruan-g">
        <!-- Body -->
        <rect x="278" y="230" width="84" height="90"
              rx="20" fill="#FAC775"/>
        <rect x="278" y="248" width="84" height="8"
              rx="2" fill="#534AB7" opacity="0.3"/>
        <rect x="278" y="264" width="84" height="8"
              rx="2" fill="#534AB7" opacity="0.3"/>
        <rect x="278" y="280" width="84" height="8"
              rx="2" fill="#534AB7" opacity="0.2"/>
        <!-- Neck -->
        <rect x="307" y="214" width="26" height="22"
              rx="8" fill="#FAC775"/>
        <!-- Head -->
        <ellipse cx="320" cy="184" rx="52" ry="50"
                 fill="#FAC775"/>
        <!-- Hair -->
        <ellipse cx="320" cy="141" rx="50" ry="22"
                 fill="#2C2C2A"/>
        <ellipse cx="278" cy="161" rx="15" ry="21"
                 fill="#2C2C2A"/>
        <ellipse cx="362" cy="161" rx="15" ry="21"
                 fill="#2C2C2A"/>
        <ellipse cx="296" cy="147" rx="19" ry="15"
                 fill="#2C2C2A"/>
        <ellipse cx="344" cy="147" rx="19" ry="15"
                 fill="#2C2C2A"/>
        <!-- Ears -->
        <ellipse cx="269" cy="187" rx="10" ry="12"
                 fill="#FAC775"/>
        <ellipse cx="371" cy="187" rx="10" ry="12"
                 fill="#FAC775"/>
        <ellipse cx="269" cy="187" rx="6" ry="8"
                 fill="#EF9F27" opacity="0.3"/>
        <ellipse cx="371" cy="187" rx="6" ry="8"
                 fill="#EF9F27" opacity="0.3"/>
        <!-- Eyes -->
        <g class="eyes-g">
          <ellipse cx="300" cy="184" rx="13" ry="14"
                   fill="white"/>
          <ellipse cx="302" cy="185" rx="8" ry="9"
                   fill="#2C2C2A"/>
          <ellipse cx="305" cy="182" rx="3" ry="3"
                   fill="white"/>
          <ellipse cx="340" cy="184" rx="13" ry="14"
                   fill="white"/>
          <ellipse cx="342" cy="185" rx="8" ry="9"
                   fill="#2C2C2A"/>
          <ellipse cx="345" cy="182" rx="3" ry="3"
                   fill="white"/>
        </g>
        <!-- Eyebrows -->
        <path d="{e['browL']}" fill="none"
              stroke="#2C2C2A" stroke-width="3"
              stroke-linecap="round"/>
        <path d="{e['browR']}" fill="none"
              stroke="#2C2C2A" stroke-width="3"
              stroke-linecap="round"/>
        <!-- Nose -->
        <ellipse cx="320" cy="200" rx="5" ry="4"
                 fill="#EF9F27" opacity="0.45"/>
        <!-- Mouth -->
        <path d="{e['mouth']}" fill="none"
              stroke="#2C2C2A" stroke-width="3"
              stroke-linecap="round"/>
        <!-- Cheeks -->
        <ellipse cx="282" cy="206" rx="12" ry="8"
                 fill="#F0997B" opacity="0.4"/>
        <ellipse cx="358" cy="206" rx="12" ry="8"
                 fill="#F0997B" opacity="0.4"/>
        <!-- Arms -->
        <rect x="232" y="234" width="50" height="18"
              rx="9" fill="#FAC775"
              transform="rotate(20 257 243)"/>
        <rect x="358" y="234" width="50" height="18"
              rx="9" fill="#FAC775"
              transform="rotate(-20 383 243)"/>
        <!-- Hands -->
        <circle cx="224" cy="256" r="10" fill="#FAC775"/>
        <circle cx="416" cy="256" r="10" fill="#FAC775"/>
        <!-- Legs -->
        <rect x="288" y="314" width="26" height="52"
              rx="12" fill="#534AB7"/>
        <rect x="326" y="314" width="26" height="52"
              rx="12" fill="#534AB7"/>
        <!-- Shoes -->
        <ellipse cx="301" cy="365" rx="20" ry="10"
                 fill="#2C2C2A"/>
        <ellipse cx="339" cy="365" rx="20" ry="10"
                 fill="#2C2C2A"/>

        <!-- Data screens -->
        <g class="sc1">
          <rect x="144" y="156" width="84" height="60"
                rx="8" fill="#E6F1FB"
                stroke="#378ADD" stroke-width="1.2"/>
          <rect x="150" y="164" width="30" height="4"
                rx="2" fill="#378ADD" opacity="0.6"/>
          <rect x="152" y="202" width="8" height="10"
                rx="1" fill="#534AB7"/>
          <rect x="163" y="195" width="8" height="17"
                rx="1" fill="#1D9E75"/>
          <rect x="174" y="198" width="8" height="14"
                rx="1" fill="#BA7517"/>
          <rect x="185" y="191" width="8" height="21"
                rx="1" fill="#534AB7"/>
          <line x1="228" y1="186" x2="268" y2="210"
                stroke="#7F77DD" stroke-width="1"
                stroke-dasharray="4,3" opacity="0.5"/>
        </g>
        <g class="sc2">
          <rect x="266" y="64" width="108" height="64"
                rx="8" fill="#E1F5EE"
                stroke="#1D9E75" stroke-width="1.2"/>
          <polyline
            points="274,112 290,104 306,110 322,96 338,90 354,94"
            fill="none" stroke="#1D9E75" stroke-width="2"
            stroke-linecap="round"/>
          <line x1="320" y1="128" x2="320" y2="136"
                stroke="#1D9E75" stroke-width="1"
                stroke-dasharray="4,3" opacity="0.5"/>
        </g>
        <g class="sc3">
          <rect x="408" y="146" width="84" height="60"
                rx="8" fill="#FAEEDA"
                stroke="#BA7517" stroke-width="1.2"/>
          <circle cx="450" cy="186" r="17" fill="#EF9F27"/>
          <path d="M450 186 L450 169 A17 17 0 0 1 465 195 Z"
                fill="#534AB7"/>
          <path d="M450 186 L465 195 A17 17 0 0 1 436 200 Z"
                fill="#1D9E75"/>
          <line x1="412" y1="176" x2="378" y2="210"
                stroke="#7F77DD" stroke-width="1"
                stroke-dasharray="4,3" opacity="0.5"/>
        </g>

        <!-- Name tag -->
        <rect x="282" y="380" width="76" height="24"
              rx="12" fill="#EEEDFE"
              stroke="#7F77DD" stroke-width="0.8"/>
        <text x="320" y="396" font-size="12"
              font-weight="bold" fill="#3C3489"
              font-family="Arial"
              text-anchor="middle">Ruan</text>
      </g>

      <!-- ── OWLY ── -->
      <g class="{
        'owly-fly' if emotion in ['excited','surprised']
        else 'owly-wiggle'
      }">
        <ellipse cx="560" cy="282" rx="28" ry="34"
                 fill="#BA7517"/>
        <ellipse cx="560" cy="290" rx="18" ry="22"
                 fill="#FAEEDA"/>
        <ellipse cx="560" cy="250" rx="26" ry="24"
                 fill="#BA7517"/>
        <polygon points="546,230 550,211 556,230"
                 fill="#854F0B"/>
        <polygon points="564,230 570,211 574,230"
                 fill="#854F0B"/>
        <ellipse cx="551" cy="250" rx="10" ry="10"
                 fill="white"/>
        <ellipse cx="569" cy="250" rx="10" ry="10"
                 fill="white"/>
        <ellipse cx="552" cy="251" rx="6" ry="6"
                 fill="#2C2C2A"/>
        <ellipse cx="570" cy="251" rx="6" ry="6"
                 fill="#2C2C2A"/>
        <ellipse cx="553" cy="249" rx="2" ry="2"
                 fill="white"/>
        <ellipse cx="571" cy="249" rx="2" ry="2"
                 fill="white"/>
        <polygon points="560,258 555,265 565,265"
                 fill="#EF9F27"/>
        <ellipse cx="532" cy="280" rx="14" ry="22"
                 fill="#854F0B"
                 transform="rotate(-15 532 280)"/>
        <ellipse cx="588" cy="280" rx="14" ry="22"
                 fill="#854F0B"
                 transform="rotate(15 588 280)"/>
        <ellipse cx="551" cy="315" rx="10" ry="5"
                 fill="#EF9F27"/>
        <ellipse cx="569" cy="315" rx="10" ry="5"
                 fill="#EF9F27"/>
        <rect x="590" y="260" width="38" height="28"
              rx="4" fill="#EEEDFE"
              stroke="#7F77DD" stroke-width="0.8"/>
        <rect x="594" y="265" width="15" height="2"
              rx="1" fill="#534AB7" opacity="0.6"/>
        <rect x="594" y="270" width="11" height="2"
              rx="1" fill="#534AB7" opacity="0.4"/>
        <rect x="594" y="275" width="13" height="2"
              rx="1" fill="#1D9E75" opacity="0.5"/>
        <text x="560" y="334" font-size="11"
              fill="#633806" font-family="Arial"
              text-anchor="middle">Owly</text>
      </g>

    </svg>
    </div>

    <!-- Ruan speech bubble -->
    {f'<div class="speech-ruan">🤖 {message}</div>' if message else ''}

    <!-- Owly speech bubble -->
    {f'<div class="speech-owly">🦉 {owly_message}</div>' if owly_message else ''}

    </div>
    </body>
    </html>
    """
    components.html(html, height=520)


def show_ruan_storytelling(insights, business, city):
    """
    Owly flies around data and explains
    insights one by one like a story
    """

    # Step 1 — excited upload
    placeholder = st.empty()
    with placeholder.container():
        show_ruan_cinematic(
            emotion="excited",
            message=f"Ooh data! Let me look! 👀",
            owly_message="I found your records! Reading them now..."
        )
    time.sleep(2)

    # Step 2 — thinking
    with placeholder.container():
        show_ruan_cinematic(
            emotion="thinking",
            message="Hmm let me check your numbers carefully... 🤔",
            owly_message=f"Scanning {insights.get('total_orders',0):,} records..."
        )
    time.sleep(2)

    # Step 3 — revenue reveal
    with placeholder.container():
        show_ruan_cinematic(
            emotion="surprised",
            message=f"Wow! Your total sales are "
                    f"₹{insights.get('total_revenue',0):,.0f}! 💰",
            owly_message="Now let me check if that's actually profitable..."
        )
    time.sleep(2)

    # Step 4 — profit reveal
    profit = insights.get('total_profit', 0)
    if profit > 0:
        with placeholder.container():
            show_ruan_cinematic(
                emotion="excited",
                message=f"Great news! You made ₹{profit:,.0f} profit! 🎉",
                owly_message=f"Profit margin is "
                             f"{insights.get('profit_margin',0)}% "
                             f"— let me check if that's healthy for "
                             f"{business} in {city}..."
            )
    else:
        with placeholder.container():
            show_ruan_cinematic(
                emotion="worried",
                message=f"Hmm... you have a loss of "
                        f"₹{abs(profit):,.0f} 😟 "
                        f"Don't worry — let's find why!",
                owly_message="I will find what is costing you money..."
            )
    time.sleep(2)

    # Step 5 — best product
    with placeholder.container():
        show_ruan_cinematic(
            emotion="excited",
            message=f"⭐ Your best product is "
                    f"{insights.get('best_product','N/A')}! "
                    f"It made ₹"
                    f"{insights.get('best_product_profit',0):,.0f}!",
            owly_message=f"Focus more on this product. "
                         f"It is your biggest money maker!"
        )
    time.sleep(2)

    # Step 6 — warning
    loss_orders = insights.get('loss_orders', 0)
    if loss_orders > 0:
        with placeholder.container():
            show_ruan_cinematic(
                emotion="worried",
                message=f"⚠️ Watch out! {loss_orders} orders "
                        f"are losing money!",
                owly_message="Review your pricing on these orders immediately."
            )
        time.sleep(2)

    # Step 7 — best day
    with placeholder.container():
        show_ruan_cinematic(
            emotion="happy",
            message=f"📅 Your best day is "
                    f"{insights.get('best_day','N/A')}! "
                    f"Make sure you are fully stocked!",
            owly_message=f"Worst day is "
                         f"{insights.get('worst_day','N/A')} "
                         f"— consider special offers that day."
        )
    time.sleep(2)

    # Step 8 — final
    with placeholder.container():
        show_ruan_cinematic(
            emotion="excited",
            message="That's everything I found! "
                    "Ask me anything below! 🎉",
            owly_message="Full analysis ready. "
                         "Scroll down to see all details!"
        )
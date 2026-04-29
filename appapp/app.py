import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - להעלים הכל ולהשאיר נקי
st.set_page_config(page_title="העושר שלי", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת עיצוב "רך ויוקרתי" (Soft UI) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;600;700&display=swap');
    
    /* הגדרות כלליות - הכל עגול ורך */
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }
    .stApp { background: #F9F7FF; } /* רקע סגלגל פנינה */
    
    /* כרטיסיות (Cards) - בועות לבנות */
    .stMetric, .main-card, [data-testid="stExpander"] {
        background: white !important;
        border-radius: 30px !important;
        border: none !important;
        box-shadow: 0 10px 30px rgba(108, 99, 255, 0.08) !important;
        padding: 20px !important;
        margin-bottom: 15px !important;
    }
    
    /* טקסטים - שחור ברור במקום אפור בהיר */
    h1, h2, h3, p, span, label { color: #2D3748 !important; font-weight: 600 !important; }
    .stMetric [data-testid="stMetricValue"] { color: #6C63FF !important; font-size: 32px !important; font-weight: 700 !important; }
    
    /* כפתור הפלוס - ענקי וצף */
    .stButton>button {
        background: linear-gradient(135deg, #6C63FF 0%, #38B2AC 100%) !important;
        color: white !important;
        border-radius: 50px !important; /* עגול לגמרי */
        border: none !important;
        height: 60px !important;
        font-size: 20px !important;
        font-weight: 700 !important;
        box-shadow: 0 10px 20px rgba(108, 99, 255, 0.3) !important;
        transition: 0.3s !important;
    }
    .stButton>button:hover { transform: scale(1.05); }

    /* אייקונים בתחתית */
    .icon-box {
        background: white;
        border-radius: 25px;
        padding: 20px;
        text-align: center;
        transition: 0.3s;
        border: 2px solid #F0EBFF;
    }
    .icon-box:hover { background: #F1F0FF; transform: translateY(-5px); border-color: #6C63FF; }

    /* הסרת אלמנטים מיותרים של המערכת */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- כותרת ראשית מעוצבת ---
st.markdown('<h1 style="text-align: center; color: #4A3AFF; font-size: 45px;">העושר שלי ✨</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 18px;">ברוכה הבאה, רחלי! בואי נראה את השפע שלך.</p>', unsafe_allow_html=True)

# --- דשבורד כסף (Metrics) ---
col1, col2, col3 = st.columns(3)
with col1: st.metric("מזומן (Cash) 💵", "$2,450")
with col2: st.metric("בנק (BofA) 🏦", "$4,100")
with col3: st.metric("אשראי (Amex) 💳", "$1,200-")

# --- יעד החיסכון ($20,000) ---
st.markdown("### 🎯 הדרך אל ה-$20,000")
st.progress(5800/20000)
st.write(f"נחסכו עד כה: **$5,800** | נותרו עוד **{14} ימים** לסבב")

st.markdown("<br>", unsafe_allow_html=True)

# --- כפתור הפלוס - עכשיו הוא בולט ומרכזי ---
st.markdown("### 📝 להוסיף תנועה חדשה")
with st.expander("לחצי כאן לפתיחת טופס הכנסה/הוצאה", expanded=True):
    mode = st.radio("מה קרה עכשיו?", ["הוצאה 💸", "הכנסה 💰"], horizontal=True)
    
    c1, c2 = st.columns(2)
    with c1:
        wallet = st.selectbox("איך שילמת/קיבלת?", ["מזומן 💵", "Bank of America 🏦", "American Express 💳", "Food Stamps 🍎", "Pepper 🌶️"])
        amount = st.number_input("סכום ($)", min_value=0.0, step=10.0)
    with c2:
        date = st.date_input("מתי זה קרה?", datetime.now())
        if "הוצאה" in mode:
            cat = st.selectbox("קטגוריה", ["צדקה ❤️", "רכב 🚗", "מזון 🥗", "דירה 🏠", "כללי 📦"])
        else:
            cat = st.selectbox("מקור", ["משכורת ישראל 🇮🇱", "משכורת רחלי 👩‍💻", "כללי ישראל 👴", "עצמאי רחלי ✍️", "כללי רחלי 🌍"])
    
    note = st.text_input("פירוט קצר (למשל: 'קניות בשבת', 'בונוס')")
    
    if st.button("שמור עכשיו! ✨"):
        st.balloons()
        st.success("איזה יופי! הנתון נשמר בבטחה.")

st.markdown("<br>---<br>", unsafe_allow_html=True)

# --- פירוט אייקונים (החלק שביקשת בתחתית) ---
st.markdown("### 🔍 פירוט לפי קטגוריות")
st.write("לחצי על אייקון לראות היסטוריה:")

st.markdown("#### הוצאות")
row1 = st.columns(5)
cats = [("🚗", "רכב"), ("🥗", "מזון"), ("❤️", "צדקה"), ("🏠", "דירה"), ("📦", "כללי")]
for i, (icon, name) in enumerate(cats):
    with row1[i]:
        st.markdown(f'<div class="icon-box"><div style="font-size:35px;">{icon}</div><div style="font-size:16px; font-weight:700;">{name}</div></div>', unsafe_allow_html=True)

st.markdown("<br>#### הכנסות")
row2 = st.columns(5)
inc_cats = [("🇮🇱", "IL"), ("👩‍💻", "רחלי"), ("🌍", "כללי ר"), ("👴", "ישראל"), ("💼", "כללי IL")]
for i, (icon, name) in enumerate(inc_cats):
    with row2[i]:
        st.markdown(f'<div class="icon-box"><div style="font-size:35px;">{icon}</div><div style="font-size:16px; font-weight:700;">{name}</div></div>', unsafe_allow_html=True)

# --- תפריט צד (Sidebar) ---
with st.sidebar:
    st.markdown("## ⚙️ הגדרות")
    st.number_input("עדכון יעד חיסכון ($)", value=20000)
    st.markdown("---")
    st.subheader("🤖 הבוט של רחלי")
    st.info("אל תשכחי שיש לך הרבה מזומן! כדאי לעשות Swap.")

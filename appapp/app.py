import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - נקי ומותאם למובייל
st.set_page_config(page_title="העושר של רחלי", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת עיצוב "רך, עגול וטורקיזי" (Soft Mint UI) ---
# אנחנו משתמשים בפקודות 'important' כדי להכריח את המערכת להשתמש בעיצוב שלנו
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;600;700&display=swap');
    
    /* הגדרות כלליות - פונט נעים ועברית */
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }
    
    /* 1. רקע האפליקציה - מנטה רך (במקום לבן בוהק) */
    .stApp { background-color: #E6FFFA !important; }
    
    /* 2. כרטיסיות הנתונים (Metrics) - לבנות ועגולות מאוד */
    div[data-testid="stMetric"] {
        background-color: white !important;
        border-radius: 30px !important; /* פינות עגולות */
        padding: 20px !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.03) !important; /* צל עדין */
        border: 1px solid #B2F5EA !important; /* מסגרת טורקיז עדינה */
    }
    
    /* 3. טקסטים כהים וברורים בתוך הכרטיסיות */
    div[data-testid="stMetricLabel"] > div { color: #2D3748 !important; font-weight: 600 !important; font-size: 16px !important; }
    div[data-testid="stMetricValue"] > div { color: #2C7A7B !important; font-size: 35px !important; font-weight: 700 !important; }
    
    /* 4. כפתור הפלוס הצף (FAB) - טורקיז, עגול וממריץ */
    .fab-container {
        position: fixed;
        bottom: 30px;
        right: 30px;
        z-index: 1000;
    }
    .stButton>button {
        background: linear-gradient(135deg, #38B2AC 0%, #319795 100%) !important;
        color: white !important;
        border-radius: 50% !important; /* עגול לגמרי */
        width: 70px !important;
        height: 70px !important;
        font-size: 35px !important;
        box-shadow: 0 10px 25px rgba(49, 151, 149, 0.4) !important;
        border: none !important;
        transition: 0.3s !important;
    }
    .stButton>button:hover { transform: scale(1.1); box-shadow: 0 15px 30px rgba(49, 151, 149, 0.5) !important; }

    /* 5. אייקונים בתחתית - עיצוב מעוגל ונעים */
    .icon-box {
        background: white;
        border-radius: 25px;
        padding: 20px;
        text-align: center;
        border: 2px solid #81E6D9;
        transition: 0.3s;
    }
    .icon-box:hover { background: #F0FFF4; transform: translateY(-5px); border-color: #38B2AC; }

    /* הסרת כותרות ברירת מחדל מיותרות */
    #rachel-s-wealth { display: none; }
    header, footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- כותרת ראשית מעוצבת ---
st.markdown('<h1 style="color: #2C7A7B; text-align: center; font-size: 45px; margin-bottom: 0;">העושר שלי ✨</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #2D3748; text-align: center; font-size: 18px;">ברוכה הבאה, רחלי! בואי נראה את השפע שלך.</p>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# --- דשבורד כסף (Metrics) - עכשיו זה יופיע בתוך כרטיסיות עגולות ---
col1, col2, col3 = st.columns(3)
with col1: st.metric("מזומן (Cash) 💵", "$2,450")
with col2: st.metric("בנק (BofA) 🏦", "$4,100")
with col3: st.metric("אשראי (Amex) 💳", "$1,200-")

# --- יעד החיסכון הגדול ---
st.markdown("<br>### 🎯 הדרך אל ה-$20,000", unsafe_allow_html=True)
st.progress(5800/20000)
st.write(f"נחסכו עד כה: **$5,800** | נותרו עוד **10 ימים** לסבב")

st.markdown("<br>---<br>", unsafe_allow_html=True)

# --- עוגות נתונים להשוואה ---
st.markdown("### 📊 השוואת הוצאות שבועית", unsafe_allow_html=True)
col_g1, col_g2 = st.columns(2)
with col_g1:
    df1 = pd.DataFrame({'קטגוריה': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'סכום': [800, 300, 750, 1200, 250]})
    fig1 = px.pie(df1, values='סכום', names='קטגוריה', hole=0.6, title="הוצאות הסבב", color_discrete_sequence=px.colors.qualitative.Mint)
    st.plotly_chart(fig1, use_container_width=True)
with col_g2:
    df2 = pd.DataFrame({'קטגוריה': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'סכום': [1500, 500, 1500, 1200, 400]})
    fig2 = px.pie(df2, values='סכום', names='קטגוריה', hole=0.6, title="ממוצע היסטורי", color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig2, use_container_width=True)

# --- כפתור הפלוס הצף (FAB) להוספה - בצד ימין למטה ---
st.markdown('<div class="fab-container">', unsafe_allow_html=True)
with st.expander("➕ הוספת תנועה חדשה", expanded=False):
    st.markdown('<div style="background: white; padding: 20px; border-radius: 20px; border: 1px solid #B2F5EA;">', unsafe_allow_html=True)
    t_mode = st.radio("סוג", ["הוצאה 💸", "הכנסה 💰"], horizontal=True)
    
    c1, c2 = st.columns(2)
    with c1:
        t_wallet = st.selectbox("איך שילמת/קיבלת?", ["מזומן 💵", "Bank of America 🏦", "American Express 💳", "Food Stamps 🍎", "Pepper 🌶️"])
        t_amount = st.number_input("סכום ($)", min_value=0.0)
    with c2:
        t_date = st.date_input("מתי?", datetime.now())
        if "הוצאה" in t_mode:
            t_cat = st.selectbox("קטגוריה", ["צדקה ❤️", "רכב 🚗", "מזון 🥗", "דירה 🏠", "כללי 📦"])
        else:
            t_cat = st.selectbox("מקור", ["משכורת ישראל 🇮🇱", "משכורת רחלי 👩‍💻", "כללי ישראל 👴", "עצמאי רחלי ✍️", "כללי רחלי 🌍"])
    
    if st.button("שמור עכשיו! ✨"):
        st.balloons()
        st.success("נשמר בבטחה!")
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- פירוט אייקונים (החלק שביקשת בתחתית) ---
st.markdown("<br>---<br>", unsafe_allow_html=True)
st.markdown("### 📂 פירוט לפי קטגוריות", unsafe_allow_html=True)
st.write("לחצי על אייקון לראות היסטוריה:")

st.markdown("#### הוצאות")
row1 = st.columns(5)
cats = [("🚗", "רכב"), ("🥗", "מזון"), ("❤️", "צדקה"), ("🏠", "דירה"), ("📦", "כללי")]
for i, (icon, name) in enumerate(cats):
    with row1[i]:
        st.markdown(f'<div class="icon-box"><div style="font-size:35px;">{icon}</div><div style="font-size:16px; font-weight:700; color: #2D3748;">{name}</div></div>', unsafe_allow_html=True)

# --- תפריט צד (Sidebar) מעוצב ---
with st.sidebar:
    st.markdown('<h2 style="color: #2C7A7B; text-align: right;">⚙️ הגדרות</h2>', unsafe_allow_html=True)
    st.number_input("עדכון יעד חיסכון ($)", value=20000)
    st.markdown("---")
    st.subheader("🤖 בוט AI")
    st.info("רחלי, אל תשכחי לעשות Swap למזומן השבוע!")

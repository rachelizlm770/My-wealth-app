import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - ניקוי מקסימלי
st.set_page_config(page_title="Rachel's Wealth", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת עיצוב "Luxury Minimalist" - ללא פסים ועם כפתור עובד ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* 1. מחיקת הפס הצידי והדרכים של המערכת */
    [data-testid="stSidebar"], [data-testid="stHeader"], .css-1rs6os, .st-emotion-cache-16idsys { display: none !important; }
    .block-container { padding-top: 1rem !important; max-width: 95% !important; }
    
    /* 2. רקע פנינה נקי */
    .stApp { background-color: #FFFFFF !important; }
    
    /* 3. פונט ויישור */
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }
    
    /* 4. כרטיסיות נתונים - עיצוב בוגר */
    div[data-testid="stMetric"] {
        background-color: #FDFDFF !important;
        border-radius: 20px !important;
        padding: 25px !important;
        border: 1px solid #EAEAF2 !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.02) !important;
        border-right: 5px solid #5A52CB !important;
    }
    
    /* 5. צבעי טקסט ברורים */
    h1, h2, h3, p, span, label { color: #1A1A2E !important; font-weight: 600 !important; }
    div[data-testid="stMetricValue"] > div { color: #4A3AFF !important; font-size: 36px !important; font-weight: 700 !important; }
    
    /* 6. כפתור פלוס צף יוקרתי */
    .fab-button {
        position: fixed;
        bottom: 30px;
        left: 30px;
        width: 65px;
        height: 65px;
        background: #4A3AFF;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white !important;
        font-size: 32px;
        box-shadow: 0 8px 25px rgba(74, 58, 255, 0.4);
        z-index: 9999;
        text-decoration: none !important;
        transition: 0.3s;
    }
    .fab-button:hover { transform: scale(1.1); background: #3A2ADF; }

    /* 7. אייקונים בוגרים (Minimalist) */
    .cat-box {
        background: #F9F9FB;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        border: 1px solid #F0F0F5;
    }
    .cat-label { color: #5A52CB; font-size: 14px; font-weight: 700; margin-top: 8px; }
    .cat-symbol { color: #A0A0C0; font-size: 22px; }

    /* הסתרת כפתורי מערכת */
    #MainMenu, footer { visibility: hidden; }
    </style>
    
    <a href="#register" class="fab-button">+</a>
    """, unsafe_allow_html=True)

# --- כותרת ---
st.markdown('<h1 style="text-align: center; font-size: 34px; color: #1A1A2E;">Wealth Management</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #716B94; font-size: 14px; margin-top: -15px;">ניהול נכסים אישי | רחלי</p>', unsafe_allow_html=True)

# --- דשבורד כסף ---
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: st.metric("Cash", "$2,450")
with c2: st.metric("BofA", "$4,100")
with c3: st.metric("Amex", "$1,200-")

# מד התקדמות
st.markdown("<br>", unsafe_allow_html=True)
st.progress(5800/20000)
st.markdown('<p style="font-size: 13px; color: #716B94;">סטטוס חיסכון: <b>$5,800</b> מתוך <b>$20,000</b></p>', unsafe_allow_html=True)

st.markdown("<br><hr style='border: 0.1px solid #EEE;'><br>", unsafe_allow_html=True)

# --- עוגות נתונים ---
col_g1, col_g2 = st.columns(2)
with col_g1:
    df1 = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
    fig1 = px.pie(df1, values='Val', names='Cat', hole=0.8, title="פירוט הוצאות סבב")
    fig1.update_traces(marker=dict(colors=['#4A3AFF', '#6C63FF', '#8E86FF', '#B0AAFF', '#D2CFFF']), textinfo='none')
    fig1.update_layout(showlegend=True, margin=dict(t=30, b=0, l=0, r=0), font=dict(family="Assistant", size=12))
    st.plotly_chart(fig1, use_container_width=True)

with col_g2:
    df2 = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [1500, 500, 1500, 1200, 400]})
    fig2 = px.pie(df2, values='Val', names='Cat', hole=0.8, title="ממוצע תקופתי")
    fig2.update_traces(marker=dict(colors=['#D2CFFF', '#B0AAFF', '#8E86FF', '#6C63FF', '#4A3AFF']), textinfo='none')
    fig2.update_layout(showlegend=True, margin=dict(t=30, b=0, l=0, r=0), font=dict(family="Assistant", size=12))
    st.plotly_chart(fig2, use_container_width=True)

# --- טופס רישום (הפלוס הצף מקפיץ לכאן) ---
st.markdown('<div id="register"></div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
with st.expander("📝 רישום תנועה חדשה", expanded=False):
    t_mode = st.radio("סוג פעולה", ["הוצאה", "הכנסה"], horizontal=True)
    ca, cb = st.columns(2)
    with ca:
        t_wallet = st.selectbox("חשבון", ["מזומן", "BofA", "Amex", "Food Stamps", "Pepper"])
        t_amount = st.number_input("סכום", min_value=0.0)
    with cb:
        t_date = st.date_input("תאריך", datetime.now())
        if t_mode == "הוצאה":
            t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
        else:
            t_cat = st.selectbox("מקור", ["משכורת ישראל", "משכורת רחלי", "עצמאי", "כללי"])
    
    if st.button("אישור רישום"):
        st.success("הנתון נרשם במערכת.")

# --- אייקונים בוגרים (Minimalist) ---
st.markdown("<br>### ניתוח קטגוריות", unsafe_allow_html=True)
row_icons = st.columns(5)
# שימוש בסמלים גרפיים במקום אימוג'ים צבעוניים
cats_minimal = [("○", "רכב"), ("◇", "מזון"), ("♡", "צדקה"), ("□", "דירה"), ("△", "כללי")]

for i, (symbol, name) in enumerate(cats_minimal):
    with row_icons[i]:
        st.markdown(f'''
            <div class="cat-box">
                <div class="cat-symbol">{symbol}</div>
                <div class="cat-label">{name}</div>
            </div>
        ''', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

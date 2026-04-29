import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף
st.set_page_config(page_title="Rachel's Wealth", layout="wide", initial_sidebar_state="expanded")

# --- הזרקת עיצוב Luxury Minimalist - פלוס צף ותפריט נקי ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* 1. רקע לבן וניקיון כללי */
    .stApp { background-color: #FFFFFF !important; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    .block-container { padding-top: 1rem !important; }
    
    /* הסרת הפס המפריד המציק באמצע */
    .st-emotion-cache-16idsys, .st-emotion-cache-6q9sum { display: none !important; }

    /* 2. פונט ויישור */
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }
    
    /* 3. כרטיסיות נתונים - עיצוב בוגר */
    div[data-testid="stMetric"] {
        background-color: #FDFDFF !important;
        border-radius: 20px !important;
        padding: 25px !important;
        border: 1px solid #EAEAF2 !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.02) !important;
        border-right: 5px solid #4A3AFF !important;
    }
    
    /* 4. צבעי טקסט */
    h1, h2, h3, p, span, label { color: #1A1A2E !important; font-weight: 600 !important; }
    div[data-testid="stMetricValue"] > div { color: #4A3AFF !important; font-size: 34px !important; font-weight: 700 !important; }
    
    /* 5. כפתור פלוס צף (FAB) */
    .stButton > button {
        position: fixed !important;
        bottom: 30px !important;
        left: 30px !important;
        width: 70px !important;
        height: 70px !important;
        background: #4A3AFF !important;
        color: white !important;
        border-radius: 50% !important;
        font-size: 40px !important;
        box-shadow: 0 10px 25px rgba(74, 58, 255, 0.4) !important;
        border: 2px solid white !important;
        z-index: 99999 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        transition: 0.3s !important;
    }

    /* 6. אייקונים בוגרים בתחתית */
    .cat-box {
        background: #F9F9FB;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        border: 1px solid #F0F0F5;
    }
    .cat-label { color: #5A52CB; font-size: 14px; font-weight: 700; margin-top: 8px; }
    .cat-symbol { color: #A0A0C0; font-size: 22px; letter-spacing: 2px; }

    /* עיצוב תפריט הצד */
    [data-testid="stSidebar"] { background-color: #FBFBFF !important; border-left: 1px solid #EEE !important; }
    </style>
    """, unsafe_allow_html=True)

# --- לוגיקת מצב למסך ההוספה ---
if 'show_form' not in st.session_state:
    st.session_state.show_form = False

def toggle_form():
    st.session_state.show_form = not st.session_state.show_form

# --- כותרת ---
st.markdown('<h1 style="text-align: center; font-size: 32px; color: #1A1A2E;">Wealth Management</h1>', unsafe_allow_html=True)
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

# --- גרפים ---
st.markdown("<br>", unsafe_allow_html=True)
col_g1, col_g2 = st.columns(2)
with col_g1:
    df1 = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
    fig1 = px.pie(df1, values='Val', names='Cat', hole=0.8, title="סבב נוכחי")
    fig1.update_traces(marker=dict(colors=['#4A3AFF', '#6C63FF', '#8E86FF', '#B0AAFF', '#D2CFFF']), textinfo='none')
    fig1.update_layout(showlegend=True, margin=dict(t=30, b=0, l=0, r=0))
    st.plotly_chart(fig1, use_container_width=True)

with col_g2:
    df2 = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [1500, 500, 1500, 1200, 400]})
    fig2 = px.pie(df2, values='Val', names='Cat', hole=0.8, title="ממוצע תקופתי")
    fig2.update_traces(marker=dict(colors=['#D2CFFF', '#B0AAFF', '#8E86FF', '#6C63FF', '#4A3AFF']), textinfo='none')
    fig2.update_layout(showlegend=True, margin=dict(t=30, b=0, l=0, r=0))
    st.plotly_chart(fig2, use_container_width=True)

# --- כפתור הפלוס הצף (באמת עובד עכשיו) ---
if st.button("+"):
    toggle_form()

# --- עמוד/חלון הוספת תנועה (מופיע רק כשלוחצים על הפלוס) ---
if st.session_state.show_form:
    st.markdown("---")
    st.subheader("📝 רישום תנועה חדשה")
    with st.container():
        t_mode = st.radio("סוג", ["הוצאה", "הכנסה"], horizontal=True)
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
        
        if st.button("אישור ושמירה"):
            st.balloons()
            st.success("הנתון נרשם!")
            st.session_state.show_form = False
            st.rerun()
    st.markdown("---")

# --- אייקונים בוגרים בתחתית ---
st.markdown("### ניתוח קטגוריות", unsafe_allow_html=True)
row_icons = st.columns(5)
cats_minimal = [("CAR", "רכב"), ("FOOD", "מזון"), ("GIVE", "צדקה"), ("HOME", "דירה"), ("MISC", "כללי")]

for i, (symbol, name) in enumerate(cats_minimal):
    with row_icons[i]:
        st.markdown(f'<div class="cat-box"><div class="cat-symbol">{symbol}</div><div class="cat-label">{name}</div></div>', unsafe_allow_html=True)

# --- תפריט צד (Sidebar) - החזרנו אותו! ---
with st.sidebar:
    st.title("⚙️ הגדרות")
    st.number_input("עדכון יעד חיסכון", value=20000)
    st.markdown("---")
    st.subheader("📜 ארכיון")
    if st.button("לצפייה בהיסטוריה המלאה"):
        st.write("כאן תופיע הטבלה בעתיד")
    st.markdown("---")
    st.subheader("🤖 בוט AI")
    st.info("רחלי, הכל נראה תקין. אל תשכחי לבצע Swap למזומן.")

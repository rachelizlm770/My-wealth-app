import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף
st.set_page_config(page_title="Rachel's Wealth", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת עיצוב "Clean Luxury" - מחיקת קווים וטופס נסתר ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* 1. מחיקת קווים, פסים ושאריות מערכת */
    .st-emotion-cache-16idsys, .st-emotion-cache-6q9sum, .st-emotion-cache-z5fcl4 { display: none !important; }
    [data-testid="stHeader"] { background: transparent !important; }
    .block-container { padding-top: 1rem !important; max-width: 95% !important; }
    hr { border: 0.1px solid #F0F0F5 !important; opacity: 0.3; }

    /* 2. רקע לבן צחור */
    .stApp { background-color: #FFFFFF !important; }
    
    /* 3. פונט ויישור */
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }
    
    /* 4. כרטיסיות נתונים בוגרות */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border-radius: 15px !important;
        padding: 25px !important;
        border: 1px solid #F0F0F5 !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.02) !important;
        border-right: 5px solid #4A3AFF !important;
    }
    
    /* 5. צבעי טקסט */
    h1, h2, h3, p, span, label { color: #1F1F2F !important; font-weight: 600 !important; }
    div[data-testid="stMetricValue"] > div { color: #4A3AFF !important; font-size: 34px !important; font-weight: 700 !important; }
    
    /* 6. כפתור פלוס צף יוקרתי (FAB) */
    div.stButton > button:first-child {
        position: fixed !important;
        bottom: 30px !important;
        left: 30px !important;
        width: 65px !important;
        height: 65px !important;
        background: #4A3AFF !important;
        color: white !important;
        border-radius: 50% !important;
        font-size: 35px !important;
        box-shadow: 0 10px 30px rgba(74, 58, 255, 0.4) !important;
        border: 2px solid white !important;
        z-index: 99999 !important;
        transition: 0.3s !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* 7. אייקונים בוגרים בתחתית */
    .cat-box {
        background: #FDFDFF;
        border-radius: 12px;
        padding: 18px;
        text-align: center;
        border: 1px solid #F0F0F5;
    }
    .cat-label { color: #5A52CB; font-size: 13px; font-weight: 700; margin-top: 5px; }
    .cat-symbol { color: #B0B0D0; font-size: 18px; letter-spacing: 1px; }

    /* עיצוב תפריט הצד */
    [data-testid="stSidebar"] { background-color: #FBFBFF !important; }
    </style>
    """, unsafe_allow_html=True)

# --- ניהול מצב (האם להציג את הטופס?) ---
if 'adding' not in st.session_state:
    st.session_state.adding = False

def open_form():
    st.session_state.adding = True

# --- כותרת ---
st.markdown('<h1 style="text-align: center; font-size: 30px; color: #1A1A2E;">Wealth Management</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #716B94; font-size: 14px; margin-top: -15px;">Asset Tracking | רחלי</p>', unsafe_allow_html=True)

# --- דשבורד כסף ---
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: st.metric("Cash", "$2,450")
with c2: st.metric("BofA", "$4,100")
with c3: st.metric("Amex", "$1,200-")

# מד התקדמות
st.markdown("<br>", unsafe_allow_html=True)
st.progress(5800/20000)
st.markdown('<p style="font-size: 13px; color: #716B94;">סטטוס יעד: <b>$5,800</b> / $20,000</p>', unsafe_allow_html=True)

# --- הצגת הטופס - רק אם לחצו על הפלוס ---
if st.session_state.adding:
    st.markdown("<br><div style='background-color: #F8F7FF; padding: 25px; border-radius: 20px; border: 1px solid #E9E4FF;'>", unsafe_allow_html=True)
    st.subheader("📝 רישום תנועה חדשה")
    t_mode = st.radio("סוג", ["הוצאה", "הכנסה"], horizontal=True)
    ca, cb = st.columns(2)
    with ca:
        t_wallet = st.selectbox("חשבון", ["מזומן", "BofA", "Amex", "Food Stamps", "Pepper"])
        t_amount = st.number_input("סכום ($)", min_value=0.0)
    with cb:
        t_date = st.date_input("תאריך", datetime.now())
        if t_mode == "הוצאה":
            t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
        else:
            t_cat = st.selectbox("מקור", ["משכורת ישראל", "משכורת רחלי", "עצמאי", "כללי"])
    
    col_save, col_cancel = st.columns(2)
    with col_save:
        if st.button("אישור ושמירה"):
            st.balloons()
            st.session_state.adding = False
            st.rerun()
    with col_cancel:
        if st.button("ביטול"):
            st.session_state.adding = False
            st.rerun()
    st.markdown("</div><br>", unsafe_allow_html=True)

# --- גרפים (מוצגים תמיד מתחת) ---
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

# --- אייקונים בוגרים בתחתית ---
st.markdown("### ניתוח קטגוריות", unsafe_allow_html=True)
row_icons = st.columns(5)
cats_minimal = [("○", "רכב"), ("◇", "מזון"), ("♡", "צדקה"), ("□", "דירה"), ("△", "כללי")]

for i, (symbol, name) in enumerate(cats_minimal):
    with row_icons[i]:
        st.markdown(f'<div class="cat-box"><div class="cat-symbol">{symbol}</div><div class="cat-label">{name}</div></div>', unsafe_allow_html=True)

# --- כפתור הפלוס הצף (פעולה יחידה) ---
st.button("+", on_click=open_form)

# --- תפריט צד ---
with st.sidebar:
    st.title("⚙️ הגדרות")
    st.number_input("עדכון יעד חיסכון", value=20000)
    st.markdown("---")
    st.subheader("🤖 הבוט של רחלי")
    st.info("רחלי, הכל נראה נקי ומסודר עכשיו.")

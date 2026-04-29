import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - ניקוי מוחלט
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת CSS "The Cleanest Slate" ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* 1. מחיקה מוחלטת של קווים ושאריות תפריטים */
    [data-testid="stHeader"], .st-emotion-cache-16idsys, .st-emotion-cache-6q9sum, 
    .st-emotion-cache-z5fcl4, .st-emotion-cache-10o1p90, div[data-testid="stSidebarNav"] {
        display: none !important;
        background-color: transparent !important;
        border: none !important;
    }
    
    /* העלמת הקו המפריד המציק */
    div[class^="st-emotion-cache"] { border-top: none !important; border-bottom: none !important; }
    
    /* 2. רקע פנינה צחור */
    .stApp { background-color: #FFFFFF !important; }
    .block-container { padding: 2rem !important; max-width: 95% !important; }
    
    /* 3. פונט Assistant ויישור לימין */
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }
    
    /* 4. כרטיסיות נתונים */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border-radius: 15px !important;
        padding: 25px !important;
        border: 1px solid #F0F0F5 !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.02) !important;
        border-right: 5px solid #4A3AFF !important;
    }
    
    /* 5. כפתור פלוס צף (FAB) */
    div.stButton > button:first-child {
        position: fixed !important;
        bottom: 35px !important;
        left: 35px !important;
        width: 65px !important;
        height: 65px !important;
        background: #4A3AFF !important;
        color: white !important;
        border-radius: 50% !important;
        font-size: 35px !important;
        box-shadow: 0 10px 30px rgba(74, 58, 255, 0.4) !important;
        border: 2px solid white !important;
        z-index: 99999 !important;
    }

    /* עיצוב חלון הדיאלוג */
    div[data-testid="stDialog"] { direction: rtl !important; }
    </style>
    """, unsafe_allow_html=True)

# --- פונקציית החלון המרחף (Dialog) ---
@st.dialog("תיעוד פעולה חדשה")
def show_transaction_form():
    t_mode = st.radio("סוג פעולה", ["הוצאה", "הכנסה"], horizontal=True)
    
    ca, cb = st.columns(2)
    with ca:
        t_wallet = st.selectbox("אמצעי תשלום / חשבון", ["מזומן", "BofA", "Amex", "Food Stamps", "Pepper", "Leumi"])
        t_amount = st.number_input("סכום ($)", min_value=0.0, step=10.0)
    with cb:
        t_date = st.date_input("תאריך", datetime.now())
        if t_mode == "הוצאה":
            t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
        else:
            # מקורות הכנסה לפי מה שביקשת
            t_cat = st.selectbox("מקור הכנסה", ["משכורת ישראל", "משכורת רחלי", "כללי ישראל", "עצמאי רחלי", "כללי רחלי"])
    
    # שורת הפירוט
    t_desc = st.text_input("פירוט", placeholder="מה בדיוק קרה?")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("אישור ושמירה", use_container_width=True):
        st.balloons()
        st.success(f"הפעולה נרשמה בהצלחה!")
        st.rerun()

# --- תוכן עמוד הבית ---
st.markdown('<h1 style="text-align: center; font-size: 32px; color: #1A1A2E;">Wealth Management</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #716B94; margin-top: -15px;">Asset Tracking | רחלי</p>', unsafe_allow_html=True)

# דשבורד כסף
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: st.metric("Cash", "$2,450")
with c2: st.metric("BofA", "$4,100")
with c3: st.metric("Amex", "$1,200-")

# מד התקדמות
st.markdown("<br>", unsafe_allow_html=True)
st.progress(5800/20000)
st.markdown('<p style="font-size: 13px; color: #716B94;">יעד חיסכון: $20,000</p>', unsafe_allow_html=True)

# גרפים
st.markdown("<br>", unsafe_allow_html=True)
col_g1, col_g2 = st.columns(2)
with col_g1:
    df1 = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
    fig1 = px.pie(df1, values='Val', names='Cat', hole=0.8, title="פירוט סבב")
    fig1.update_layout(showlegend=True, margin=dict(t=30, b=0, l=0, r=0))
    st.plotly_chart(fig1, use_container_width=True)

with col_g2:
    df2 = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [1500, 500, 1500, 1200, 400]})
    fig2 = px.pie(df2, values='Val', names='Cat', hole=0.8, title="ממוצע תקופתי")
    fig2.update_layout(showlegend=True, margin=dict(t=30, b=0, l=0, r=0))
    st.plotly_chart(fig2, use_container_width=True)

# כפתור הפלוס
if st.button("+"):
    show_transaction_form()

# תפריט צד
with st.sidebar:
    st.title("⚙️ הגדרות")
    st.number_input("עדכון יעד", value=20000)
    st.markdown("---")
    st.subheader("🤖 הבוט של רחלי")
    st.info("רחלי, הכל מעודכן.")

import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - חייב להישאר 'expanded' כדי שהסרגל יהיה זמין
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת CSS "Pop-up Style" - מראה אפליקציה נקי לחלוטין ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* 1. הסרת כל הפסים והקווים המיותרים של המערכת */
    [data-testid="stHeader"] { background: transparent !important; }
    .st-emotion-cache-16idsys, .st-emotion-cache-6q9sum, .st-emotion-cache-z5fcl4 { display: none !important; }
    
    /* ניקוי מרחקים בשוליים */
    .block-container { padding: 2rem !important; max-width: 95% !important; }
    
    /* 2. רקע לבן צחור */
    .stApp { background-color: #FFFFFF !important; }
    
    /* 3. פונט Assistant ויישור לימין */
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }
    
    /* 4. כרטיסיות נתונים - בגרות ויוקרה */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border-radius: 15px !important;
        padding: 20px !important;
        border: 1px solid #F0F0F5 !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.02) !important;
        border-right: 5px solid #4A3AFF !important;
    }
    
    /* 5. כפתור פלוס צף (FAB) */
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
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* עיצוב הדיאלוג (החלון המרחף) */
    div[data-testid="stDialog"] { direction: rtl !important; }
    
    /* עיצוב תפריט הצד */
    [data-testid="stSidebar"] { background-color: #FBFBFF !important; border-left: 1px solid #EEE !important; }
    </style>
    """, unsafe_allow_html=True)

# --- פונקציית הדיאלוג (העמוד המרחף) ---
@st.dialog("רישום תנועה חדשה")
def show_transaction_form():
    st.write("מלאי את פרטי הפעולה למטה:")
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
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("אישור ושמירה", use_container_width=True):
        st.success("הנתונים נשמרו!")
        st.rerun()

# --- כותרת דף הבית ---
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

# --- אייקונים בוגרים בתחתית ---
st.markdown("### ניתוח קטגוריות", unsafe_allow_html=True)
row_icons = st.columns(5)
cats_minimal = [("○", "רכב"), ("◇", "מזון"), ("♡", "צדקה"), ("□", "דירה"), ("△", "כללי")]

for i, (symbol, name) in enumerate(cats_minimal):
    with row_icons[i]:
        st.markdown(f'''
            <div style="background:#FDFDFF; border-radius:12px; padding:15px; text-align:center; border:1px solid #F0F0F5;">
                <div style="color:#A0A0C0;">{symbol}</div>
                <div style="color:#5A52CB; font-size:13px; font-weight:700; margin-top:5px;">{name}</div>
            </div>
        ''', unsafe_allow_html=True)

# --- כפתור הפלוס הצף (מפעיל את הדיאלוג) ---
if st.button("+"):
    show_transaction_form()

# --- תפריט צד (Sidebar) - החץ יופיע בפינה ---
with st.sidebar:
    st.title("⚙️ הגדרות")
    st.number_input("עדכון יעד חיסכון", value=20000)
    st.markdown("---")
    st.subheader("🤖 הבוט של רחלי")
    st.info("הכל מוכן לעבודה.")

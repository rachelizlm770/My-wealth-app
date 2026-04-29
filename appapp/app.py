import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת CSS "The One Circle" ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* ניקוי מערכת */
    section[data-testid="stSidebar"], [data-testid="stHeader"], .st-emotion-cache-16idsys { display: none !important; }
    .stApp { background-color: #FFFFFF !important; }
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }

    /* כרטיסיות נתונים */
    div[data-testid="stMetric"] {
        background: white !important;
        border-radius: 20px !important;
        border-right: 8px solid #4A3AFF !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05) !important;
        margin-bottom: 10px !important;
    }

    /* עיצוב כפתור הפלוס הסגול (היחיד) */
    div.stButton > button {
        position: fixed !important;
        bottom: 30px !important;
        left: 30px !important;
        width: 75px !important;
        height: 75px !important;
        background-color: #4A3AFF !important;
        color: white !important;
        border-radius: 50% !important;
        border: 4px solid white !important;
        font-size: 40px !important;
        box-shadow: 0 10px 30px rgba(74, 58, 255, 0.5) !important;
        z-index: 999999 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- פונקציית תפריט פעולות (נפתחת מהעיגול) ---
@st.dialog("מה תרצי לעשות?")
def show_main_menu():
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📝 רישום תנועה", use_container_width=True):
            st.session_state.menu_choice = "transaction"
            st.rerun()
    with col2:
        if st.button("⚙️ הגדרות", use_container_width=True):
            st.session_state.menu_choice = "settings"
            st.rerun()

# --- חלון רישום תנועה ---
@st.dialog("רישום תנועה חדשה")
def show_transaction_form():
    t_mode = st.radio("סוג", ["הוצאה", "הכנסה"], horizontal=True)
    ca, cb = st.columns(2)
    with ca:
        t_wallet = st.selectbox("חשבון", ["מזומן", "BofA", "Amex", "Food Stamps", "Leumi"])
        t_amount = st.number_input("סכום ($)", min_value=0.0)
    with cb:
        t_date = st.date_input("תאריך", datetime.now())
        if t_mode == "הוצאה":
            t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
        else:
            t_cat = st.selectbox("מקור", ["משכורת ישראל", "משכורת רחלי", "עצמאי רחלי", "כללי"])
    st.text_input("פירוט")
    if st.button("שמור נתונים", use_container_width=True):
        st.balloons()
        st.session_state.menu_choice = None
        st.rerun()

# --- חלון הגדרות ---
@st.dialog("הגדרות מערכת")
def show_settings_form():
    st.number_input("עדכון יעד חיסכון", value=20000)
    if st.button("סגור", use_container_width=True):
        st.session_state.menu_choice = None
        st.rerun()

# --- ניהול ניווט פנימי ---
if 'menu_choice' not in st.session_state:
    st.session_state.menu_choice = None

if st.session_state.menu_choice == "transaction":
    show_transaction_form()
elif st.session_state.menu_choice == "settings":
    show_settings_form()

# --- תוכן דף הבית ---
st.markdown('<h1 style="text-align: center; font-size: 30px; color: #1A1A2E;">Wealth Management</h1>', unsafe_allow_html=True)

# דשבורד
c1, c2, c3 = st.columns(3)
with c1: st.metric("Cash", "$2,450")
with c2: st.metric("BofA", "$4,100")
with c3: st.metric("Amex", "-$1,200")

# גרפים משופרים - נתונים בחוץ
st.markdown("<br>", unsafe_allow_html=True)
col_g1, col_g2 = st.columns(2)
df = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
purple_palette = ['#4A3AFF', '#6C63FF', '#8E86FF', '#B0AAFF', '#D2CFFF']

with col_g1:
    fig1 = px.pie(df, values='Val', names='Cat', hole=0.7, title="פירוט סבב")
    fig1.update_traces(
        marker=dict(colors=purple_palette),
        textinfo='label+value+percent',
        texttemplate='<b>%{label}</b><br>$%{value}<br>%{percent}',
        textposition='outside'
    )
    fig1.update_layout(showlegend=False, margin=dict(t=60, b=60, l=60, r=60), height=380)
    st.plotly_chart(fig1, use_container_width=True)

with col_g2:
    fig2 = px.pie(df, values='Val', names='Cat', hole=0.7, title="ממוצע היסטורי")
    fig2.update_traces(
        marker=dict(colors=purple_palette[::-1]),
        textinfo='label+value+percent',
        texttemplate='<b>%{label}</b><br>$%{value}<br>%{percent}',
        textposition='outside'
    )
    fig2.update_layout(showlegend=False, margin=dict(t=60, b=60, l=60, r=60), height=380)
    st.plotly_chart(fig2, use_container_width=True)

# --- הכפתור הסגול היחיד ---
if st.button("+"):
    show_main_menu()

# אייקונים בתחתית
st.markdown("<br>", unsafe_allow_html=True)
row_icons = st.columns(5)
cats = ["רכב", "מזון", "צדקה", "דירה", "כללי"]
for i, name in enumerate(cats):
    with row_icons[i]:
        st.markdown(f'<div style="text-align:center; background:#FDFDFF; padding:12px; border-radius:12px; border:1px solid #F0F0F5; color:#5A52CB; font-weight:700; font-size:12px;">{name}</div>', unsafe_allow_html=True)

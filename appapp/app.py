import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת CSS "The Final Fix" ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* 1. מחיקת כל שארית של המערכת והפסים */
    section[data-testid="stSidebar"], [data-testid="stHeader"], .st-emotion-cache-16idsys, .st-emotion-cache-6q9sum, [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }
    
    .stApp { background-color: #FFFFFF !important; }
    .block-container { padding: 1rem !important; max-width: 100% !important; }
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }
    
    /* 2. כרטיסיות נתונים */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border-radius: 20px !important;
        border: 1px solid #F0F0F5 !important;
        border-right: 8px solid #4A3AFF !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.03) !important;
        margin-bottom: 10px !important;
    }

    /* 3. עיצוב הפלוס הסגול - זיהוי לפי טקסט הכפתור */
    button:has(div:contains("+")) {
        position: fixed !important;
        bottom: 30px !important;
        left: 30px !important;
        width: 75px !important;
        height: 75px !important;
        background-color: #4A3AFF !important;
        color: white !important;
        border-radius: 50% !important;
        border: 4px solid white !important;
        font-size: 45px !important;
        box-shadow: 0 10px 30px rgba(74, 58, 255, 0.5) !important;
        z-index: 99999 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* 4. עיצוב גלגל השיניים בפינה למעלה */
    .settings-wrapper {
        position: fixed;
        top: 20px;
        left: 20px;
        z-index: 9999;
    }
    .settings-wrapper button {
        background-color: #F8F9FA !important;
        border-radius: 50% !important;
        width: 50px !important;
        height: 50px !important;
        border: 1px solid #DDD !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- חלונות מרחפים ---
@st.dialog("תיעוד פעולה")
def show_transaction_form():
    t_mode = st.radio("סוג", ["הוצאה", "הכנסה"], horizontal=True)
    ca, cb = st.columns(2)
    with ca:
        t_wallet = st.selectbox("חשבון", ["מזומן", "BofA", "Amex", "Food Stamps", "Pepper", "Leumi"])
        t_amount = st.number_input("סכום ($)", min_value=0.0)
    with cb:
        t_date = st.date_input("תאריך", datetime.now())
        t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
    st.text_input("פירוט")
    if st.button("אישור ושמירה", use_container_width=True):
        st.balloons()
        st.rerun()

@st.dialog("הגדרות")
def show_settings():
    st.subheader("⚙️ הגדרות")
    st.number_input("יעד חיסכון", value=20000)
    st.info("הכל נקי מקווים!")

# --- תוכן ראשי ---
st.markdown('<h1 style="text-align: center; font-size: 28px;">Wealth Management</h1>', unsafe_allow_html=True)

# דשבורד
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: st.metric("Cash", "$2,450")
with c2: st.metric("BofA", "$4,100")
with c3: st.metric("Amex", "-$1,200")

# גרפים (עם אחוזים, שמות וסכומים)
st.markdown("<br>", unsafe_allow_html=True)
col_g1, col_g2 = st.columns(2)
df = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
purple_palette = ['#4A3AFF', '#6C63FF', '#8E86FF', '#B0AAFF', '#D2CFFF']

with col_g1:
    fig1 = px.pie(df, values='Val', names='Cat', hole=0.7, title="פירוט סבב")
    fig1.update_traces(
        marker=dict(colors=purple_palette),
        textinfo='label+value+percent',
        texttemplate='%{label}<br>$%{value}<br>%{percent}',
        textfont_size=11
    )
    fig1.update_layout(showlegend=False, margin=dict(t=40, b=0, l=0, r=0), height=280)
    st.plotly_chart(fig1, use_container_width=True, config={'displayModeBar': False})

with col_g2:
    fig2 = px.pie(df, values='Val', names='Cat', hole=0.7, title="ממוצע היסטורי")
    fig2.update_traces(
        marker=dict(colors=purple_palette[::-1]),
        textinfo='label+value+percent',
        texttemplate='%{label}<br>$%{value}<br>%{percent}',
        textfont_size=11
    )
    fig2.update_layout(showlegend=False, margin=dict(t=40, b=0, l=0, r=0), height=280)
    st.plotly_chart(fig2, use_container_width=True, config={'displayModeBar': False})

# --- כפתור הפלוס הסגול ---
if st.button("+", key="plus_btn"):
    show_transaction_form()

# --- כפתור הגדרות בפינה למעלה ---
st.markdown('<div class="settings-wrapper">', unsafe_allow_html=True)
if st.button("⚙️", key="settings_btn"):
    show_settings()
st.markdown('</div>', unsafe_allow_html=True)

# קטגוריות בתחתית
st.markdown("<br>", unsafe_allow_html=True)
row_icons = st.columns(5)
cats = ["רכב", "מזון", "צדקה", "דירה", "כללי"]
for i, name in enumerate(cats):
    with row_icons[i]:
        st.markdown(f'<div style="text-align:center; background:#FDFDFF; padding:10px; border-radius:10px; border:1px solid #F0F0F5; color:#5A52CB; font-weight:700; font-size:12px;">{name}</div>', unsafe_allow_html=True)

import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - ניקוי מוחלט
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת CSS לעיצוב היוקרתי והחזרת הכפתורים לחיים ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* 1. מחיקת רכיבי מערכת וקווים */
    [data-testid="stHeader"], [data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
        width: 0 !important;
    }
    .stApp { background-color: #FFFFFF !important; }
    * { font-family: 'Assistant', sans-serif; direction: rtl; }

    /* 2. כפתור פלוס דומיננטי ומרחף (שיטת השכבות) */
    .stButton > button[key="main_plus"] {
        position: fixed !important;
        bottom: 35px !important;
        left: 35px !important;
        width: 80px !important;
        height: 80px !important;
        background-color: #2C5F5F !important; /* טורקיז בוגר */
        color: white !important;
        border-radius: 50% !important;
        border: 4px solid white !important;
        font-size: 40px !important;
        box-shadow: 0 12px 30px rgba(44, 95, 95, 0.4) !important;
        z-index: 999999 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* 3. תווית הגדרות ימנית אקטיבית */
    .stButton > button[key="side_label"] {
        position: fixed !important;
        top: 25% !important;
        right: 0 !important;
        width: 45px !important;
        height: 140px !important;
        background-color: #2C5F5F !important;
        color: white !important;
        border-radius: 15px 0 0 15px !important;
        writing-mode: vertical-rl !important;
        text-orientation: mixed !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        border: none !important;
        z-index: 999999 !important;
        box-shadow: -2px 4px 15px rgba(0,0,0,0.1) !important;
        cursor: pointer !important;
    }

    /* 4. כרטיסיות נתונים בוגרות */
    div[data-testid="stMetric"] {
        background: #F8FBFB !important;
        border-radius: 20px !important;
        border-right: 8px solid #2C5F5F !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.02) !important;
    }
    div[data-testid="stMetricValue"] > div { color: #1B4343 !important; font-weight: 700 !important; }

    /* 5. שורת אייקונים בוגרת */
    .icon-card {
        text-align: center;
        background: #F9F9F9;
        padding: 15px;
        border-radius: 15px;
        border: 1px solid #E6EDED;
    }
    </style>
    """, unsafe_allow_html=True)

# --- חלונות מרחפים ---

@st.dialog("הגדרות וכלים")
def show_settings():
    st.markdown("### 🛠️ ניהול")
    st.radio("ניווט:", ["🤖 בוט פיננסי", "📜 היסטוריה", "📦 ארכיון", "⚙️ הגדרות"], label_visibility="collapsed")
    st.number_input("יעד חיסכון", value=20000)
    if st.button("סגור"): st.rerun()

@st.dialog("דיווח תנועה חדשה")
def show_transaction():
    st.markdown("### 📝 פרטי הפעולה")
    t_mode = st.radio("סוג", ["הוצאה", "הכנסה"], horizontal=True)
    ca, cb = st.columns(2)
    with ca:
        t_amount = st.number_input("סכום ($)", min_value=0.0)
        t_wallet = st.selectbox("חשבון", ["מזומן", "BofA", "Amex", "Leumi"])
    with cb:
        t_date = st.date_input("תאריך", datetime.now())
        t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
    
    st.text_area("לפרט כאן:", placeholder="תיאור חופשי...")
    
    if st.button("אישור ושמירה", use_container_width=True):
        st.balloons()
        st.rerun()

# --- כפתורי הפעלה ---
if st.button("⚙️ הגדרות וכלים", key="side_label"):
    show_settings()

if st.button("+", key="main_plus"):
    show_transaction()

# --- תוכן דף הבית ---
st.markdown('<h1 style="text-align: center; color: #1B4343; font-size: 32px;">Wealth Management</h1>', unsafe_allow_html=True)

# מד התקדמות
col_goal = st.columns([1, 3, 1])
with col_goal[1]:
    st.markdown("<p style='text-align:center; color:#666; font-size:14px; margin-bottom: 5px;'>יעד חיסכון שנתי: <b>$12,450 / $20,000</b></p>", unsafe_allow_html=True)
    st.progress(0.62)

# דשבורד
st.markdown("<br>", unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m1: st.metric("Cash Balance", "$2,450")
with m2: st.metric("Bank Assets", "$4,100")
with m3: st.metric("Credit Debt", "-$1,200")

# גרפים
st.markdown("<br>", unsafe_allow_html=True)
g1, g2 = st.columns(2)
df = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
colors = ['#2C5F5F', '#4E8B8B', '#76A5A5', '#A2C1C1', '#CDE0E0']

with g1:
    st.markdown("<p style='text-align:center; font-weight:700; color:#1B4343;'>📊 פירוט הוצאות שבועי</p>", unsafe_allow_html=True)
    fig1 = px.pie(df, values='Val', names='Cat', hole=0.7)
    fig1.update_traces(marker=dict(colors=colors), textinfo='label+value', textposition='outside')
    fig1.update_layout(showlegend=False, margin=dict(t=30, b=30, l=30, r=30), height=350)
    st.plotly_chart(fig1, use_container_width=True)

with g2:
    st.markdown("<p style='text-align:center; font-weight:700; color:#1B4343;'>📈 ממוצע דו-שבועי כללי</p>", unsafe_allow_html=True)
    fig2 = px.pie(df, values='Val', names='Cat', hole=0.7)
    fig2.update_traces(marker=dict(colors=colors[::-1]), textinfo='label+value', textposition='outside')
    fig2.update_layout(showlegend=False, margin=dict(t=30, b=30, l=30, r=30), height=350)
    st.plotly_chart(fig2, use_container_width=True)

# שורת אייקונים בוגרת
st.markdown("<br>", unsafe_allow_html=True)
row_icons = st.columns(5)
items = [("🚗", "רכב"), ("🛒", "מזון"), ("✡️", "צדקה"), ("🏠", "דירה"), ("⚙️", "כללי")]
for i, (icon, name) in enumerate(items):
    with row_icons[i]:
        st.markdown(f'<div class="icon-card"><div style="font-size: 22px;">{icon}</div><div style="color:#1B4343; font-weight:700; font-size:13px;">{name}</div></div>', unsafe_allow_html=True)

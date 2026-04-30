import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - יציבות מקסימלית
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת CSS יציב ואקטיבי ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* ניקוי רכיבי מערכת */
    [data-testid="stHeader"], [data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }
    .stApp { background-color: #FFFFFF !important; }
    * { font-family: 'Assistant', sans-serif; direction: rtl; }

    /* עיצוב כפתור הפלוס בשמאל (שימוש ב-ID ספציפי) */
    div.stButton > button[key="main_plus_btn"] {
        position: fixed !important;
        bottom: 30px !important;
        left: 30px !important;
        width: 75px !important;
        height: 75px !important;
        background-color: #00A8A8 !important; /* טורקיז ממריץ */
        color: white !important;
        border-radius: 50% !important;
        border: 4px solid white !important;
        font-size: 40px !important;
        box-shadow: 0 10px 25px rgba(0, 168, 168, 0.4) !important;
        z-index: 100000 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* עיצוב לשונית הגדרות בימין (כפתור מערכת במסווה) */
    div.stButton > button[key="side_tools_btn"] {
        position: fixed !important;
        top: 25% !important;
        right: 0 !important;
        width: 45px !important;
        height: 140px !important;
        background-color: #008080 !important;
        color: white !important;
        border-radius: 15px 0 0 15px !important;
        writing-mode: vertical-rl !important;
        text-orientation: mixed !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        border: none !important;
        z-index: 100000 !important;
        box-shadow: -2px 4px 15px rgba(0,0,0,0.1) !important;
    }

    /* כרטיסיות נתונים */
    div[data-testid="stMetric"] {
        background: #F0F9F9 !important;
        border-radius: 20px !important;
        border-right: 8px solid #00A8A8 !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.03) !important;
    }
    div[data-testid="stMetricValue"] > div { color: #004D4D !important; font-weight: 700 !important; }

    /* שורת אייקונים בוגרת */
    .icon-wrapper {
        text-align: center;
        background: #F9FDFD;
        padding: 15px;
        border-radius: 15px;
        border: 1px solid #E0EDED;
    }
    .icon-name { color: #004D4D; font-weight: 700; font-size: 13px; margin-top: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- חלונות מרחפים ---

@st.dialog("שורת כלים והגדרות")
def show_tools_menu():
    st.markdown("### 🛠️ ניהול וכלים")
    choice = st.radio("בחר פעולה:", ["🤖 בוט פיננסי", "📜 היסטוריה", "📦 ארכיון", "⚙️ הגדרות יעד"], label_visibility="collapsed")
    st.markdown("---")
    if choice == "⚙️ הגדרות יעד":
        st.number_input("עדכון יעד חיסכון", value=20000)
    elif choice == "🤖 בוט פיננסי":
        st.info("רחלי, אני מוכן לנתח את הנתונים.")
    if st.button("סגור", use_container_width=True):
        st.rerun()

@st.dialog("דיווח תנועה חדשה")
def show_transaction_dialog():
    st.markdown("### 📝 פרטי הפעולה")
    t_mode = st.radio("סוג פעולה", ["הוצאה", "הכנסה"], horizontal=True)
    ca, cb = st.columns(2)
    with ca:
        t_amount = st.number_input("סכום ($)", min_value=0.0, step=10.0)
        t_wallet = st.selectbox("חשבון", ["מזומן", "BofA", "Amex", "Leumi", "Pepper"])
    with cb:
        t_date = st.date_input("תאריך", datetime.now())
        if t_mode == "הוצאה":
            t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
        else:
            t_cat = st.selectbox("מקור", ["משכורת", "עצמאי", "אחר"])
    
    st.text_area("לפרט כאן (תיאור הפעולה):", placeholder="הוסיפי תיאור כאן...")
    
    if st.button("אישור ושמירה", use_container_width=True):
        st.balloons()
        st.rerun()

# --- תוכן דף הבית ---

# 1. כפתור תווית צדדית (מוזרק ככפתור מערכת)
if st.button("⚙️ הגדרות וכלים", key="side_tools_btn"):
    show_tools_menu()

# 2. כפתור פלוס צף
if st.button("+", key="main_plus_btn"):
    show_transaction_dialog()

st.markdown('<h1 style="text-align: center; color: #004D4D; font-size: 32px;">Wealth Management</h1>', unsafe_allow_html=True)

# מד התקדמות ליעד
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
df_sample = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
colors = ['#00A8A8', '#26C6DA', '#4DD0E1', '#80DEEA', '#B2EBF2']

with g1:
    st.markdown("<p style='text-align:center; font-weight:700; color:#004D4D;'>📊 פירוט הוצאות שבועי</p>", unsafe_allow_html=True)
    fig1 = px.pie(df_sample, values='Val', names='Cat', hole=0.7)
    fig1.update_traces(marker=dict(colors=colors), textinfo='label+value', textposition='outside')
    fig1.update_layout(showlegend=False, margin=dict(t=30, b=30, l=30, r=30), height=320)
    st.plotly_chart(fig1, use_container_width=True)

with g2:
    st.markdown("<p style='text-align:center; font-weight:700; color:#004D4D;'>📈 ממוצע דו-שבועי כללי</p>", unsafe_allow_html=True)
    fig2 = px.pie(df_sample, values='Val', names='Cat', hole=0.7)
    fig2.update_traces(marker=dict(colors=colors[::-1]), textinfo='label+value', textposition='outside')
    fig2.update_layout(showlegend=False, margin=dict(t=30, b=30, l=30, r=30), height=320)
    st.plotly_chart(fig2, use_container_width=True)

# שורת אייקונים בוגרת
st.markdown("<br>", unsafe_allow_html=True)
row_icons = st.columns(5)
items = [("🚗", "רכב"), ("🛒", "מזון"), ("🤝", "צדקה"), ("🏠", "דירה"), ("✨", "כללי")]

for i, (icon, name) in enumerate(items):
    with row_icons[i]:
        st.markdown(f'<div class="icon-wrapper"><div style="font-size: 22px;">{icon}</div><div class="icon-name">{name}</div></div>', unsafe_allow_html=True)

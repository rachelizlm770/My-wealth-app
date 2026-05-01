import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- CSS לעיצוב יוקרתי וכפתורים שעובדים באמת ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* ניקוי רכיבי מערכת */
    [data-testid="stHeader"], [data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }
    .stApp { background-color: #FFFFFF !important; }
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }

    /* עיצוב כפתור הפלוס (בשמאל למטה) */
    div.stButton > button[key="plus_main"] {
        position: fixed !important;
        bottom: 30px !important;
        left: 30px !important;
        width: 70px !important;
        height: 70px !important;
        background-color: #008080 !important;
        color: white !important;
        border-radius: 50% !important;
        border: 4px solid white !important;
        font-size: 35px !important;
        box-shadow: 0 10px 25px rgba(0, 128, 128, 0.4) !important;
        z-index: 1000000 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* עיצוב תווית הגדרות (בימין) */
    div.stButton > button[key="settings_main"] {
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
        z-index: 1000000 !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        border: none !important;
        box-shadow: -2px 4px 15px rgba(0,0,0,0.1) !important;
    }

    /* כרטיסיות נתונים */
    div[data-testid="stMetric"] {
        background: #F4FBFB !important;
        border-radius: 20px !important;
        border-right: 8px solid #008080 !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.03) !important;
    }
    div[data-testid="stMetricValue"] > div { color: #004D4D !important; font-weight: 700 !important; }

    /* אייקונים בתחתית */
    .icon-card {
        text-align: center;
        background: #FAFAFA;
        padding: 20px;
        border-radius: 18px;
        border: 1px solid #E0EAEA;
    }
    </style>
    """, unsafe_allow_html=True)

# --- חלונות מרחפים ---

@st.dialog("⚙️ הגדרות וכלים")
def show_settings():
    st.markdown("### 🛠️ תפריט ניהול")
    st.write("🤖 בוט פיננסי | 📜 היסטוריה | 📦 ארכיון")
    st.number_input("יעד חיסכון חודשי", value=20000)
    if st.button("סגור"): st.rerun()

@st.dialog("📝 תנועה חדשה")
def show_transaction():
    st.markdown("### דיווח פעולה")
    t_mode = st.radio("סוג", ["הוצאה", "הכנסה"], horizontal=True)
    ca, cb = st.columns(2)
    with ca:
        t_amount = st.number_input("סכום ($)", min_value=0.0)
        t_wallet = st.selectbox("חשבון", ["מזומן", "BofA", "Amex", "Pepper"])
    with cb:
        t_date = st.date_input("תאריך", datetime.now())
        t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
    st.text_area("פירוט:", placeholder="הוסיפי תיאור כאן...")
    if st.button("אישור ושמירה", use_container_width=True):
        st.balloons(); st.rerun()

# --- כפתורי הפעלה (הם המעוצבים עכשיו) ---
# הצבתי אותם כאן כדי שיהיו זמינים ל-CSS
if st.button("⚙️ הגדרות וכלים", key="settings_main"):
    show_settings()

if st.button("+", key="plus_main"):
    show_transaction()

# --- תוכן דף הבית ---
st.markdown('<h1 style="text-align: center; color: #004D4D; font-size: 34px;">Wealth Management</h1>', unsafe_allow_html=True)

# יעד חיסכון
col_goal = st.columns([1, 3, 1])
with col_goal[1]:
    st.markdown("<p style='text-align:center; font-size:14px; color:#666;'>יעד חיסכון שנתי: <b>$12,450 / $20,000</b></p>", unsafe_allow_html=True)
    st.progress(0.62)

st.markdown("<br>", unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m1: st.metric("Cash Balance", "$2,450")
with m2: st.metric("Bank Assets", "$4,100")
with m3: st.metric("Credit Debt", "-$1,200")

# גרפים
st.markdown("<br>", unsafe_allow_html=True)
g1, g2 = st.columns(2)
df = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
colors = ['#008080', '#2E9A9A', '#5CB4B4', '#8ACFCF', '#B8E9E9']

with g1:
    st.markdown("<p style='text-align:center; font-weight:700; color:#004D4D;'>📊 פירוט הוצאות שבועי</p>", unsafe_allow_html=True)
    fig1 = px.pie(df, values='Val', names='Cat', hole=0.7)
    fig1.update_traces(marker=dict(colors=colors), textinfo='label+value')
    fig1.update_layout(showlegend=False, margin=dict(t=0, b=0, l=30, r=30), height=300)
    st.plotly_chart(fig1, use_container_width=True)

with g2:
    st.markdown("<p style='text-align:center; font-weight:700; color:#004D4D;'>📈 ממוצע דו-שבועי כללי</p>", unsafe_allow_html=True)
    fig2 = px.pie(df, values='Val', names='Cat', hole=0.7)
    fig2.update_traces(marker=dict(colors=colors[::-1]), textinfo='label+value')
    fig2.update_layout(showlegend=False, margin=dict(t=0, b=0, l=30, r=30), height=300)
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)
row_icons = st.columns(5)
items = [("🚗", "רכב"), ("🛒", "מזון"), ("🤝", "צדקה"), ("🏠", "דירה"), ("✨", "כללי")]
for i, (icon, name) in enumerate(items):
    with row_icons[i]:
        st.markdown(f'<div class="icon-card"><div style="font-size:24px; color:#008080; margin-bottom:5px;">{icon}</div><div style="color:#004D4D; font-weight:700; font-size:13px;">{name}</div></div>', unsafe_allow_html=True)

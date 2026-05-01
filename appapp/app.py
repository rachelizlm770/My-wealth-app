import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת CSS חזק יותר (Force Style) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* העלמה מוחלטת של רכיבי מערכת */
    [data-testid="stHeader"], [data-testid="stSidebarCollapsedControl"] { display: none !important; }
    .stApp { background-color: #FFFFFF !important; }
    * { font-family: 'Assistant', sans-serif; direction: rtl; }

    /* עיצוב כפתור הפלוס - כפייה של מיקום וצורה */
    button[key="plus_fixed"] {
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
        z-index: 99999 !important;
    }
    
    /* עיצוב תווית ההגדרות - כפייה של מיקום וצורה */
    button[key="settings_fixed"] {
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
        z-index: 99999 !important;
        font-weight: 600 !important;
        border: none !important;
        box-shadow: -2px 4px 15px rgba(0,0,0,0.1) !important;
    }

    /* מחיקת הריבועים הלבנים שנוצרים כשאריות */
    .stButton > button:not([key="plus_fixed"]):not([key="settings_fixed"]) {
        display: none !important;
    }

    /* כרטיסיות נתונים */
    div[data-testid="stMetric"] {
        background: #F4FBFB !important;
        border-radius: 20px !important;
        border-right: 8px solid #008080 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- פונקציות הדיאלוג ---
@st.dialog("⚙️ הגדרות וכלים")
def show_settings():
    st.write("🤖 בוט פיננסי | 📜 היסטוריה | 📦 ארכיון")
    st.number_input("יעד חיסכון חודשי", value=20000)

@st.dialog("📝 תנועה חדשה")
def show_transaction():
    st.markdown("### דיווח פעולה")
    t_mode = st.radio("סוג", ["הוצאה", "הכנסה"], horizontal=True)
    st.number_input("סכום ($)", min_value=0.0)
    st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
    st.text_area("פירוט:")
    if st.button("שמור"): st.rerun()

# --- יצירת הכפתורים בתוך מיכל צף (זה ימנע מהם להופיע למעלה) ---
placeholder = st.empty()
with placeholder.container():
    if st.button("⚙️ הגדרות וכלים", key="settings_fixed"):
        show_settings()
    if st.button("+", key="plus_fixed"):
        show_transaction()

# --- תוכן דף הבית ---
st.markdown('<h1 style="text-align: center; color: #004D4D; font-size: 34px;">Wealth Management</h1>', unsafe_allow_html=True)

col_goal = st.columns([1, 3, 1])
with col_goal[1]:
    st.progress(0.62)
    st.markdown("<p style='text-align:center; font-size:14px; color:#666;'>יעד חיסכון שנתי: $12,450 / $20,000</p>", unsafe_allow_html=True)

m1, m2, m3 = st.columns(3)
with m1: st.metric("Cash Balance", "$2,450")
with m2: st.metric("Bank Assets", "$4,100")
with m3: st.metric("Credit Debt", "-$1,200")

st.markdown("<br>", unsafe_allow_html=True)
g1, g2 = st.columns(2)
df = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
colors = ['#008080', '#2E9A9A', '#5CB4B4', '#8ACFCF', '#B8E9E9']

with g1:
    fig1 = px.pie(df, values='Val', names='Cat', hole=0.7, title="הוצאות שבועי")
    fig1.update_traces(marker=dict(colors=colors), textinfo='label+value')
    st.plotly_chart(fig1, use_container_width=True)

with g2:
    fig2 = px.pie(df, values='Val', names='Cat', hole=0.7, title="ממוצע כללי")
    fig2.update_traces(marker=dict(colors=colors[::-1]), textinfo='label+value')
    st.plotly_chart(fig2, use_container_width=True)

# שורת אייקונים
st.markdown("<br>", unsafe_allow_html=True)
row_icons = st.columns(5)
items = [("🚗", "רכב"), ("🛒", "מזון"), ("🤝", "צדקה"), ("🏠", "דירה"), ("✨", "כללי")]
for i, (icon, name) in enumerate(items):
    with row_icons[i]:
        st.markdown(f'<div style="text-align:center; background:#FAFAFA; padding:20px; border-radius:18px; border:1px solid #E0EAEA;"><div style="font-size:24px;">{icon}</div><div style="color:#004D4D; font-weight:700;">{name}</div></div>', unsafe_allow_html=True)

import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - יציב
st.set_page_config(page_title="Wealth Management", layout="wide")

# --- CSS יציב (בלי ניסיונות הסתרה ששוברים את הדף) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* עיצוב כללי */
    .stApp { background-color: #FFFFFF; }
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }
    
    /* כרטיסיות נתונים בטורקיז בוגר */
    div[data-testid="stMetric"] {
        background: #F4F8F8 !important;
        border-radius: 15px !important;
        border-right: 8px solid #3D5A5A !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
    }
    
    /* כפתור הפלוס הצף */
    .floating-plus {
        position: fixed;
        bottom: 30px;
        left: 30px;
        width: 70px;
        height: 70px;
        background-color: #3D5A5A;
        color: white !important;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 40px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        z-index: 1000;
        border: 3px solid white;
        cursor: pointer;
        text-decoration: none !important;
    }

    /* עיצוב כותרות */
    h1 { color: #2A3F3F; }
    </style>
    """, unsafe_allow_html=True)

# --- פונקציות דיאלוג ---

@st.dialog("דיווח תנועה חדשה")
def show_transaction():
    t_mode = st.radio("סוג פעולה", ["הוצאה", "הכנסה"], horizontal=True)
    ca, cb = st.columns(2)
    with ca:
        t_amount = st.number_input("סכום ($)", min_value=0.0)
        t_wallet = st.selectbox("חשבון", ["מזומן", "BofA", "Amex", "Leumi"])
    with cb:
        t_date = st.date_input("תאריך", datetime.now())
        t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
    
    # שדה פירוט
    st.text_area("פירוט הפעולה:", placeholder="על מה הוצאת/הכנסת?")
    
    if st.button("שמור", use_container_width=True):
        st.balloons()
        st.rerun()

@st.dialog("הגדרות וכלים")
def show_tools():
    st.write("🤖 בוט פיננסי")
    st.write("📜 היסטוריה")
    st.number_input("יעד חיסכון", value=20000)

# --- תוכן דף הבית ---
st.markdown('<h1 style="text-align: center;">Wealth Management</h1>', unsafe_allow_html=True)

# כפתור הגדרות בראש העמוד (במקום התווית ששברה הכל)
col_set1, col_set2 = st.columns([8, 2])
with col_set2:
    if st.button("⚙️ הגדרות וכלים", use_container_width=True):
        show_tools()

# מדדים
m1, m2, m3 = st.columns(3)
with m1: st.metric("Cash Balance", "$2,450")
with m2: st.metric("Bank Assets", "$4,100")
with m3: st.metric("Credit Debt", "-$1,200")

# גרפים
st.markdown("<br>", unsafe_allow_html=True)
g1, g2 = st.columns(2)
df = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
colors = ['#3D5A5A', '#5E8080', '#83A3A3', '#ABC5C5', '#D4E4E4']

with g1:
    fig1 = px.pie(df, values='Val', names='Cat', hole=0.7, title="הוצאות")
    fig1.update_traces(marker=dict(colors=colors), textinfo='label+value')
    st.plotly_chart(fig1, use_container_width=True)

with g2:
    fig2 = px.pie(df, values='Val', names='Cat', hole=0.7, title="ממוצע")
    fig2.update_traces(marker=dict(colors=colors[::-1]), textinfo='label+value')
    st.plotly_chart(fig2, use_container_width=True)

# כפתור פלוס
if st.button("+"):
    show_transaction()

# קטגוריות
st.markdown("<br>", unsafe_allow_html=True)
row = st.columns(5)
for i, name in enumerate(["רכב", "מזון", "צדקה", "דירה", "כללי"]):
    with row[i]:
        st.info(name)

import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף
st.set_page_config(page_title="העושר שלי", layout="wide", initial_sidebar_state="collapsed")

# --- עיצוב טורקיז-מנטה רך וברור ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;600;700&display=swap');
    
    /* רקע ופונט כללי */
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }
    .stApp { background: #E6FFFA; } /* רקע מנטה בהיר מאוד */
    
    /* כרטיסיות לבנות ורכות */
    div[data-testid="stMetric"], .main-card, div[data-testid="stExpander"] {
        background-color: white !important;
        border-radius: 35px !important;
        border: 2px solid #B2F5EA !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.02) !important;
        padding: 20px !important;
    }
    
    /* טקסטים כהים וברורים */
    h1, h2, h3, p, span, label { color: #234E52 !important; font-weight: 700 !important; }
    div[data-testid="stMetricValue"] > div { color: #2C7A7B !important; font-size: 35px !important; }
    
    /* כפתור פלוס צף */
    .fab-container {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 100;
    }
    .stButton>button {
        background: #319795 !important;
        color: white !important;
        border-radius: 50% !important;
        width: 70px !important;
        height: 70px !important;
        font-size: 30px !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2) !important;
        border: none !important;
    }

    /* אייקונים בתחתית */
    .icon-box {
        background: white;
        border-radius: 30px;
        padding: 15px;
        text-align: center;
        border: 2px solid #81E6D9;
        transition: 0.3s;
    }
    .icon-box:hover { transform: translateY(-5px); background: #F0FFF4; }
    </style>
    """, unsafe_allow_html=True)

# כותרת
st.markdown('<h1 style="text-align: center; font-size: 40px;">העושר שלי ✨</h1>', unsafe_allow_html=True)

# דשבורד כסף
col1, col2, col3 = st.columns(3)
with col1: st.metric("מזומן (Cash) 💵", "$2,450")
with col2: st.metric("בנק (BofA) 🏦", "$4,100")
with col3: st.metric("אשראי (Amex) 💳", "$1,200-")

# מד התקדמות
st.markdown("### 🎯 היעד: $20,000")
st.progress(5800/20000)
st.write(f"נחסכו: **$5,800** | עוד **10 ימים** לאיפוס")

st.markdown("---")

# עוגות נתונים (החזרתי אותן!)
col_g1, col_g2 = st.columns(2)
with col_g1:
    df1 = pd.DataFrame({'קטגוריה': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'סכום': [800, 300, 750, 1200, 250]})
    fig1 = px.pie(df1, values='סכום', names='קטגוריה', hole=0.5, title="הוצאות הסבב")
    fig1.update_traces(marker=dict(colors=['#319795', '#4FD1C5', '#81E6D9', '#B2F5EA', '#285E61']))
    st.plotly_chart(fig1, use_container_width=True)
with col_g2:
    df2 = pd.DataFrame({'קטגוריה': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'סכום': [1500, 500, 1500, 1200, 400]})
    fig2 = px.pie(df2, values='סכום', names='קטגוריה', hole=0.5, title="ממוצע היסטורי")
    st.plotly_chart(fig2, use_container_width=True)

# כפתור הפלוס להוספה
st.markdown('<div class="fab-container">', unsafe_allow_html=True)
with st.expander("➕ הוספת תנועה", expanded=False):
    t_mode = st.radio("סוג", ["הוצאה", "הכנסה"], horizontal=True)
    t_wallet = st.selectbox("אמצעי תשלום", ["מזומן", "Bank of America", "American Express", "Food Stamps", "Pepper"])
    t_amount = st.number_input("סכום ($)", min_value=0.0)
    
    if t_mode == "הוצאה":
        t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
    else:
        t_cat = st.selectbox("מקור", ["משכורת ישראל", "משכורת רחלי", "כללי ישראל", "עצמאי רחלי", "כללי רחלי"])
    
    if st.button("שמור"):
        st.balloons()
        st.success("נשמר!")
st.markdown('</div>', unsafe_allow_html=True)

# אייקונים בתחתית
st.markdown("### 🔍 פירוט מהיר")
rows = st.columns(5)
cats = [("🚗", "רכב"), ("🥗", "מזון"), ("❤️", "צדקה"), ("🏠", "דירה"), ("📦", "כללי")]
for i, (icon, name) in enumerate(cats):
    with rows[i]:
        st.markdown(f'<div class="icon-box"><div style="font-size:30px;">{icon}</div><div style="font-size:14px;">{name}</div></div>', unsafe_allow_html=True)

# תפריט צד
with st.sidebar:
    st.title("⚙️ הגדרות")
    st.number_input("יעד חיסכון", value=20000)
    st.info("🤖 רחלי, אל תשכחי לעשות Swap למזומן!")

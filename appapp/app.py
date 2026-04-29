import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף
st.set_page_config(page_title="העושר שלי", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת עיצוב "מנטה-טורקיז" חזק וברור ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;600;700&display=swap');
    
    /* 1. רקע האפליקציה - מנטה-טורקיז רך ונעים */
    .stApp { background-color: #E6FFFA !important; }
    
    /* 2. טקסטים - שחור עמוק וברור (שלא יהיה ספק) */
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }
    h1, h2, h3, p, span, label, div { color: #1A365D !important; font-weight: 800 !important; }
    
    /* 3. כרטיסיות (Metrics) - בועות לבנות עגולות */
    div[data-testid="stMetric"] {
        background-color: white !important;
        border-radius: 40px !important;
        padding: 25px !important;
        box-shadow: 0 15px 35px rgba(49, 151, 149, 0.15) !important;
        border: 3px solid #81E6D9 !important;
    }
    div[data-testid="stMetricValue"] > div { color: #2C7A7B !important; font-size: 40px !important; }

    /* 4. פלוס צף אמיתי - עגול ובצד למטה */
    .fab-container {
        position: fixed;
        bottom: 30px;
        left: 30px; /* שמתי בצד שמאל כדי שלא יפריע לעברית */
        z-index: 9999;
    }
    .stButton>button {
        background: #38B2AC !important;
        color: white !important;
        border-radius: 50% !important;
        width: 80px !important;
        height: 80px !important;
        font-size: 40px !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3) !important;
        border: 4px solid white !important;
    }

    /* 5. עוגות נתונים - עיצוב רך */
    .plot-container { border-radius: 30px; overflow: hidden; background: white; padding: 10px; }

    /* 6. אייקונים בתחתית */
    .icon-box {
        background: white;
        border-radius: 35px;
        padding: 20px;
        text-align: center;
        border: 3px solid #81E6D9;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    }
    header, footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# כותרת
st.markdown('<h1 style="text-align: center; font-size: 50px; color: #2C7A7B !important;">העושר שלי ✨</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 22px;">רחלי, בואי נצמח היום!</p>', unsafe_allow_html=True)

# --- דשבורד כסף ---
col1, col2, col3 = st.columns(3)
with col1: st.metric("מזומן ביד 💵", "$2,450")
with col2: st.metric("בבנק BofA 🏦", "$4,100")
with col3: st.metric("חוב אשראי 💳", "$1,200-")

# מד התקדמות
st.markdown("<br>### 🎯 היעד: $20,000", unsafe_allow_html=True)
st.progress(5800/20000)
st.write("נחסכו: **$5,800** | עוד **10 ימים** לסבב")

st.markdown("<br>---<br>", unsafe_allow_html=True)

# --- עוגות הנתונים (ממוצע מול נוכחי) ---
st.markdown("### 📊 ניתוח הוצאות שבועי", unsafe_allow_html=True)
c_g1, c_g2 = st.columns(2)
with c_g1:
    df1 = pd.DataFrame({'קט': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], '₪': [800, 300, 750, 1200, 250]})
    fig1 = px.pie(df1, values='₪', names='קט', hole=0.6, title="הסבב הנוכחי")
    fig1.update_traces(marker=dict(colors=['#319795', '#4FD1C5', '#81E6D9', '#B2F5EA', '#2D3748']))
    st.plotly_chart(fig1, use_container_width=True)
with c_g2:
    df2 = pd.DataFrame({'קט': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], '₪': [1500, 500, 1500, 1200, 400]})
    fig2 = px.pie(df2, values='₪', names='קט', hole=0.6, title="ממוצע היסטורי")
    fig2.update_traces(marker=dict(colors=['#2C7A7B', '#38B2AC', '#4FD1C5', '#81E6D9', '#E6FFFA']))
    st.plotly_chart(fig2, use_container_width=True)

# --- כפתור הפלוס הצף להוספה ---
st.markdown('<div class="fab-container">', unsafe_allow_html=True)
with st.expander("➕", expanded=False):
    st.markdown('<div style="background: white; padding: 25px; border-radius: 30px; border: 3px solid #81E6D9;">', unsafe_allow_html=True)
    st.write("### הוספת תנועה")
    t_mode = st.radio("סוג", ["הוצאה 💸", "הכנסה 💰"], horizontal=True)
    t_wallet = st.selectbox("איך שילמת?", ["מזומן", "BofA", "Amex", "Food Stamps", "Pepper"])
    t_amount = st.number_input("סכום ($)", min_value=0.0)
    
    if "הוצאה" in t_mode:
        t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
    else:
        t_cat = st.selectbox("מקור", ["משכורת ישראל", "משכורת רחלי", "כללי ישראל", "עצמאי רחלי", "כללי רחלי"])
    
    if st.button("שמור ✅"):
        st.balloons()
        st.success("נשמר!")
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- פירוט אייקונים בתחתית ---
st.markdown("<br>### 📂 קטגוריות", unsafe_allow_html=True)
row = st.columns(5)
cats = [("🚗", "רכב"), ("🥗", "מזון"), ("❤️", "צדקה"), ("🏠", "דירה"), ("📦", "כללי")]
for i, (icon, name) in enumerate(cats):
    with row[i]:
        st.markdown(f'<div class="icon-box"><div style="font-size:40px;">{icon}</div><div style="font-size:18px; font-weight:800;">{name}</div></div>', unsafe_allow_html=True)

# תפריט צד
with st.sidebar:
    st.title("⚙️ הגדרות")
    st.number_input("יעד חיסכון", value=20000)
    st.info("🤖 רחלי, הבוט כאן לשירותך!")

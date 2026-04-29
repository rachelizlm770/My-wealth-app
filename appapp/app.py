import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - הסתרת התפריטים לחלוטין למראה נקי
st.set_page_config(page_title="העושר שלי", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת עיצוב Luxury Purple: בוגר, אחיד ומכבד ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* ניקוי רקע כללי והסרת הפס הצידי */
    .stApp { background-color: #FFFFFF !important; }
    [data-testid="stSidebar"] { background-color: #F8F7FF !important; border-left: 1px solid #E9E4FF; }
    
    /* פונט Assistant ויישור לימין */
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }
    
    /* כרטיסיות נתונים - סגול בהיר מאוד עם קו סגול עמוק */
    div[data-testid="stMetric"] {
        background-color: #FBFBFF !important;
        border-radius: 20px !important;
        padding: 20px !important;
        border: 1px solid #E9E4FF !important;
        box-shadow: 0 4px 15px rgba(108, 99, 255, 0.05) !important;
        border-top: 4px solid #6C63FF !important; /* פס עליון סגול למראה מכבד */
    }
    
    /* טקסטים - סגול כהה/שחור */
    h1, h2, h3, p, span, label { color: #2D2A4A !important; font-weight: 600 !important; }
    div[data-testid="stMetricValue"] > div { color: #5A52CB !important; font-size: 32px !important; font-weight: 700 !important; }
    
    /* כפתור הפלוס הצף (FAB) - סגול יוקרתי */
    .fab-button {
        position: fixed;
        bottom: 40px;
        left: 40px;
        width: 65px;
        height: 65px;
        background: linear-gradient(135deg, #6C63FF 0%, #4A3AFF 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white !important;
        font-size: 35px;
        box-shadow: 0 10px 25px rgba(108, 99, 255, 0.3);
        cursor: pointer;
        z-index: 9999;
        border: 2px solid #FFFFFF;
        text-decoration: none !important;
    }

    /* כרטיסיות אייקונים בתחתית - גווני לילך אחידים */
    .icon-card {
        background: #F8F7FF;
        border-radius: 20px;
        padding: 18px;
        text-align: center;
        border: 1px solid #E9E4FF;
        transition: 0.3s;
    }
    .icon-card:hover { background: #EEECFF; border-color: #6C63FF; }

    /* הסתרת כותרות מערכת של Streamlit */
    header, footer { visibility: hidden; }
    .css-1rs6os {display: none;} /* מסתיר את הפס המעצבן בצד */
    </style>
    
    <a href="#add-data" class="fab-button">+</a>
    """, unsafe_allow_html=True)

# --- כותרת ראשית ---
st.markdown('<h1 style="text-align: center; font-size: 38px; color: #4A3AFF; letter-spacing: 1px;">העושר שלי ✨</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #716B94; font-size: 16px; margin-top: -10px;">ניהול פיננסי חכם ומכבד</p>', unsafe_allow_html=True)

# --- דשבורד כסף ---
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: st.metric("מזומן (Cash)", "$2,450")
with c2: st.metric("בנק (BofA)", "$4,100")
with c3: st.metric("אשראי (Amex)", "$1,200-")

# מד התקדמות (סגול)
st.markdown("<br>### 🎯 יעד חיסכון: $20,000", unsafe_allow_html=True)
st.progress(5800/20000)
st.write(f"נחסכו עד כה: **$5,800** | **10 ימים** לסיום הסבב")

st.markdown("<br><hr style='border: 0.5px solid #E9E4FF;'><br>", unsafe_allow_html=True)

# --- עוגות נתונים (גווני סגול בלבד) ---
col_g1, col_g2 = st.columns(2)
purple_scale = ['#4A3AFF', '#6C63FF', '#8E86FF', '#B0AAFF', '#D2CFFF']

with col_g1:
    df1 = pd.DataFrame({'קטגוריה': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'סכום': [800, 300, 750, 1200, 250]})
    fig1 = px.pie(df1, values='סכום', names='קטגוריה', hole=0.7, title="הוצאות נוכחיות")
    fig1.update_traces(marker=dict(colors=purple_scale), textinfo='none')
    fig1.update_layout(showlegend=True, margin=dict(t=30, b=0, l=0, r=0))
    st.plotly_chart(fig1, use_container_width=True)

with col_g2:
    df2 = pd.DataFrame({'קטגוריה': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'סכום': [1500, 500, 1500, 1200, 400]})
    fig2 = px.pie(df2, values='סכום', names='קטגוריה', hole=0.7, title="ממוצע תקופתי")
    fig2.update_traces(marker=dict(colors=['#D2CFFF', '#B0AAFF', '#8E86FF', '#6C63FF', '#4A3AFF']), textinfo='none')
    fig2.update_layout(showlegend=True, margin=dict(t=30, b=0, l=0, r=0))
    st.plotly_chart(fig2, use_container_width=True)

# --- אזור הוספת תנועה ---
st.markdown('<div id="add-data"></div>', unsafe_allow_html=True)
with st.expander("📝 רישום תנועה חדשה", expanded=False):
    st.markdown("<div style='padding: 10px;'>", unsafe_allow_html=True)
    mode = st.radio("סוג הפעולה", ["הוצאה 💸", "הכנסה 💰"], horizontal=True)
    
    ca, cb = st.columns(2)
    with ca:
        wallet = st.selectbox("מקור כספי", ["מזומן", "BofA", "Amex", "Food Stamps", "Pepper"])
        amount = st.number_input("סכום בשפע ($)", min_value=0.0)
    with cb:
        date = st.date_input("תאריך", datetime.now())
        if "הוצאה" in mode:
            cat = st.selectbox("לאן הכסף הלך?", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
        else:
            cat = st.selectbox("מאיפה הכסף הגיע?", ["משכורת ישראל", "משכורת רחלי", "כללי ישראל", "עצמאי רחלי", "כללי רחלי"])
    
    if st.button("אישור ושמירה ✨"):
        st.balloons()
        st.success("הנתונים עודכנו במערכת.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- אייקונים בתחתית - כולם בגוון סגול אחיד ---
st.markdown("<br>### 📂 קטגוריות מרכזיות", unsafe_allow_html=True)
row_icons = st.columns(5)
cats = [("🚗", "רכב"), ("🥗", "מזון"), ("❤️", "צדקה"), ("🏠", "דירה"), ("📦", "כללי")]

for i, (icon, name) in enumerate(cats):
    with row_icons[i]:
        st.markdown(f'''
            <div class="icon-card">
                <div style="font-size:30px; margin-bottom:5px;">{icon}</div>
                <div style="font-size:14px; color:#4A3AFF; font-weight:700;">{name}</div>
            </div>
        ''', unsafe_allow_html=True)

# --- סרגל צד (Sidebar) ---
with st.sidebar:
    st.markdown("<h2 style='color: #4A3AFF;'>⚙️ ניהול חשבון</h2>", unsafe_allow_html=True)
    st.number_input("עדכון יעד חיסכון", value=20000)
    st.markdown("---")
    st.info("💡 רחלי, המראה הסגול נותן שקט נפשי לניהול הכסף. מה דעתך?")

import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - נקי ומותאם למובייל
st.set_page_config(page_title="העושר של רחלי", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת עיצוב יוקרתי: רקע בהיר, כפתור צף וצבעים ממריצים ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;600;700&display=swap');
    
    /* רקע בהיר ונקי */
    .stApp { background-color: #FFFFFF !important; }
    
    /* פונט Assistant קריא וברור */
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }
    
    /* כרטיסיות נתונים - לבנות עם מסגרת צבעונית עדינה */
    div[data-testid="stMetric"] {
        background-color: #F8FAFC !important;
        border-radius: 25px !important;
        padding: 20px !important;
        border: 2px solid #E2E8F0 !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
    }
    
    /* טקסטים שחורים וברורים */
    h1, h2, h3, p, span, label { color: #1A202C !important; font-weight: 700 !important; }
    div[data-testid="stMetricValue"] > div { color: #319795 !important; font-size: 32px !important; }

    /* כפתור הפלוס הצף (FAB) - עיגול טורקיז */
    .fab-button {
        position: fixed;
        bottom: 30px;
        left: 30px; /* צד שמאל למטה */
        width: 70px;
        height: 70px;
        background-color: #38B2AC;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 40px;
        box-shadow: 0 10px 25px rgba(56, 178, 172, 0.4);
        cursor: pointer;
        z-index: 9999;
        border: 3px solid white;
        text-decoration: none;
    }

    /* עיצוב האייקונים בתחתית - צבעוניים ומעוגלים */
    .icon-card {
        background: #F1F5F9;
        border-radius: 25px;
        padding: 15px;
        text-align: center;
        transition: 0.3s;
        border: 2px solid transparent;
    }
    .icon-card:hover { transform: translateY(-5px); border-color: #38B2AC; background: white; }

    /* הסתרת אלמנטים מיותרים */
    header, footer { visibility: hidden; }
    </style>
    
    <a href="#add-transaction" class="fab-button">+</a>
    """, unsafe_allow_html=True)

# --- כותרת ראשית ---
st.markdown('<h1 style="text-align: center; font-size: 40px; color: #2C7A7B;">העושר שלי ✨</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #4A5568;">הדרך הבטוחה לשפע כלכלי</p>', unsafe_allow_html=True)

# --- דשבורד כסף ---
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1: st.metric("מזומן ביד 💵", "$2,450")
with col2: st.metric("בבנק BofA 🏦", "$4,100")
with col3: st.metric("חוב אשראי 💳", "$1,200-")

# מד התקדמות (טורקיז)
st.markdown("<br>### 🎯 היעד: $20,000", unsafe_allow_html=True)
st.progress(5800/20000)
st.write(f"נחסכו: **$5,800** | נותרו **10 ימים** לסבב")

st.markdown("---")

# --- עוגות נתונים ---
col_g1, col_g2 = st.columns(2)
with col_g1:
    df1 = pd.DataFrame({'קטגוריה': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'סכום': [800, 300, 750, 1200, 250]})
    fig1 = px.pie(df1, values='סכום', names='קטגוריה', hole=0.6, title="הוצאות הסבב")
    fig1.update_traces(marker=dict(colors=['#38B2AC', '#4FD1C5', '#81E6D9', '#B2F5EA', '#2D3748']))
    st.plotly_chart(fig1, use_container_width=True)
with col_g2:
    df2 = pd.DataFrame({'קטגוריה': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'סכום': [1500, 500, 1500, 1200, 400]})
    fig2 = px.pie(df2, values='סכום', names='קטגוריה', hole=0.6, title="ממוצע היסטורי")
    st.plotly_chart(fig2, use_container_width=True)

# --- אזור הוספת תנועה (נפתח בלחיצה על הפלוס או כאן) ---
st.markdown('<div id="add-transaction"></div>', unsafe_allow_html=True)
with st.expander("➕ הוספת תנועה חדשה (הכנסה/הוצאה)", expanded=False):
    st.write("### פרטי הפעולה")
    mode = st.radio("סוג", ["הוצאה 💸", "הכנסה 💰"], horizontal=True)
    
    c1, c2 = st.columns(2)
    with c1:
        wallet = st.selectbox("אמצעי תשלום", ["מזומן 💵", "Bank of America 🏦", "American Express 💳", "Food Stamps 🍎", "Pepper 🌶️"])
        amount = st.number_input("סכום ($)", min_value=0.0)
    with c2:
        date = st.date_input("תאריך", datetime.now())
        if "הוצאה" in mode:
            cat = st.selectbox("קטגוריה", ["צדקה ❤️", "רכב 🚗", "מזון 🥗", "דירה 🏠", "כללי 📦"])
        else:
            cat = st.selectbox("מקור", ["משכורת ישראל 🇮🇱", "משכורת רחלי 👩‍💻", "כללי ישראל 👴", "עצמאי רחלי ✍️", "כללי רחלי 🌍"])
    
    # חישוב פוד סטאמפס אוטומטי
    if "Food Stamps" in wallet:
        st.info(f"מחשב 75% ליתרה: ${amount * 0.75:.2f}")

    if st.button("שמור נתונים ✨"):
        st.balloons()
        st.success("נשמר בהצלחה!")

# --- אייקונים צבעוניים בתחתית ---
st.markdown("<br>### 📂 קטגוריות", unsafe_allow_html=True)
row1 = st.columns(5)
# צבעים לאייקונים: רכב (כחול), מזון (כתום), צדקה (ורוד), דירה (ירוק), כללי (סגול)
cat_icons = [("🚗", "רכב", "#EBF8FF"), ("🥗", "מזון", "#FFFAF0"), ("❤️", "צדקה", "#FFF5F5"), ("🏠", "דירה", "#F0FFF4"), ("📦", "כללי", "#FAF5FF")]

for i, (icon, name, color) in enumerate(cat_icons):
    with row1[i]:
        st.markdown(f'<div class="icon-card" style="background-color: {color}; border-bottom: 5px solid {color.replace("F", "E")}"><div style="font-size:35px;">{icon}</div><div style="font-size:16px; color:#2D3748;">{name}</div></div>', unsafe_allow_html=True)

# --- תפריט צד (Sidebar) ---
with st.sidebar:
    st.markdown("## ⚙️ הגדרות")
    st.number_input("יעד חיסכון סופי ($)", value=20000)
    st.markdown("---")
    st.subheader("🤖 הבוט של רחלי")
    st.info("רחלי, שמת לב שהחודש הצלחת לחסוך יותר במזון? כל הכבוד!")

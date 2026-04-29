import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - נקי ומותאם למובייל
st.set_page_config(page_title="Rachel's Wealth", layout="wide", initial_sidebar_state="collapsed")

# --- עיצוב "יוקרה רכה": לילך, טורקיז ופנינה ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Assistant', sans-serif; text-align: right; direction: rtl; }
    
    .stApp { background-color: #F7F3FF; } /* רקע לילך בהיר מאוד */
    
    /* כרטיסיות לבנות מעוגלות */
    .card { 
        background: white; 
        padding: 20px; 
        border-radius: 25px; 
        box-shadow: 0 8px 20px rgba(108, 99, 255, 0.05);
        margin-bottom: 15px;
        border: 1px solid #EBE3FF;
    }
    
    /* כפתורים מעוצבים - סגול ממריץ */
    .stButton>button { 
        border-radius: 18px; 
        background: linear-gradient(135deg, #8E78FF 0%, #6C63FF 100%); 
        color: white; 
        font-weight: 600; 
        border: none;
        transition: 0.3s;
    }
    
    /* כפתור ה"+" הגדול */
    .plus-btn button {
        background: #38B2AC !important; /* טורקיז לכפתור ההוספה */
        font-size: 20px !important;
    }

    /* אייקונים בתחתית */
    .icon-card {
        background: white;
        border-radius: 20px;
        padding: 15px;
        text-align: center;
        border: 2px solid #F0EBFF;
        transition: 0.2s;
    }
    .icon-card:hover { border-color: #8E78FF; background: #F9F8FF; }
    
    /* כותרות */
    h1, h2, h3 { color: #4A3AFF; }
    </style>
    """, unsafe_allow_html=True)

# --- לוגיקה של זמנים ---
cycle_start = datetime(2026, 4, 15) 
days_passed = (datetime.now() - cycle_start).days
days_left = 14 - (days_passed % 14)

# --- כותרת עליונה ---
st.markdown('<h1 style="text-align: center;">העושר של רחלי 🦄</h1>', unsafe_allow_html=True)
st.markdown(f'<p style="text-align: center; color: #6C63FF;">נותרו <b>{days_left} ימים</b> לסיום הסבב</p>', unsafe_allow_html=True)

# --- דשבורד: איפה הכסף שלי? ---
st.markdown("### 💰 מצב הקופות")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="card"><p style="margin:0; font-size:14px; color:gray;">מזומן (Cash)</p><h2 style="margin:0;">$2,450</h2></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card"><p style="margin:0; font-size:14px; color:gray;">בנק (BofA)</p><h2 style="margin:0;">$4,100</h2></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="card"><p style="margin:0; font-size:14px; color:gray;">אשראי (Amex)</p><h2 style="margin:0; color:#FF4B4B;">$1,200-</h2></div>', unsafe_allow_html=True)

# --- יעד החיסכון הגדול ---
st.markdown("### 🎯 התקדמות ליעד ($20,000)")
st.progress(5800/20000)
st.markdown('<p style="text-align: left; font-size:12px;">נחסכו עד כה: $5,800</p>', unsafe_allow_html=True)

st.markdown("---")

# --- כפתור הוספה (טורקיז בולט) ---
st.markdown('<div class="plus-btn">', unsafe_allow_html=True)
with st.expander("➕ הוספת פעולה (הכנסה / הוצאה)", expanded=False):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    t_type = st.radio("מה קרה?", ["הוצאה 💸", "הכנסה 💰"], horizontal=True)
    
    c_a, c_b = st.columns(2)
    with c_a:
        t_wallet = st.selectbox("איך שילמתי/קיבלתי?", ["מזומן 💵", "Bank of America 🏦", "American Express 💳", "Food Stamps 🍎", "Pepper 🌶️"])
        t_amount = st.number_input("סכום ($)", min_value=0.0)
    with c_b:
        t_date = st.date_input("מתי?", datetime.now())
        if "הוצאה" in t_type:
            t_cat = st.selectbox("קטגוריה", ["צדקה ❤️", "רכב 🚗", "מזון 🥗", "דירה 🏠", "כללי 📦"])
        else:
            t_cat = st.selectbox("מקור", ["משכורת ישראל 🇮🇱", "משכורת רחלי 👩‍💻", "כללי ישראל 👴", "עצמאי רחלי ✍️", "כללי רחלי 🌍"])
    
    t_note = st.text_input("פירוט קצר (על מה?)")
    
    # חישוב פוד סטאמפס אוטומטי
    if "Food Stamps" in t_wallet:
        st.info(f"מחשב 75% ליתרה: ${t_amount * 0.75:.2f}")

    if st.button("שמור נתונים"):
        st.balloons()
        st.success("נשמר!")
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- גרפים להשוואה (ממוצע מול שבועיים) ---
st.markdown("### 📊 השוואת הוצאות")
g1, g2 = st.columns(2)
with g1:
    df_curr = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 200]})
    st.plotly_chart(px.pie(df_curr, values='Val', names='Cat', hole=0.6, title="בשבועיים האלו", color_discrete_sequence=px.colors.qualitative.Pastel), use_container_width=True)
with g2:
    df_avg = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [1500, 500, 1500, 1200, 400]})
    st.plotly_chart(px.pie(df_avg, values='Val', names='Cat', hole=0.6, title="ממוצע היסטורי", color_discrete_sequence=px.colors.qualitative.Safe), use_container_width=True)

# --- פירוט אייקונים מהיר ---
st.markdown("### 📂 פירוט לפי קטגוריות")
row1 = st.columns(5)
cats = [("🚗", "רכב"), ("🥗", "מזון"), ("❤️", "צדקה"), ("🏠", "דירה"), ("📦", "כללי")]
for i, (icon, name) in enumerate(cats):
    with row1[i]:
        st.markdown(f'<div class="icon-card"><div style="font-size:25px;">{icon}</div><div style="font-size:12px;">{name}</div></div>', unsafe_allow_html=True)

# --- תפריט צד (Sidebar) ---
with st.sidebar:
    st.markdown("## 🤖 העוזר האישי")
    st.info("רחלי, יש לך $2,450 במזומן. אולי כדאי לעשות Swap?")
    st.markdown("---")
    st.subheader("⚙️ הגדרות")
    st.number_input("עדכון יעד חיסכון ($)", value=20000)
    if st.button("📜 לצפייה בכל ההיסטוריה"):
        st.write("כאן תופיע הטבלה המלאה")
    

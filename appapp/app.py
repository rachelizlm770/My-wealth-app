import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - נקי ומותאם למובייל
st.set_page_config(page_title="Rachel's Wealth", layout="wide", initial_sidebar_state="collapsed")

# --- המהפך העיצובי: טורקיז, מנטה ורך ---
# צבעים נעימים: #38B2AC (טורקיז), #81E6D9 (מנטה בהיר), #F0F4F8 (רקע)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Assistant', sans-serif; text-align: right; direction: rtl; }
    
    /* רקע האפליקציה - רך ונעים */
    .stApp { background-color: #F0F4F8; }
    
    /* כרטיסיות צפות (Cards) - עגולות ורכות */
    .main-card { 
        background: white; 
        padding: 25px; 
        border-radius: 30px; /* עגול מאוד */
        box-shadow: 0 10px 25px rgba(0,0,0,0.03); /* צל עדין */
        margin-bottom: 20px; 
        border: 1px solid #E2E8F0; 
    }
    
    /* כפתורים - טורקיז מעוגל וממריץ */
    .stButton>button { 
        width: 100%; 
        border-radius: 20px; 
        height: 3.5em; 
        background: linear-gradient(135deg, #38B2AC 0%, #2C7A7B 100%); 
        color: white; 
        font-weight: 600; 
        font-size: 16px; 
        border: none; 
        box-shadow: 0 4px 10px rgba(44, 122, 123, 0.2);
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(44, 122, 123, 0.3);
    }
    
    /* אייקונים בתחתית - עיצוב רך וממריץ */
    .icon-box { 
        text-align: center; 
        padding: 20px; 
        border-radius: 25px; 
        background: white; 
        border: 1px solid #E2E8F0; 
        transition: 0.3s; 
        cursor: pointer; 
        min-height: 120px;
    }
    .icon-box:hover { 
        transform: translateY(-5px); 
        box-shadow: 0 12px 25px rgba(0,0,0,0.08); 
        background-color: #E6FFFA; /* צבע מנטה עדין ב-hover */
        border-color: #81E6D9;
    }
    .icon-symbol { font-size: 35px; margin-bottom: 10px; }
    .icon-text { color: #2D3748; font-weight: 600; font-size: 14px; }
    
    /* מדדי כסף (Metrics) */
    .metric-title { color: #718096; font-size: 15px; margin-bottom: 5px; }
    .metric-value { color: #1A202C; font-size: 28px; font-weight: 600; }
    
    /* טיפול בטקסט RTL בשדות */
    .stTextInput input, .stNumberInput input, .stSelectbox, .stTextArea textarea { text-align: right; direction: rtl; border-radius: 15px !important; }
    
    /* הסרת כותרות ברירת מחדל כדי לשמור על קו נקי */
    #rachel-s-wealth-by-racheli-izim { display: none; }
    </style>
    """, unsafe_allow_html=True)

# --- לוגיקה (סבב שבועיים) ---
# הערה: כשנחבר ל-Google Sheets, התאריך הזה יישמר שם
cycle_start = datetime(2026, 4, 15) 
days_since = (datetime.now() - cycle_start).days
days_left = 14 - (days_since % 14)

# --- דשבורד עליון (Dashboard) ---
# כותרת נעימה
st.markdown('<h1 style="color: #2C7A7B; text-align: right; margin-bottom: 0;">העושר שלי 💰</h1>', unsafe_allow_html=True)
st.caption(f"📊 סבב נוכחי: נותרו עוד {days_left} ימים לאיפוס השבועי")
st.markdown("<br>", unsafe_allow_html=True)

# כרטיסיות מצב הכסף - גדולות ורכות
col1, col2, col3, col4 = st.columns(4)
with col1: 
    st.markdown(f'<div class="main-card"><div class="metric-title">מזומן (Cash)</div><div class="metric-value">$2,450</div></div>', unsafe_allow_html=True)
with col2: 
    st.markdown(f'<div class="main-card"><div class="metric-title">בנק (BofA)</div><div class="metric-value">$4,100</div></div>', unsafe_allow_html=True)
with col3: 
    st.markdown(f'<div class="main-card"><div class="metric-title">אשראי (Amex)</div><div class="metric-value" style="color:#E53E3E;">$1,200-</div></div>', unsafe_allow_html=True)
with col4: 
    st.markdown(f'<div class="main-card"><div class="metric-title">נחסך ליעד </div><div class="metric-value" style="color:#38A169;">$5,800</div><div style="color: #718096; font-size: 13px;">מתוך: $20,000</div></div>', unsafe_allow_html=True)

# מד התקדמות (טורקיז)
st.progress(5800/20000)

st.markdown("<br>---<br>", unsafe_allow_html=True)

# --- כפתור הפלוס (הזנה) - כרטיסייה מעוגלת ורכה ---
with st.expander("➕ הוספת פעולה חדשה", expanded=False):
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    t_mode = st.radio("סוג הפעולה", ["הוצאה 💸", "הכנסה 💰"], horizontal=True)
    t_date = st.date_input("תאריך", datetime.now())
    t_wallet = st.selectbox("אמצעי תשלום", ["מזומן 💵", "Bank of America 🏦", "American Express 💳", "Food Stamps 🍎", "Pepper 🌶️"])
    
    if t_mode == "הוצאה 💸":
        t_cat = st.selectbox("סוג הוצאה", ["צדקה ❤️", "רכב 🚗", "מזון 🥗", "דירה 🏠", "כללי 📦"])
    else:
        t_cat = st.selectbox("מקור הכנסה", ["משכורת ישראל 👴", "משכורת רחלי 👩‍💻", "כללי ישראל 🇮🇱", "עצמאי רחלי ✍️", "כללי רחלי 🌍"])
    
    t_note = st.text_area("פירוט ההוצאה/הכנסה")
    t_amount = st.number_input("סכום ($)", min_value=0.0)
    
    # מנגנון פוד סטאמפס (75%)
    if "Food Stamps" in t_wallet:
        real_val = t_amount * 0.75
        st.info(f"חישוב אוטומטי (75%): הערך הריאלי שיורד מהתקציב הוא **${real_val:.2F}**")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("שמור פעולה ✅"):
        st.balloons()
        st.success("הנתון נשמר בהצלחה! הגיבוי מעודכן.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>---<br>", unsafe_allow_html=True)

# --- אייקונים אינטראקטיביים בתחתית - גדולים ורכים ---
st.markdown('<h3 style="color: #2C7A7B; text-align: right;">פירוט לפי קטגוריה</h3>', unsafe_allow_html=True)
st.write("לחצי על אייקון לצפייה בכל התנועות מסוג:")

# שורת הוצאות
st.markdown("#### הוצאות")
i1, i2, i3, i4, i5 = st.columns(5)
with i1: st.markdown('<div class="icon-box"><div class="icon-symbol">🚗</div><div class="icon-text">רכב</div></div>', unsafe_allow_html=True)
with i2: st.markdown('<div class="icon-box"><div class="icon-symbol">🥗</div><div class="icon-text">מזון</div></div>', unsafe_allow_html=True)
with i3: st.markdown('<div class="icon-box"><div class="icon-symbol">❤️</div><div class="icon-text">צדקה</div></div>', unsafe_allow_html=True)
with i4: st.markdown('<div class="icon-box"><div class="icon-symbol">🏠</div><div class="icon-text">דירה</div></div>', unsafe_allow_html=True)
with i5: st.markdown('<div class="icon-box"><div class="icon-symbol">📦</div><div class="icon-text">כללי</div></div>', unsafe_allow_html=True)

# שורת הכנסות
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("#### הכנסות")
in1, in2, in3, in4, in5 = st.columns(5)
with in1: st.markdown('<div class="icon-box"><div class="icon-symbol">🇮🇱</div><div class="icon-text">משכורת IL</div></div>', unsafe_allow_html=True)
with in2: st.markdown('<div class="icon-box"><div class="icon-symbol">👩‍💻</div><div class="icon-text">עצמאי</div></div>', unsafe_allow_html=True)
with in3: st.markdown('<div class="icon-box"><div class="icon-symbol">🌍</div><div class="icon-text">כללי רחלי</div></div>', unsafe_allow_html=True)
with in4: st.markdown('<div class="icon-box"><div class="icon-symbol">👴</div><div class="icon-text">ישראל</div></div>', unsafe_allow_html=True)
with in5: st.markdown('<div class="icon-box"><div class="icon-symbol">💼</div><div class="icon-text">כללי IL</div></div>', unsafe_allow_html=True)

# --- תפריט צד (Sidebar) מעוצב ---
with st.sidebar:
    st.markdown('<h1 style="color: #2C7A7B; text-align: right;">ניהול והגדרות</h1>', unsafe_allow_html=True)
    
    st.subheader("🤖 בוט AI האישי שלך")
    st.info("היי רחלי! שמת לב שרוב ההוצאות החריגות השבוע היו על רכב? כדאי לבדוק את זה.")
    st.markdown("---")
    
    st.subheader("הגדרות")
    goal_val = st.number_input("יעד חיסכון סופי ($)", value=20000)
    
    st.markdown("---")
    if st.button("📜 לצפייה בכל ההיסטוריה"):
        st.write("כאן תופיע הטבלה המלאה מהגיבוי")
    
# תזכורות מעוצבות
if 2450 > 1000:
    st.markdown("<br>", unsafe_allow_html=True)
    st.warning("💡 רחלי, יש לך $2,450 במזומן. זמן מצוין למצוא Swap!")

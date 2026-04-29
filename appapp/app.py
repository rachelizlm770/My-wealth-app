import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - מותאם למובייל
st.set_page_config(page_title="Rachel's Wealth", layout="wide", initial_sidebar_state="collapsed")

# עיצוב CSS יוקרתי ונקי (Direction RTL לעברית)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Assistant', sans-serif; text-align: right; direction: rtl; }
    .stApp { background-color: #F8F9FB; }
    .main-card { background: white; padding: 20px; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 15px; border: 1px solid #EEF2F6; }
    .stButton>button { width: 100%; border-radius: 15px; height: 3.5em; background: linear-gradient(135deg, #6C63FF 0%, #4B45B2 100%); color: white; font-weight: 600; border: none; }
    .icon-box { text-align: center; padding: 15px; border-radius: 20px; background: white; border: 1px solid #E2E8F0; transition: 0.3s; cursor: pointer; min-height: 100px; }
    .icon-box:hover { transform: translateY(-5px); box-shadow: 0 8px 20px rgba(0,0,0,0.1); background-color: #F1F5F9; }
    .metric-title { color: #718096; font-size: 14px; margin-bottom: 5px; }
    .metric-value { color: #1A202C; font-size: 24px; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# --- חישוב זמן (סבב שבועיים) ---
cycle_start = datetime(2026, 4, 15)
days_since = (datetime.now() - cycle_start).days
days_left = 14 - (days_since % 14)

# --- תפריט צד (Sidebar) ---
with st.sidebar:
    st.title("⚙️ הגדרות")
    goal_val = st.number_input("עדכון יעד חיסכון ($)", value=20000)
    st.markdown("---")
    st.subheader("🤖 הבוט של רחלי")
    st.info("היי רחלי! אני עוקב אחרי ההוצאות. שמת לב שבשבועיים האחרונים חסכת 15% יותר במזון?")
    st.markdown("---")
    if st.button("📜 היסטוריה ופירוט מלא"):
        st.write("כאן יוצגו כל הנתונים השמורים בגיבוי.")

# --- מסך ראשי ---
st.title("העושר של רחלי 💰")
st.write(f"📊 סבב נוכחי: נותרו עוד **{days_left} ימים** לאיפוס")

# כרטיסיות מצב הכסף
c1, c2, c3, c4 = st.columns(4)
with c1: st.markdown(f'<div class="main-card"><div class="metric-title">מזומן (Cash)</div><div class="metric-value">$2,450</div></div>', unsafe_allow_html=True)
with c2: st.markdown(f'<div class="main-card"><div class="metric-title">BofA</div><div class="metric-value">$4,100</div></div>', unsafe_allow_html=True)
with c3: st.markdown(f'<div class="main-card"><div class="metric-title">Amex (חוב)</div><div class="metric-value" style="color:#E53E3E;">$1,200</div></div>', unsafe_allow_html=True)
with c4: st.markdown(f'<div class="main-card"><div class="metric-title">נחסך ליעד</div><div class="metric-value" style="color:#38A169;">$5,800</div></div>', unsafe_allow_html=True)

st.progress(5800/goal_val)

# --- גרפים מרכזיים ---
st.markdown("### תמונת מצב")
g1, g2 = st.columns(2)
with g1:
    df_cycle = pd.DataFrame({'קטגוריה': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'סכום': [800, 300, 750, 1200, 250]})
    st.plotly_chart(px.pie(df_cycle, values='סכום', names='קטגוריה', hole=0.5, title="הוצאות הסבב"), use_container_width=True)
with g2:
    df_avg = pd.DataFrame({'קטגוריה': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'סכום': [1500, 500, 1500, 1200, 400]})
    st.plotly_chart(px.pie(df_avg, values='סכום', names='קטגוריה', hole=0.5, title="ממוצע היסטורי"), use_container_width=True)

# --- כפתור הפלוס (הזנה) ---
st.markdown("---")
with st.expander("➕ הוספת פעולה חדשה (הכנסה/הוצאה)", expanded=False):
    t_mode = st.radio("סוג", ["הוצאה", "הכנסה"], horizontal=True)
    t_date = st.date_input("תאריך", datetime.now())
    t_wallet = st.selectbox("אמצעי תשלום", ["מזומן", "Bank of America", "American Express", "Food Stamps", "Pepper"])
    
    if t_mode == "הוצאה":
        t_cat = st.selectbox("מקור הוצאה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
    else:
        t_cat = st.selectbox("מקור הכנסה", ["משכורת ישראל", "משכורת רחלי", "כללי ישראל", "עצמאי רחלי", "כללי רחלי"])
    
    t_note = st.text_area("פירוט ההוצאה/הכנסה")
    t_amount = st.number_input("סכום ($)", min_value=0.0)
    
    # חישוב פוד סטאמפס
    if t_wallet == "Food Stamps":
        st.info(f"ערך ריאלי לאחר חישוב (75%): ${t_amount * 0.75}")

    if st.button("שמור פעולה ✅"):
        st.balloons()
        st.success("הנתון נשמר בהצלחה!")

# --- אייקונים בתחתית ---
st.markdown("### פירוט מהיר")
st.write("לחצי על אייקון לראות מה יצא בבנק")
st.markdown("#### הוצאות")
i1, i2, i3, i4, i5 = st.columns(5)
i1.markdown('<div class="icon-box">🚗<br>רכב</div>', unsafe_allow_html=True)
i2.markdown('<div class="icon-box">🥗<br>מזון</div>', unsafe_allow_html=True)
i3.markdown('<div class="icon-box">❤️<br>צדקה</div>', unsafe_allow_html=True)
i4.markdown('<div class="icon-box">🏠<br>דירה</div>', unsafe_allow_html=True)
i5.markdown('<div class="icon-box">📦<br>כללי</div>', unsafe_allow_html=True)

st.markdown("#### הכנסות")
in1, in2, in3, in4, in5 = st.columns(5)
in1.markdown('<div class="icon-box">🇮🇱<br>משכורת IL</div>', unsafe_allow_html=True)
in2.markdown('<div class="icon-box">👩‍💻<br>משכורת רחלי</div>', unsafe_allow_html=True)
in3.markdown('<div class="icon-box">🌍<br>כללי רחלי</div>', unsafe_allow_html=True)
in4.markdown('<div class="icon-box">👴<br>ישראל</div>', unsafe_allow_html=True)
in5.markdown('<div class="icon-box">💼<br>עצמאי</div>', unsafe_allow_html=True)

# תזכורות
if 2450 > 1000:
    st.warning("💡 רחלי, יש לך $2,450 במזומן. אולי הגיע הזמן לעשות Swap ולהפקיד לבנק?")

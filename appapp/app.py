import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px

# הגדרות עיצוב - מראה נקי ויוקרתי
st.set_page_config(page_title="Rachel's Wealth", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #F8F9FB; }
    .stButton>button { width: 100%; border-radius: 25px; height: 3.5em; background-color: #6C63FF; color: white; font-weight: bold; border: none; }
    .metric-card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- כותרת ראשית ---
st.title("Rachel's Wealth 💰")

# --- נתונים זמניים (סימולציה) ---
# הערה: בשלב הבא נחבר את זה ל-Google Sheets שלך
target = 20000
saved_so_far = 5800
days_left = 10 

# --- דשבורד עליון ---
st.subheader(f"⏳ עוד {days_left} ימים לסיום הסבב")
col1, col2, col3, col4 = st.columns(4)

with col1: st.metric("מזומן (Cash)", "$2,450")
with col2: st.metric("בנק (BofA)", "$4,100")
with col3: st.metric("אשראי (Amex)", "$1,200", delta="- חוב נוכחי", delta_color="inverse")
with col4: st.metric("יעד כללי", f"${target}", delta=f"${saved_so_far} נחסכו")

st.progress(saved_so_far/target)

st.markdown("---")

# --- עוגות נתונים (ממוצע מול שבועיים) ---
c1, c2 = st.columns(2)
with c1:
    df_current = pd.DataFrame({'קטגוריה': ['רכב', 'אוכל', 'צדקה', 'דירה'], 'סכום': [800, 300, 750, 1200]})
    fig1 = px.pie(df_current, values='סכום', names='קטגוריה', title="הוצאות שבועיים אלו", hole=0.5, color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    df_avg = pd.DataFrame({'קטגוריה': ['רכב', 'אוכל', 'צדקה', 'דירה'], 'סכום': [1500, 500, 1500, 1200]})
    fig2 = px.pie(df_avg, values='סכום', names='קטגוריה', title="ממוצע היסטורי", hole=0.5)
    st.plotly_chart(fig2, use_container_width=True)

# --- כפתור הפלוס המרכזי ---
with st.expander("➕ הוספת תנועה (הכנסה/הוצאה)", expanded=False):
    t_type = st.radio("סוג", ["הוצאה", "הכנסה"], horizontal=True)
    t_date = st.date_input("תאריך", datetime.now())
    t_wallet = st.selectbox("אמצעי תשלום", ["Cash", "BofA", "Amex", "Food Stamps", "Pepper"])
    t_amount = st.number_input("סכום ($)", min_value=0.0)
    
    # חישוב פוד סטאמפס
    final_val = t_amount * 0.75 if t_wallet == "Food Stamps" else t_amount
    if t_wallet == "Food Stamps": st.caption(f"ערך לאחר חישוב (75%): ${final_val}")

    if t_type == "הוצאה":
        t_cat = st.selectbox("מקור הוצאה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
    else:
        t_cat = st.selectbox("מקור הכנסה", ["משכורת ישראל", "משכורת רחלי", "עצמאי רחלי", "כללי"])
    
    t_note = st.text_input("פירוט חופשי")
    
    if st.button("שמור נתונים ✅"):
        st.balloons()
        st.success("נשמר בהצלחה! הנתונים נשלחו לגיבוי.")

# --- תפריט צד (Sidebar) ---
with st.sidebar:
    st.header("⚙️ הגדרות")
    new_target = st.number_input("עדכון יעד חיסכון", value=target)
    st.color_picker("צבע אפליקציה", "#6C63FF")
    
    st.markdown("---")
    st.subheader("🤖 בוט בינה מלאכותית")
    st.info("היי רחלי! אני כאן לעזור. תרצי שאנתח את הוצאות הרכב שלך?")
    
    if st.button("📜 היסטוריה מלאה"):
        st.write("כאן תופיע רשימת כל התנועות שלך מה-Google Sheets")

# --- תזכורות חכמות ---
if 2450 > 1000:
    st.warning("💡 רחלי, יש לך הרבה מזומן ביד! אולי כדאי לעשות Swap?")

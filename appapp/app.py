import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import os

# הגדרות דף
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- פונקציות לניהול נתונים ---
DATA_FILE = "transactions.csv"

def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    return pd.DataFrame(columns=["date", "type", "amount", "wallet", "category", "description"])

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

# טעינת הנתונים בתחילת הריצה
if 'df' not in st.session_state:
    st.session_state.df = load_data()

# --- הזרקת CSS (אותו עיצוב יפה שלך עם תיקונים קלים) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    [data-testid="stHeader"], [data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] { display: none !important; }
    .stApp { background-color: #FFFFFF !important; }
    * { font-family: 'Assistant', sans-serif; direction: rtl; }
    
    /* העלמת ריבועי כפתורים ברירת מחדל */
    .stButton > button { background: transparent !important; border: none !important; color: transparent !important; box-shadow: none !important; padding: 0 !important; height: 0px !important; width: 0px !important; }

    /* עיצוב כפתור הפלוס וההגדרות */
    .fab-plus-visual { position: fixed; bottom: 35px; left: 35px; width: 70px; height: 70px; background-color: #008080; color: white !important; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 40px; z-index: 999; border: 4px solid white; box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
    .side-label-visual { position: fixed; top: 25%; right: 0; background-color: #008080; color: white; padding: 15px 8px; border-radius: 10px 0 0 10px; z-index: 999; writing-mode: vertical-rl; font-weight: 600; }

    /* שכבת הכפתורים האמיתית */
    button[key="real_plus_btn"] { position: fixed !important; bottom: 35px !important; left: 35px !important; width: 70px !important; height: 70px !important; z-index: 1000 !important; cursor: pointer !important; }
    button[key="real_settings_btn"] { position: fixed !important; top: 25% !important; right: 0 !important; width: 40px !important; height: 120px !important; z-index: 1000 !important; cursor: pointer !important; }

    div[data-testid="stMetric"] { background: #F4FBFB !important; border-radius: 15px !important; border-right: 5px solid #008080 !important; padding: 10px !important; }
    </style>
    <div class="side-label-visual">⚙️ הגדרות</div>
    <div class="fab-plus-visual">+</div>
    """, unsafe_allow_html=True)

# --- חלונות דיאלוג ---
@st.dialog("תנועה חדשה")
def show_transaction():
    st.markdown("### 📝 דיווח פעולה")
    t_mode = st.radio("סוג", ["הוצאה", "הכנסה"], horizontal=True)
    ca, cb = st.columns(2)
    with ca:
        t_amount = st.number_input("סכום", min_value=0.0)
        t_wallet = st.selectbox("חשבון", ["מזומן", "BofA", "Amex", "Pepper"])
    with cb:
        t_date = st.date_input("תאריך", datetime.now())
        t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
    t_desc = st.text_input("פירוט")
    
    if st.button("שמור נתונים", key="confirm_btn_actual"):
        new_data = {
            "date": t_date.strftime("%Y-%m-%d"),
            "type": t_mode,
            "amount": t_amount if t_mode == "הכנסה" else -t_amount,
            "wallet": t_wallet,
            "category": t_cat,
            "description": t_desc
        }
        st.session_state.df = pd.concat([st.session_state.df, pd.DataFrame([new_data])], ignore_index=True)
        save_data(st.session_state.df)
        st.success("נשמר בהצלחה!")
        st.rerun()

@st.dialog("הגדרות")
def show_settings():
    st.write("נתונים גולמיים:")
    st.dataframe(st.session_state.df)
    if st.button("מחק הכל"):
        st.session_state.df = pd.DataFrame(columns=["date", "type", "amount", "wallet", "category", "description"])
        save_data(st.session_state.df)
        st.rerun()

# הפעלת הכפתורים
if st.button("", key="real_settings_btn"): show_settings()
if st.button("", key="real_plus_btn"): show_transaction()

# --- תצוגת נתונים (Dashboard) ---
st.markdown('<h1 style="text-align: center; color: #004D4D;">Wealth Management</h1>', unsafe_allow_html=True)

# חישובים מהדאטה-פרייס
df = st.session_state.df
total_balance = df['amount'].sum() if not df.empty else 0
expenses_df = df[df['amount'] < 0].copy()
expenses_df['amount'] = expenses_df['amount'].abs()

# שורת מטריקות
m1, m2, m3 = st.columns(3)
with m1: st.metric("יתרה כוללת", f"${total_balance:,.0f}")
with m2: st.metric("הוצאות החודש", f"${expenses_df['amount'].sum():,.0f}")
with m3: st.metric("מספר תנועות", len(df))

# גרפים
if not expenses_df.empty:
    g1, g2 = st.columns(2)
    with g1:
        fig1 = px.pie(expenses_df, values='amount', names='category', hole=0.6, title="הוצאות לפי קטגוריה")
        st.plotly_chart(fig1, use_container_width=True)
    with g2:
        # גרף התפתחות יתרה לאורך זמן
        df['date'] = pd.to_datetime(df['date'])
        trend = df.sort_values('date').groupby('date')['amount'].sum().cumsum().reset_index()
        fig2 = px.line(trend, x='date', y='amount', title="מגמת הון עצמי")
        st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("עדיין אין נתונים להצגה. לחץ על ה-+ למטה כדי להוסיף תנועה!")

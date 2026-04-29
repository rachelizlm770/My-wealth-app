import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - ניקוי מוחלט
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- ניהול מצב (Session State) ---
if 'show_settings' not in st.session_state:
    st.session_state.show_settings = False

# --- הזרקת CSS לעיצוב יוקרתי ומחיקת הקו ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* 1. השמדת ה-Sidebar והקו מהשורש */
    section[data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"], [data-testid="stHeader"] {
        display: none !important;
        width: 0px !important;
    }
    .stApp { background-color: #FFFFFF !important; }
    * { font-family: 'Assistant', sans-serif; direction: rtl; }

    /* 2. תווית הגדרות ימנית מעוצבת */
    .side-label-fixed {
        position: fixed;
        top: 25%;
        right: 0;
        background-color: #3D5A5A;
        color: white;
        padding: 20px 12px;
        border-radius: 15px 0 0 15px;
        z-index: 9999;
        writing-mode: vertical-rl;
        text-orientation: mixed;
        font-weight: 600;
        font-size: 14px;
        box-shadow: -2px 4px 15px rgba(0,0,0,0.15);
        pointer-events: none;
    }

    /* 3. כפתור פלוס עגול ומרחף בשמאל */
    .stButton > button[key="plus_btn"] {
        position: fixed !important;
        bottom: 35px !important;
        left: 35px !important;
        width: 75px !important;
        height: 75px !important;
        background-color: #3D5A5A !important;
        color: white !important;
        border-radius: 50% !important;
        border: 4px solid white !important;
        font-size: 40px !important;
        box-shadow: 0 10px 25px rgba(61, 90, 90, 0.4) !important;
        z-index: 10000 !important;
    }

    /* 4. כפתור הפעלה שקוף לתווית הימנית */
    .stButton > button[key="label_btn"] {
        position: fixed !important;
        top: 25% !important;
        right: 0 !important;
        width: 50px !important;
        height: 140px !important;
        background: transparent !important;
        border: none !important;
        color: transparent !important;
        z-index: 10001 !important;
        cursor: pointer !important;
    }

    /* 5. כרטיסיות נתונים */
    div[data-testid="stMetric"] {
        background: #F9FBFB !important;
        border-radius: 20px !important;
        border-right: 10px solid #3D5A5A !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.02) !important;
    }
    div[data-testid="stMetricValue"] > div { color: #2A3F3F !important; font-weight: 700 !important; }
    </style>
    
    <div class="side-label-fixed">⚙️ הגדרות וכלים</div>
    """, unsafe_allow_html=True)

# --- פונקציות חלונות מרחפים ---

@st.dialog("שורת כלים והגדרות")
def show_settings_dialog():
    st.markdown("### 🛠️ תפריט ניהול")
    choice = st.radio("בחר פעולה:", ["🤖 בוט פיננסי", "📜 היסטוריה", "📦 ארכיון", "⚙️ הגדרות יעד"], label_visibility="collapsed")
    st.markdown("---")
    if choice == "⚙️ הגדרות יעד":
        st.number_input("עדכון יעד חיסכון", value=20000)
    elif choice == "🤖 בוט פיננסי":
        st.info("מוכן לניתוח הנתונים שלך.")
    
    if st.button("סגור תפריט", use_container_width=True):
        st.session_state.show_settings = False
        st.rerun()

@st.dialog("דיווח תנועה חדשה")
def show_transaction_dialog():
    st.markdown("<h3 style='color: #3D5A5A;'>📝 פרטי הפעולה</h3>", unsafe_allow_html=True)
    t_mode = st.radio("סוג פעולה", ["הוצאה", "הכנסה"], horizontal=True)
    
    ca, cb = st.columns(2)
    with ca:
        t_amount = st.number_input("סכום ($)", min_value=0.0, step=10.0)
        t_wallet = st.selectbox("חשבון / ארנק", ["מזומן", "BofA", "Amex", "Leumi", "Pepper"])
    with cb:
        t_date = st.date_input("תאריך", datetime.now())
        if t_mode == "הוצאה":
            t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
        else:
            t_cat = st.selectbox("מקור הכנסה", ["משכורת", "עצמאי", "אחר"])
    
    # הוספת אופציה לפרט - לבקשתך
    t_desc = st.text_area("לפרט כאן (תיאור הפעולה):", placeholder="למשל: קניות לשבת, תיקון פנצ'ר וכו'...")
            
    if st.button("אישור ושמירה", use_container_width=True):
        st.success(f"הפעולה נשמרה: {t_desc if t_desc else 'ללא פירוט'}")
        st.balloons()
        st.rerun()

# --- כפתורי הפעלה צפים ---

# כפתור שקוף על התווית הימנית
if st.button("", key="label_btn"):
    st.session_state.show_settings = True

# כפתור הפלוס בשמאל
if st.button("+", key="plus_btn"):
    show_transaction_dialog()

# הפעלת חלון הגדרות במידה ונלחץ
if st.session_state.show_settings:
    show_settings_dialog()

# --- תוכן דף הבית ---
st.markdown('<h1 style="text-align: center; color: #2A3F3F; font-size: 32px;">Wealth Management</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #666; margin-top: -15px;">Asset Tracking Dashboard</p>', unsafe_allow_html=True)

# דשבורד מספרים
st.markdown("<br>", unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m1: st.metric("Cash Balance", "$2,450")
with m2: st.metric("Bank Assets", "$4,100")
with m3: st.metric("Credit Debt", "-$1,200")

# גרפים בטורקיז בוגר
st.markdown("<br>", unsafe_allow_html=True)
g1, g2 = st.columns(2)
df_sample = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
colors = ['#3D5A5A', '#5E8080', '#83A3A3', '#ABC5C5', '#D4E4E4']

with g1:
    fig1 = px.pie(df_sample, values='Val', names='Cat', hole=0.7, title="הוצאות נוכחיות")
    fig1.update_traces(marker=dict(colors=colors), textinfo='label+value', textposition='outside')
    fig1.update_layout(showlegend=False, margin=dict(t=30, b=30, l=30, r=30), height=350)
    st.plotly_chart(fig1, use_container_width=True)

with g2:
    fig2 = px.pie(df_sample, values='Val', names='Cat', hole=0.7, title="ממוצע תקופתי")
    fig2.update_traces(marker=dict(colors=colors[::-1]), textinfo='label+value', textposition='outside')
    fig2.update_layout(showlegend=False, margin=dict(t=30, b=30, l=30, r=30), height=350)
    st.plotly_chart(fig2, use_container_width=True)

# שורת קטגוריות תחתונה
st.markdown("<br>", unsafe_allow_html=True)
row = st.columns(5)
for i, name in enumerate(["רכב", "מזון", "צדקה", "דירה", "כללי"]):
    with row[i]:
        st.markdown(f'<div style="text-align:center; background:#F0F7F7; padding:12px; border-radius:12px; border:1px solid #3D5A5A; color:#2A3F3F; font-weight:600; font-size:13px;">{name}</div>', unsafe_allow_html=True)

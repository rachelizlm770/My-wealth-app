import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - ניקוי מהשורש
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת CSS: צבעים ממריצים, אייקונים בוגרים וניקוי פסים ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* ניקוי רכיבי מערכת וקווים */
    [data-testid="stHeader"], [data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }
    .stApp { background-color: #FFFFFF !important; }
    * { font-family: 'Assistant', sans-serif; direction: rtl; }

    /* כרטיסיות נתונים - טורקיז בוגר */
    div[data-testid="stMetric"] {
        background: #F0F7F7 !important;
        border-radius: 20px !important;
        border-right: 8px solid #008080 !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.03) !important;
        padding: 20px !important;
    }
    div[data-testid="stMetricValue"] > div { color: #004D4D !important; font-weight: 700 !important; }

    /* תווית הגדרות ימנית צפה (Floating Tab) */
    .side-tab {
        position: fixed;
        top: 30%;
        right: 0;
        background-color: #008080;
        color: white;
        padding: 18px 8px;
        border-radius: 15px 0 0 15px;
        z-index: 9999;
        writing-mode: vertical-rl;
        text-orientation: mixed;
        font-weight: 600;
        font-size: 13px;
        box-shadow: -3px 0 15px rgba(0,0,0,0.1);
        pointer-events: none;
    }

    /* כפתור הפלוס הטורקיז המרחף (היחיד בשמאל) */
    .stButton > button[key="plus_btn"] {
        position: fixed !important;
        bottom: 35px !important;
        left: 35px !important;
        width: 75px !important;
        height: 75px !important;
        background-color: #008080 !important;
        color: white !important;
        border-radius: 50% !important;
        border: 4px solid white !important;
        font-size: 40px !important;
        box-shadow: 0 12px 30px rgba(0, 128, 128, 0.4) !important;
        z-index: 10000 !important;
    }

    /* כפתור שקוף על התווית הימנית */
    .stButton > button[key="label_trigger"] {
        position: fixed !important;
        top: 30% !important;
        right: 0 !important;
        width: 45px !important;
        height: 130px !important;
        background: transparent !important;
        border: none !important;
        color: transparent !important;
        z-index: 10001 !important;
    }

    /* עיצוב שורת אייקונים בוגרת */
    .icon-card {
        text-align: center;
        background: #F9F9F9;
        padding: 20px;
        border-radius: 18px;
        border: 1px solid #E6EDED;
        transition: 0.3s;
    }
    .icon-card:hover { border-color: #008080; background: #F0F7F7; }
    .icon-label { color: #004D4D; font-weight: 700; font-size: 14px; margin-top: 8px; }

    /* כותרות גרפים */
    .chart-header {
        color: #004D4D;
        font-weight: 700;
        text-align: center;
        font-size: 18px;
        margin-bottom: 5px;
    }
    </style>
    
    <div class="side-tab">⚙️ כלים והגדרות</div>
    """, unsafe_allow_html=True)

# --- פונקציות דיאלוג ---

@st.dialog("שורת כלים והגדרות")
def show_settings_menu():
    st.markdown("### 🛠️ ניהול חשבון")
    choice = st.radio("בחר פעולה:", ["🤖 בוט פיננסי", "📜 היסטוריה", "📦 ארכיון", "⚙️ הגדרות יעד"], label_visibility="collapsed")
    st.markdown("---")
    if choice == "⚙️ הגדרות יעד":
        st.number_input("עדכון יעד חיסכון", value=20000)
    elif choice == "🤖 בוט פיננסי":
        st.info("רחלי, הממשק נקי ומוכן לניתוח.")
    if st.button("סגור", use_container_width=True):
        st.rerun()

@st.dialog("דיווח תנועה חדשה")
def show_transaction_dialog():
    st.markdown("<h3 style='color: #008080;'>📝 פרטי הפעולה</h3>", unsafe_allow_html=True)
    t_mode = st.radio("סוג פעולה", ["הוצאה", "הכנסה"], horizontal=True)
    ca, cb = st.columns(2)
    with ca:
        t_amount = st.number_input("סכום ($)", min_value=0.0, step=10.0)
        t_wallet = st.selectbox("חשבון", ["מזומן", "BofA", "Amex", "Leumi", "Pepper"])
    with cb:
        t_date = st.date_input("תאריך", datetime.now())
        if t_mode == "הוצאה":
            t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
        else:
            t_cat = st.selectbox("מקור", ["משכורת", "עצמאי", "אחר"])
    
    st.text_area("פירוט (על מה?):", placeholder="הוסיפי תיאור כאן...")
            
    if st.button("אישור ושמירה", use_container_width=True):
        st.success("הפעולה נשמרה")
        st.balloons()
        st.rerun()

# --- תוכן דף הבית ---

# הפעלת תפריט מהתווית
if st.button(" ", key="label_trigger"):
    show_settings_menu()

st.markdown('<h1 style="text-align: center; color: #004D4D; font-size: 36px; margin-bottom: 0;">Wealth Management</h1>', unsafe_allow_html=True)

# שורת יעד ומטרה
col_goal = st.columns([1, 3, 1])
with col_goal[1]:
    current, goal = 12450, 20000
    st.markdown(f"<p style='text-align:center; color:#666; font-size:14px; margin-bottom: 5px;'>המטרה: <b>חיסכון שנתי</b> | מצב נוכחי: <b>${current:,} / ${goal:,}</b></p>", unsafe_allow_html=True)
    st.progress(current/goal)

# דשבורד מספרים
st.markdown("<br>", unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m1: st.metric("יתרה במזומן", "$2,450")
with m2: st.metric("נכסים בבנק", "$4,100")
with m3: st.metric("חובות אשראי", "-$1,200")

# גרפים מעוצבים
st.markdown("<br>", unsafe_allow_html=True)
g1, g2 = st.columns(2)
df_sample = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
colors = ['#008080', '#00A8A8', '#4DBDBD', '#99DEDE', '#E6F4F4']

with g1:
    st.markdown('<p class="chart-header">📊 פירוט הוצאות שבועי</p>', unsafe_allow_html=True)
    fig1 = px.pie(df_sample, values='Val', names='Cat', hole=0.7)
    fig1.update_traces(marker=dict(colors=colors), textinfo='label+value+percent', texttemplate='%{label}<br>$%{value}', textposition='outside')
    fig1.update_layout(showlegend=False, margin=dict(t=0, b=0, l=40, r=40), height=320)
    st.plotly_chart(fig1, use_container_width=True)

with g2:
    st.markdown('<p class="chart-header">📈 ממוצע דו-שבועי כללי</p>', unsafe_allow_html=True)
    fig2 = px.pie(df_sample, values='Val', names='Cat', hole=0.7)
    fig2.update_traces(marker=dict(colors=colors[::-1]), textinfo='label+value+percent', texttemplate='%{label}<br>$%{value}', textposition='outside')
    fig2.update_layout(showlegend=False, margin=dict(t=0, b=0, l=40, r=40), height=320)
    st.plotly_chart(fig2, use_container_width=True)

# שורת אייקונים בוגרת
st.markdown("<br>", unsafe_allow_html=True)
row_icons = st.columns(5)
items = [("🔹", "רכב"), ("🔸", "מזון"), ("⬥", "צדקה"), ("⬩", "דירה"), ("▪", "כללי")]

for i, (icon, name) in enumerate(items):
    with row_icons[i]:
        st.markdown(f'<div class="icon-card"><div style="font-size: 22px;">{icon}</div><div class="icon-label">{name}</div></div>', unsafe_allow_html=True)

# כפתור הפלוס הצף (דיווח תנועה)
if st.button("+", key="plus_btn"):
    show_transaction_dialog()

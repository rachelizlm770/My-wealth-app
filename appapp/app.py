import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת CSS: צבעים בוגרים ועיצוב SaaS נקי ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* 1. מחיקת רכיבי מערכת וקווים */
    [data-testid="stHeader"], [data-testid="stSidebarResizer"] { display: none !important; }
    .stApp { background-color: #FFFFFF !important; }
    * { font-family: 'Assistant', sans-serif; direction: rtl; }
    
    /* חיסול הקו באמצע - פקודה אגרסיבית */
    [data-testid="stSidebar"] { border: none !important; box-shadow: none !important; }
    .st-emotion-cache-16idsys, .st-emotion-cache-6q9sum { border: none !important; }

    /* 2. תווית הגדרות מצד ימין (בוגרת ויוקרתית) */
    .side-label-right {
        position: fixed;
        top: 25%;
        right: 0;
        background-color: #2C5F5F; /* טורקיז עמוק בוגר */
        color: white;
        padding: 20px 8px;
        border-radius: 12px 0 0 12px;
        cursor: pointer;
        z-index: 999998;
        writing-mode: vertical-rl;
        text-orientation: mixed;
        font-weight: 600;
        font-size: 14px;
        box-shadow: -2px 4px 15px rgba(0,0,0,0.1);
    }

    /* 3. כפתור פלוס דומיננטי בשמאל */
    div.stButton > button:first-child {
        position: fixed !important;
        bottom: 40px !important;
        left: 40px !important;
        width: 80px !important;
        height: 80px !important;
        background-color: #2C5F5F !important;
        color: white !important;
        border-radius: 50% !important;
        border: 4px solid white !important;
        font-size: 45px !important;
        box-shadow: 0 12px 30px rgba(44, 95, 95, 0.3) !important;
        z-index: 999999 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* 4. כרטיסיות נתונים (בוגרות) */
    div[data-testid="stMetric"] {
        background: #F8FBFB !important;
        border-radius: 20px !important;
        border-right: 8px solid #2C5F5F !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.02) !important;
        padding: 20px !important;
    }
    div[data-testid="stMetricValue"] > div { color: #1B4343 !important; font-weight: 700 !important; }

    /* 5. עיצוב חלון מרחף */
    div[data-testid="stDialog"] { border-radius: 25px !important; direction: rtl !important; }
    </style>
    """, unsafe_allow_html=True)

# --- חלון צד (Sidebar) ---
with st.sidebar:
    st.markdown("<h2 style='color: #2C5F5F;'>שורת כלים</h2>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("ניווט", ["🏠 דף בית", "🤖 בוט פיננסי", "📜 היסטוריה", "📦 ארכיון", "⚙️ הגדרות"])
    
    if menu == "⚙️ הגדרות":
        st.number_input("יעד חיסכון", value=20000)
    elif menu == "🤖 בוט פיננסי":
        st.info("רחלי, הממשק עודכן לצבעים בוגרים יותר.")

# --- דיאלוג "תנועה חדשה" ---
@st.dialog("דיווח תנועה חדשה")
def show_transaction_dialog():
    st.markdown("<h3 style='color: #2C5F5F;'>📝 פרטי הפעולה</h3>", unsafe_allow_html=True)
    t_mode = st.radio("סוג פעולה", ["הוצאה", "הכנסה"], horizontal=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        t_amount = st.number_input("סכום ($)", min_value=0.0, step=10.0)
        t_wallet = st.selectbox("חשבון / ארנק", ["מזומן", "BofA", "Amex", "Leumi", "Pepper"])
    with col_b:
        t_date = st.date_input("תאריך", datetime.now())
        if t_mode == "הוצאה":
            t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
        else:
            t_cat = st.selectbox("מקור הכנסה", ["משכורת ישראל", "משכורת רחלי", "עצמאי", "אחר"])
            
    if st.button("אישור ושמירה", use_container_width=True):
        st.balloons()
        st.rerun()

# --- תוכן דף הבית ---
st.markdown('<h1 style="text-align: center; color: #1B4343; font-size: 32px;">Wealth Management</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #666; margin-top: -15px;">Asset Tracking Dashboard</p>', unsafe_allow_html=True)

# דשבורד
st.markdown("<br>", unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m1: st.metric("Cash Balance", "$2,450")
with m2: st.metric("Bank Assets", "$4,100")
with m3: st.metric("Credit Debt", "-$1,200")

# גרפים בטורקיז עמוק וירוק מרווה
st.markdown("<br>", unsafe_allow_html=True)
g_col1, g_col2 = st.columns(2)
df_sample = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
# פלטת צבעים בוגרת
colors = ['#2C5F5F', '#4E8B8B', '#76A5A5', '#A2C1C1', '#CDE0E0']

with g_col1:
    fig1 = px.pie(df_sample, values='Val', names='Cat', hole=0.7, title="הוצאות נוכחיות")
    fig1.update_traces(marker=dict(colors=colors), textinfo='label+value+percent', texttemplate='%{label}<br>$%{value}<br>%{percent}', textposition='outside')
    fig1.update_layout(showlegend=False, margin=dict(t=50, b=50, l=50, r=50), height=380)
    st.plotly_chart(fig1, use_container_width=True)

with g_col2:
    fig2 = px.pie(df_sample, values='Val', names='Cat', hole=0.7, title="ממוצע תקופתי")
    fig2.update_traces(marker=dict(colors=colors[::-1]), textinfo='label+value+percent', texttemplate='%{label}<br>$%{value}<br>%{percent}', textposition='outside')
    fig2.update_layout(showlegend=False, margin=dict(t=50, b=50, l=50, r=50), height=380)
    st.plotly_chart(fig2, use_container_width=True)

# --- אלמנטים צפים ---

# 1. תווית הגדרות ימנית
st.markdown('<div class="side-label-right">⚙️ הגדרות וכלים</div>', unsafe_allow_html=True)

# 2. כפתור פלוס
if st.button("+"):
    show_transaction_dialog()

# שורת קטגוריות
st.markdown("<br>", unsafe_allow_html=True)
row = st.columns(5)
for i, name in enumerate(["רכב", "מזון", "צדקה", "דירה", "כללי"]):
    with row[i]:
        st.markdown(f'<div style="text-align:center; background:#F0F7F7; padding:12px; border-radius:12px; border:1px solid #2C5F5F; color:#1B4343; font-weight:600; font-size:13px;">{name}</div>', unsafe_allow_html=True)

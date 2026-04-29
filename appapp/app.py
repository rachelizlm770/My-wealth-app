import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - ניקוי מוחלט
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת CSS לעיצוב יוקרתי (SaaS Style) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* 1. הסתרת רכיבי מערכת */
    [data-testid="stHeader"] { display: none !important; }
    .stApp { background-color: #FFFFFF !important; }
    * { font-family: 'Assistant', sans-serif; direction: rtl; }

    /* 2. תווית הגדרות שיוצאת מהצד (Floating Label) */
    .side-label {
        position: fixed;
        top: 20%;
        left: 0;
        background-color: #00D2D3;
        color: white;
        padding: 15px 10px;
        border-radius: 0 10px 10px 0;
        cursor: pointer;
        z-index: 999998;
        writing-mode: vertical-rl;
        text-orientation: mixed;
        font-weight: 700;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        transition: 0.3s;
    }
    .side-label:hover { padding-left: 20px; background-color: #00BABA; }

    /* 3. כפתור פלוס דומיננטי ומרחף */
    div.stButton > button:first-child {
        position: fixed !important;
        bottom: 40px !important;
        left: 40px !important;
        width: 85px !important;
        height: 85px !important;
        background-color: #00D2D3 !important;
        color: white !important;
        border-radius: 50% !important;
        border: 5px solid white !important;
        font-size: 50px !important;
        box-shadow: 0 15px 35px rgba(0, 210, 211, 0.4) !important;
        z-index: 999999 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        transition: transform 0.2s;
    }
    div.stButton > button:first-child:hover { transform: scale(1.1); }

    /* 4. עיצוב כרטיסיות נתונים */
    div[data-testid="stMetric"] {
        background: #F4FBFB !important;
        border-radius: 25px !important;
        border-right: 10px solid #00D2D3 !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.03) !important;
        padding: 20px !important;
    }
    div[data-testid="stMetricValue"] > div { color: #008080 !important; font-weight: 700 !important; }

    /* 5. עיצוב חלון מרחף (Dialog) */
    div[data-testid="stDialog"] { border-radius: 30px !important; direction: rtl !important; }
    </style>
    """, unsafe_allow_html=True)

# --- חלון צד (Sidebar) - כלים והגדרות ---
with st.sidebar:
    st.markdown("## 🛠️ שורת כלים")
    st.markdown("---")
    menu = st.radio("ניווט", ["🏠 דף בית", "🤖 בוט פיננסי", "📜 היסטוריה", "📦 ארכיון", "⚙️ הגדרות"])
    
    if menu == "⚙️ הגדרות":
        st.subheader("הגדרות")
        st.number_input("יעד חיסכון", value=20000)
    elif menu == "📜 היסטוריה":
        st.write("כאן תופיע רשימת התנועות האחרונות...")
    elif menu == "🤖 בוט פיננסי":
        st.info("רחלי, אני כאן לנתח את הנתונים שלך.")

# --- דיאלוג "תנועה חדשה" (נפתח רק מהפלוס) ---
@st.dialog("דיווח תנועה חדשה")
def show_transaction_dialog():
    st.markdown("### 📝 פרטי הפעולה")
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
            
    t_desc = st.text_input("הערות (אופציונלי)")
    
    if st.button("אישור ושמירה", use_container_width=True):
        st.balloons()
        st.success("הפעולה נשמרה בהצלחה!")
        st.rerun()

# --- תוכן דף הבית (נקי לחלוטין) ---
st.markdown('<h1 style="text-align: center; color: #008080; font-size: 35px;">Wealth Management</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #888; margin-top: -20px;">Asset Tracking Dashboard</p>', unsafe_allow_html=True)

# דשבורד מרכזי
st.markdown("<br>", unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m1: st.metric("Cash Balance", "$2,450")
with m2: st.metric("Bank Assets", "$4,100")
with m3: st.metric("Credit Debt", "-$1,200")

# גרפים בטורקיז וירוק
st.markdown("<br>", unsafe_allow_html=True)
g_col1, g_col2 = st.columns(2)
df_sample = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
colors = ['#00D2D3', '#1DD1A1', '#10AC84', '#00B894', '#55E6C1']

with g_col1:
    fig1 = px.pie(df_sample, values='Val', names='Cat', hole=0.7, title="הוצאות לפי קטגוריה")
    fig1.update_traces(marker=dict(colors=colors), textinfo='label+value+percent', texttemplate='%{label}<br>$%{value}<br>%{percent}', textposition='outside')
    fig1.update_layout(showlegend=False, margin=dict(t=50, b=50, l=50, r=50), height=400)
    st.plotly_chart(fig1, use_container_width=True)

with g_col2:
    fig2 = px.pie(df_sample, values='Val', names='Cat', hole=0.7, title="מגמה תקופתית")
    fig2.update_traces(marker=dict(colors=colors[::-1]), textinfo='label+value+percent', texttemplate='%{label}<br>$%{value}<br>%{percent}', textposition='outside')
    fig2.update_layout(showlegend=False, margin=dict(t=50, b=50, l=50, r=50), height=400)
    st.plotly_chart(fig2, use_container_width=True)

# --- כפתורים צפים (SaaS UI) ---

# 1. תווית הגדרות צדדית (HTML בלבד)
st.markdown('<div class="side-label">⚙️ הגדרות וכלים</div>', unsafe_allow_html=True)

# 2. כפתור הפלוס (מפעיל את הדיאלוג)
if st.button("+"):
    show_transaction_dialog()

# שורת קטגוריות מעוצבת בתחתית
st.markdown("<br>", unsafe_allow_html=True)
row = st.columns(5)
for i, name in enumerate(["רכב", "מזון", "צדקה", "דירה", "כללי"]):
    with row[i]:
        st.markdown(f'<div style="text-align:center; background:#EFFFFF; padding:15px; border-radius:15px; border:1px solid #00D2D3; color:#008080; font-weight:700;">{name}</div>', unsafe_allow_html=True)

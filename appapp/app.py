import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת CSS: טורקיז, ירוק וכפתורים צפים ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* ניקוי כללי */
    [data-testid="stHeader"] { display: none !important; }
    .stApp { background-color: #FFFFFF !important; }
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }

    /* כרטיסיות נתונים בטורקיז */
    div[data-testid="stMetric"] {
        background: #F0F9F9 !important;
        border-radius: 20px !important;
        border-right: 8px solid #00D2D3 !important; /* טורקיז */
        box-shadow: 0 10px 25px rgba(0,0,0,0.05) !important;
    }
    div[data-testid="stMetricValue"] > div { color: #008080 !important; }

    /* כפתור הפלוס הטורקיז המרחף */
    div.stButton > button:first-child {
        position: fixed !important;
        bottom: 30px !important;
        left: 30px !important;
        width: 70px !important;
        height: 70px !important;
        background-color: #00D2D3 !important; /* טורקיז */
        color: white !important;
        border-radius: 50% !important;
        border: 3px solid white !important;
        font-size: 40px !important;
        box-shadow: 0 10px 30px rgba(0, 210, 211, 0.4) !important;
        z-index: 99999 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* אייקון הגדרות בפינה למעלה */
    .top-settings {
        position: fixed;
        top: 20px;
        left: 20px;
        z-index: 100000;
    }
    </style>
    """, unsafe_allow_html=True)

# --- חלון צד להגדרות (Sidebar) ---
with st.sidebar:
    st.markdown("### ⚙️ הגדרות מערכת")
    st.number_input("יעד חיסכון שנתי", value=20000)
    st.markdown("---")
    st.markdown("### 🤖 הבוט של רחלי")
    st.info("רחלי, הממשק עבר לצבעי טורקיז וירוק כפי שביקשת!")

# --- דיאלוג הוספת תנועה ---
@st.dialog("רישום פעולה חדשה")
def show_transaction():
    t_mode = st.radio("סוג", ["הוצאה", "הכנסה"], horizontal=True)
    ca, cb = st.columns(2)
    with ca:
        t_amount = st.number_input("סכום ($)", min_value=0.0)
        t_wallet = st.selectbox("חשבון", ["מזומן", "BofA", "Amex", "Leumi", "Pepper"])
    with cb:
        t_date = st.date_input("תאריך", datetime.now())
        t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
    if st.button("שמור", use_container_width=True):
        st.balloons()
        st.rerun()

# --- תוכן דף הבית ---
st.markdown('<h1 style="text-align: center; color: #008080;">Wealth Management</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #666; margin-top: -15px;">Asset Tracking | רחלי</p>', unsafe_allow_html=True)

# דשבורד בטורקיז
c1, c2, c3 = st.columns(3)
with c1: st.metric("Cash", "$2,450")
with c2: st.metric("BofA", "$4,100")
with c3: st.metric("Amex", "-$1,200")

# גרפים בטורקיז וירוק
st.markdown("<br>", unsafe_allow_html=True)
col_g1, col_g2 = st.columns(2)
df = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
# פלטת צבעים ירוק-טורקיז
green_turquoise_palette = ['#00D2D3', '#1DD1A1', '#10AC84', '#00B894', '#55E6C1']

with col_g1:
    fig1 = px.pie(df, values='Val', names='Cat', hole=0.7, title="פירוט הוצאות")
    fig1.update_traces(
        marker=dict(colors=green_turquoise_palette),
        textinfo='label+value+percent',
        texttemplate='%{label}<br>$%{value}<br>%{percent}',
        textposition='outside'
    )
    fig1.update_layout(showlegend=False, margin=dict(t=50, b=50, l=50, r=50), height=350)
    st.plotly_chart(fig1, use_container_width=True)

with col_g2:
    fig2 = px.pie(df, values='Val', names='Cat', hole=0.7, title="ממוצע חודשי")
    fig2.update_traces(
        marker=dict(colors=green_turquoise_palette[::-1]),
        textinfo='label+value+percent',
        texttemplate='%{label}<br>$%{value}<br>%{percent}',
        textposition='outside'
    )
    fig2.update_layout(showlegend=False, margin=dict(t=50, b=50, l=50, r=50), height=350)
    st.plotly_chart(fig2, use_container_width=True)

# כפתור הפלוס (מרחף למטה)
if st.button("+"):
    show_transaction()

# כפתור הגדרות (למעלה שפותח את ה-Sidebar)
st.markdown('<div class="top-settings">', unsafe_allow_html=True)
if st.button("⚙️"):
    # ב-Streamlit, לחיצה על כפתור כשיש Sidebar פשוט תציג אותו אם הוא היה סגור
    st.write("הגדרות פתוחות בצד")
st.markdown('</div>', unsafe_allow_html=True)

# קטגוריות
st.markdown("<br>", unsafe_allow_html=True)
row_icons = st.columns(5)
for i, name in enumerate(["רכב", "מזון", "צדקה", "דירה", "כללי"]):
    with row_icons[i]:
        st.markdown(f'<div style="text-align:center; background:#EFFFFF; padding:10px; border-radius:10px; border:1px solid #00D2D3; color:#008080; font-weight:700;">{name}</div>', unsafe_allow_html=True)

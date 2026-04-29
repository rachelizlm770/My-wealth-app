import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת CSS "The Float Master" ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* 1. ניקוי מוחלט של מערכת Streamlit */
    section[data-testid="stSidebar"], [data-testid="stHeader"], .st-emotion-cache-16idsys, [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }
    
    .stApp { background-color: #FFFFFF !important; }
    .block-container { padding: 1rem !important; max-width: 100% !important; }
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }
    
    /* 2. עיצוב כפתור הפלוס הסגול (כפתור רגיל בתוך Streamlit) */
    div.stButton > button {
        position: fixed !important;
        bottom: 30px !important;
        left: 30px !important;
        width: 70px !important;
        height: 70px !important;
        background-color: #4A3AFF !important;
        color: white !important;
        border-radius: 50% !important;
        border: 3px solid white !important;
        font-size: 40px !important;
        box-shadow: 0 10px 30px rgba(74, 58, 255, 0.5) !important;
        z-index: 999999 !important;
        padding: 0px !important;
        line-height: 1 !important;
    }

    /* 3. עיצוב כפתור הגדרות בנפרד (למעלה) */
    .settings-layer {
        position: fixed;
        top: 20px;
        left: 20px;
        z-index: 1000000;
    }
    
    .settings-layer button {
        background-color: #F8F9FA !important;
        border-radius: 50% !important;
        width: 45px !important;
        height: 45px !important;
        border: 1px solid #DDD !important;
        color: #4A3AFF !important;
        position: static !important; /* מבטל את הציפה של ה-CSS הכללי למעלה */
    }

    /* 4. כרטיסיות נתונים */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border-radius: 20px !important;
        border: 1px solid #F0F0F5 !important;
        border-right: 8px solid #4A3AFF !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.03) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- חלונות מרחפים ---
@st.dialog("תיעוד פעולה")
def show_transaction_form():
    st.write("### הוספת פעולה")
    t_mode = st.radio("סוג", ["הוצאה", "הכנסה"], horizontal=True)
    ca, cb = st.columns(2)
    with ca:
        t_wallet = st.selectbox("חשבון", ["מזומן", "BofA", "Amex", "Food Stamps", "Pepper", "Leumi"])
        t_amount = st.number_input("סכום ($)", min_value=0.0)
    with cb:
        t_date = st.date_input("תאריך", datetime.now())
        t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
    if st.button("שמור", use_container_width=True):
        st.balloons()
        st.rerun()

@st.dialog("הגדרות")
def show_settings():
    st.subheader("⚙️ הגדרות")
    st.number_input("יעד חיסכון", value=20000)

# --- תוכן האפליקציה ---
st.markdown('<h1 style="text-align: center; font-size: 28px;">Wealth Management</h1>', unsafe_allow_html=True)

# דשבורד
c1, c2, c3 = st.columns(3)
with c1: st.metric("Cash", "$2,450")
with c2: st.metric("BofA", "$4,100")
with c3: st.metric("Amex", "-$1,200")

# גרפים
st.markdown("<br>", unsafe_allow_html=True)
col_g1, col_g2 = st.columns(2)
df = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
purple_palette = ['#4A3AFF', '#6C63FF', '#8E86FF', '#B0AAFF', '#D2CFFF']

with col_g1:
    fig1 = px.pie(df, values='Val', names='Cat', hole=0.7, title="פירוט סבב")
    fig1.update_traces(
        marker=dict(colors=purple_palette),
        textinfo='label+value+percent',
        texttemplate='%{label}<br>$%{value}<br>%{percent}',
        textfont_size=11
    )
    fig1.update_layout(showlegend=False, margin=dict(t=40, b=0, l=0, r=0), height=280)
    st.plotly_chart(fig1, use_container_width=True)

with col_g2:
    fig2 = px.pie(df, values='Val', names='Cat', hole=0.7, title="ממוצע היסטורי")
    fig2.update_traces(
        marker=dict(colors=purple_palette[::-1]),
        textinfo='label+value+percent',
        texttemplate='%{label}<br>$%{value}<br>%{percent}',
        textfont_size=11
    )
    fig2.update_layout(showlegend=False, margin=dict(t=40, b=0, l=0, r=0), height=280)
    st.plotly_chart(fig2, use_container_width=True)

# כפתור הפלוס (בגלל העיצוב הוא יצוף תמיד למטה משמאל)
if st.button("+"):
    show_transaction_form()

# כפתור ההגדרות (עטוף בתוך דיב שיציף אותו למעלה)
st.markdown('<div class="settings-layer">', unsafe_allow_html=True)
if st.button("⚙️", key="settings"):
    show_settings()
st.markdown('</div>', unsafe_allow_html=True)

# קטגוריות
st.markdown("<br>", unsafe_allow_html=True)
row_icons = st.columns(5)
for name in ["רכב", "מזון", "צדקה", "דירה", "כללי"]:
    with row_icons.pop(0):
        st.markdown(f'<div style="text-align:center; background:#FDFDFF; padding:10px; border-radius:10px; border:1px solid #F0F0F5; color:#5A52CB; font-weight:700; font-size:12px;">{name}</div>', unsafe_allow_html=True)

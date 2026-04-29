import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - ביטול מוחלט של הסרגל הצידי
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת CSS "The Purge" - מחיקה פיזית של כל אזור ה-Sidebar ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* 1. מחיקה מוחלטת של ה-Sidebar והדרים מהשורש */
    section[data-testid="stSidebar"] { display: none !important; width: 0 !important; }
    [data-testid="stSidebarCollapsedControl"] { display: none !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    /* 2. ניקוי העמוד והגדרת רקע לבן */
    .stApp { background-color: #FFFFFF !important; }
    .block-container { 
        padding: 1.5rem !important; 
        max-width: 100% !important; 
        margin: 0 !important;
    }
    
    /* 3. פונט Assistant ויישור לימין */
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }
    
    /* 4. כרטיסיות נתונים נקיות */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border-radius: 15px !important;
        padding: 20px !important;
        border: 1px solid #F0F0F5 !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.02) !important;
        border-right: 5px solid #4A3AFF !important;
        margin-bottom: 10px !important;
    }
    div[data-testid="stMetricValue"] > div { color: #4A3AFF !important; font-size: 30px !important; font-weight: 700 !important; }

    /* 5. כפתורי צפה (FAB) - אחד לפלוס ואחד להגדרות */
    .fab-plus {
        position: fixed !important; bottom: 30px !important; left: 30px !important;
        width: 65px; height: 65px; background: #4A3AFF; color: white !important;
        border-radius: 50%; display: flex; align-items: center; justify-content: center;
        font-size: 35px; box-shadow: 0 8px 20px rgba(74, 58, 255, 0.3);
        z-index: 9999; border: 2px solid white; cursor: pointer; text-decoration: none !important;
    }
    .fab-settings {
        position: fixed !important; top: 20px !important; left: 20px !important;
        width: 45px; height: 45px; background: #F8F9FA; color: #4A3AFF !important;
        border-radius: 50%; display: flex; align-items: center; justify-content: center;
        font-size: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        z-index: 9998; border: 1px solid #EEE; cursor: pointer; text-decoration: none !important;
    }

    /* 6. אייקונים בוגרים בתחתית */
    .cat-box {
        background-color: #FDFDFF !important; border-radius: 12px !important;
        padding: 12px !important; text-align: center !important; border: 1px solid #F0F0F5 !important;
    }
    .cat-label { color: #5A52CB !important; font-size: 12px !important; font-weight: 700 !important; }
    
    /* תיקון דיאלוג */
    div[data-testid="stDialog"] { direction: rtl !important; }
    </style>
    
    <a href="#settings" class="fab-settings">⚙️</a>
    """, unsafe_allow_html=True)

# --- פונקציית תיעוד פעולה ---
@st.dialog("תיעוד פעולה חדשה")
def show_transaction_form():
    t_mode = st.radio("סוג פעולה", ["הוצאה", "הכנסה"], horizontal=True)
    ca, cb = st.columns(2)
    with ca:
        t_wallet = st.selectbox("חשבון", ["מזומן", "BofA", "Amex", "Food Stamps", "Pepper", "Leumi"])
        t_amount = st.number_input("סכום ($)", min_value=0.0, step=10.0)
    with cb:
        t_date = st.date_input("תאריך", datetime.now())
        if t_mode == "הוצאה":
            t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
        else:
            t_cat = st.selectbox("מקור", ["משכורת ישראל", "משכורת רחלי", "כללי ישראל", "עצמאי רחלי", "כללי רחלי"])
    t_desc = st.text_input("פירוט")
    if st.button("שמור נתונים", use_container_width=True):
        st.success("נשמר!")
        st.rerun()

# --- פונקציית הגדרות ובוט ---
@st.dialog("הגדרות ובוט AI")
def show_settings():
    st.subheader("⚙️ הגדרות אפליקציה")
    st.number_input("יעד חיסכון", value=20000)
    st.markdown("---")
    st.subheader("🤖 הבוט של רחלי")
    st.info("רחלי, הממשק עכשיו נקי לחלוטין ללא סרגל צידי. הכל עובד חלק!")

# --- תוכן דף הבית ---
st.markdown('<h1 style="text-align: center; font-size: 28px; color: #1A1A2E;">Wealth Management</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #716B94; margin-top: -15px; font-size: 14px;">Asset Tracking | רחלי</p>', unsafe_allow_html=True)

# דשבורד
c1, c2, c3 = st.columns(3)
with c1: st.metric("Cash", "$2,450")
with c2: st.metric("BofA", "$4,100")
with c3: st.metric("Amex", "-$1,200")

# מד התקדמות
st.progress(5800/20000)
st.markdown('<p style="font-size: 12px; color: #716B94; text-align: center;">נחסכו: $5,800 מתוך $20,000</p>', unsafe_allow_html=True)

# גרפים
st.markdown("<br>", unsafe_allow_html=True)
col_g1, col_g2 = st.columns(2)
purple_palette = ['#4A3AFF', '#6C63FF', '#8E86FF', '#B0AAFF', '#D2CFFF']

with col_g1:
    df1 = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
    fig1 = px.pie(df1, values='Val', names='Cat', hole=0.8)
    fig1.update_traces(marker=dict(colors=purple_palette), textinfo='none')
    fig1.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0), height=180)
    st.plotly_chart(fig1, use_container_width=True, config={'displayModeBar': False})

with col_g2:
    df2 = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [1500, 500, 1500, 1200, 400]})
    fig2 = px.pie(df2, values='Val', names='Cat', hole=0.8)
    fig2.update_traces(marker=dict(colors=purple_palette[::-1]), textinfo='none')
    fig2.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0), height=180)
    st.plotly_chart(fig2, use_container_width=True, config={'displayModeBar': False})

# אייקונים בתחתית
st.markdown("<br>", unsafe_allow_html=True)
row_icons = st.columns(5)
cats = [("○", "רכב"), ("◇", "מזון"), ("♡", "צדקה"), ("□", "דירה"), ("△", "כללי")]
for i, (symbol, name) in enumerate(cats):
    with row_icons[i]:
        st.markdown(f'<div class="cat-box"><div style="color:#B0B0D0;">{symbol}</div><div class="cat-label">{name}</div></div>', unsafe_allow_html=True)

# כפתורים צפים
col_btn1, col_btn2 = st.columns([6,1])
with col_btn2:
    if st.button("+"):
        show_transaction_form()

# כפתור הגדרות נסתר שמפעיל את הדיאלוג
if st.button("⚙️", key="settings_btn", help="הגדרות"):
    show_settings()

import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - ניקוי מוחלט מהשורש
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת CSS סופית: עיצוב בוגר, נקי ונטול פסים ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* 1. השמדת ה-Sidebar וכל שארית של פסים */
    section[data-testid="stSidebar"] { display: none !important; }
    [data-testid="stHeader"] { display: none !important; }
    .st-emotion-cache-z5fcl4, .st-emotion-cache-6q9sum, .st-emotion-cache-16idsys { display: none !important; }
    
    /* 2. רקע לבן צחור וניקוי שוליים */
    .stApp { background-color: #FFFFFF !important; }
    .block-container { padding: 1.5rem !important; max-width: 100% !important; }
    
    /* 3. פונט Assistant ויישור לימין */
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }
    
    /* 4. כרטיסיות נתונים יוקרתיות */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border-radius: 15px !important;
        padding: 20px !important;
        border: 1px solid #F0F0F5 !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.02) !important;
        border-right: 6px solid #4A3AFF !important;
        margin-bottom: 12px !important;
    }
    div[data-testid="stMetricValue"] > div { color: #4A3AFF !important; font-size: 32px !important; font-weight: 700 !important; }

    /* 5. כפתור הפלוס הצף (FAB) - עיגול סגול מושלם */
    .stButton > button {
        position: fixed !important;
        bottom: 30px !important;
        left: 30px !important;
        width: 70px !important;
        height: 70px !important;
        background: #4A3AFF !important;
        color: white !important;
        border-radius: 50% !important;
        font-size: 35px !important;
        box-shadow: 0 10px 25px rgba(74, 58, 255, 0.4) !important;
        border: 2px solid white !important;
        z-index: 99999 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        transition: 0.3s !important;
    }
    .stButton > button:hover { transform: scale(1.1); background: #3A2ADF !important; }

    /* 6. אייקון הגדרות בפינה למעלה */
    .settings-trigger {
        position: fixed;
        top: 20px;
        left: 20px;
        font-size: 24px;
        cursor: pointer;
        z-index: 9998;
        background: #F8F9FA;
        padding: 8px;
        border-radius: 50%;
        border: 1px solid #EEE;
    }

    /* 7. אייקונים בוגרים בתחתית */
    .cat-box {
        background-color: #FDFDFF;
        border-radius: 12px;
        padding: 18px;
        text-align: center;
        border: 1px solid #F0F0F5;
    }
    .cat-label { color: #5A52CB; font-size: 13px; font-weight: 700; margin-top: 5px; }
    .cat-symbol { color: #B0B0D0; font-size: 15px; }

    /* עיצוב חלון הדיאלוג */
    div[data-testid="stDialog"] { direction: rtl !important; border-radius: 20px !important; }
    </style>
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
            t_cat = st.selectbox("מקור הכנסה", ["משכורת ישראל", "משכורת רחלי", "כללי ישראל", "עצמאי רחלי", "כללי רחלי"])
    t_desc = st.text_input("פירוט חופשי")
    if st.button("שמור שינויים", use_container_width=True):
        st.balloons()
        st.success("הנתון נרשם!")
        st.rerun()

# --- פונקציית הגדרות ובוט ---
@st.dialog("הגדרות ובוט")
def show_settings():
    st.subheader("⚙️ הגדרות")
    st.number_input("יעד חיסכון חודשי", value=20000)
    st.markdown("---")
    st.subheader("🤖 הבוט של רחלי")
    st.info("רחלי, הכל נראה נקי ומסודר. האפליקציה מוכנה לעבודה!")

# --- כותרת ראשית ---
st.markdown('<h1 style="text-align: center; font-size: 32px; color: #1A1A2E;">Wealth Management</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #716B94; margin-top: -15px; font-size: 15px;">Asset Tracking | רחלי</p>', unsafe_allow_html=True)

# דשבורד כסף
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: st.metric("Cash", "$2,450")
with c2: st.metric("BofA", "$4,100")
with c3: st.metric("Amex", "-$1,200")

# מד התקדמות
st.markdown("<br>", unsafe_allow_html=True)
st.progress(5800/20000)
st.markdown('<p style="font-size: 13px; color: #716B94; text-align: center;">נחסכו: <b>$5,800</b> מתוך <b>$20,000</b></p>', unsafe_allow_html=True)

# גרפים בסגול
st.markdown("<br>", unsafe_allow_html=True)
col_g1, col_g2 = st.columns(2)
purple_palette = ['#4A3AFF', '#6C63FF', '#8E86FF', '#B0AAFF', '#D2CFFF']

with col_g1:
    df1 = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
    fig1 = px.pie(df1, values='Val', names='Cat', hole=0.8, title="סבב נוכחי")
    fig1.update_traces(marker=dict(colors=purple_palette), textinfo='none')
    fig1.update_layout(showlegend=False, margin=dict(t=30, b=0, l=0, r=0), height=200)
    st.plotly_chart(fig1, use_container_width=True, config={'displayModeBar': False})

with col_g2:
    df2 = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [1500, 500, 1500, 1200, 400]})
    fig2 = px.pie(df2, values='Val', names='Cat', hole=0.8, title="ממוצע היסטורי")
    fig2.update_traces(marker=dict(colors=purple_palette[::-1]), textinfo='none')
    fig2.update_layout(showlegend=False, margin=dict(t=30, b=0, l=0, r=0), height=200)
    st.plotly_chart(fig2, use_container_width=True, config={'displayModeBar': False})

# אייקונים בוגרים בתחתית
st.markdown("<br>### ניתוח קטגוריות", unsafe_allow_html=True)
row_icons = st.columns(5)
cats_minimal = [("CAR", "רכב"), ("FOOD", "מזון"), ("GIVE", "צדקה"), ("HOME", "דירה"), ("MISC", "כללי")]

for i, (symbol, name) in enumerate(cats_minimal):
    with row_icons[i]:
        st.markdown(f'''
            <div class="cat-box">
                <div class="cat-symbol" style="letter-spacing: 2px;">{symbol}</div>
                <div class="cat-label">{name}</div>
            </div>
        ''', unsafe_allow_html=True)

# --- כפתור הגדרות (למעלה) וכפתור פלוס (למטה) ---
# כפתור הפלוס הגדול
if st.button("+"):
    show_transaction_form()

# כפתור הגדרות
st.markdown('<div class="settings-trigger">', unsafe_allow_html=True)
if st.button("⚙️", key="settings_main"):
    show_settings()
st.markdown('</div>', unsafe_allow_html=True)

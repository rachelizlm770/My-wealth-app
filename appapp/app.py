import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת CSS "The Invisible Wall" ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* 1. העלמה מוחלטת של כל פס מפריד - צביעה בלבן וכפייה */
    [data-testid="stHeader"], .st-emotion-cache-16idsys, .st-emotion-cache-6q9sum, 
    .st-emotion-cache-z5fcl4, .st-emotion-cache-10o1p90, .st-emotion-cache-kgp7u1 {
        display: none !important;
        background-color: white !important;
        border: none !important;
        box-shadow: none !important;
    }
    
    /* מחיקת הקו האפור המפריד בין ה-Main ל-Sidebar */
    .st-emotion-cache-1837eb1 { border-top: none !important; border-bottom: none !important; }
    div[data-testid="stSidebar"] { border-left: none !important; box-shadow: none !important; }

    /* 2. רקע לבן צחור לכל האפליקציה */
    .stApp { background-color: #FFFFFF !important; }
    .block-container { 
        padding: 2rem !important; 
        max-width: 95% !important; 
        background-color: white !important;
        z-index: 10 !important; /* מרים את התוכן מעל ה"פסים" של המערכת */
    }
    
    /* 3. פונט Assistant ויישור לימין */
    * { font-family: 'Assistant', sans-serif; direction: rtl; text-align: right; }
    
    /* 4. כרטיסיות נתונים יוקרתיות */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border-radius: 15px !important;
        padding: 25px !important;
        border: 1px solid #F0F0F5 !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.02) !important;
        border-right: 5px solid #4A3AFF !important;
    }
    div[data-testid="stMetricValue"] > div { color: #4A3AFF !important; font-size: 34px !important; font-weight: 700 !important; }

    /* 5. כפתור פלוס צף (FAB) */
    div.stButton > button:first-child {
        position: fixed !important;
        bottom: 35px !important;
        left: 35px !important;
        width: 65px !important;
        height: 65px !important;
        background: #4A3AFF !important;
        color: white !important;
        border-radius: 50% !important;
        font-size: 35px !important;
        box-shadow: 0 10px 30px rgba(74, 58, 255, 0.4) !important;
        border: 2px solid white !important;
        z-index: 99999 !important;
    }

    /* 6. עיצוב האייקונים בתחתית - בוגר ונקי */
    .cat-box {
        background-color: #FDFDFF !important;
        border-radius: 12px !important;
        padding: 15px !important;
        text-align: center !important;
        border: 1px solid #F0F0F5 !important;
    }
    .cat-label { color: #5A52CB !important; font-size: 13px !important; font-weight: 700 !important; margin-top: 5px !important; }
    .cat-symbol { color: #B0B0D0 !important; font-size: 11px !important; letter-spacing: 2px !important; }

    /* עיצוב חלון הדיאלוג המרחף */
    div[data-testid="stDialog"] { direction: rtl !important; background-color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- פונקציית החלון המרחף (Dialog) ---
@st.dialog("תיעוד פעולה חדשה")
def show_transaction_form():
    t_mode = st.radio("סוג פעולה", ["הוצאה", "הכנסה"], horizontal=True)
    
    ca, cb = st.columns(2)
    with ca:
        t_wallet = st.selectbox("חשבון / מקור", ["מזומן", "BofA", "Amex", "Food Stamps", "Pepper", "Leumi"])
        t_amount = st.number_input("סכום ($)", min_value=0.0, step=10.0)
    with cb:
        t_date = st.date_input("תאריך", datetime.now())
        if t_mode == "הוצאה":
            t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
        else:
            t_cat = st.selectbox("מקור הכנסה", ["משכורת ישראל", "משכורת רחלי", "כללי ישראל", "עצמאי רחלי", "כללי רחלי"])
    
    t_desc = st.text_input("פירוט", placeholder="מה בדיוק קרה?")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("אישור ושמירה", use_container_width=True):
        st.balloons()
        st.success("הפעולה נרשמה בהצלחה!")
        st.rerun()

# --- תוכן עמוד הבית ---
st.markdown('<h1 style="text-align: center; font-size: 30px; color: #1A1A2E;">Wealth Management</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #716B94; margin-top: -15px;">Asset Tracking | רחלי</p>', unsafe_allow_html=True)

# דשבורד כסף
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: st.metric("Cash", "$2,450")
with c2: st.metric("BofA", "$4,100")
with c3: st.metric("Amex", "$1,200-")

# מד התקדמות
st.markdown("<br>", unsafe_allow_html=True)
st.progress(5800/20000)
st.markdown('<p style="font-size: 13px; color: #716B94;">יעד חיסכון: <b>$20,000</b></p>', unsafe_allow_html=True)

# גרפים
st.markdown("<br>", unsafe_allow_html=True)
col_g1, col_g2 = st.columns(2)
purple_palette = ['#4A3AFF', '#6C63FF', '#8E86FF', '#B0AAFF', '#D2CFFF']

with col_g1:
    df1 = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
    fig1 = px.pie(df1, values='Val', names='Cat', hole=0.8, title="פירוט סבב")
    fig1.update_traces(marker=dict(colors=purple_palette), textinfo='none')
    fig1.update_layout(showlegend=True, margin=dict(t=30, b=0, l=0, r=0))
    st.plotly_chart(fig1, use_container_width=True)

with col_g2:
    df2 = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [1500, 500, 1500, 1200, 400]})
    fig2 = px.pie(df2, values='Val', names='Cat', hole=0.8, title="ממוצע תקופתי")
    fig2.update_traces(marker=dict(colors=purple_palette[::-1]), textinfo='none')
    fig2.update_layout(showlegend=True, margin=dict(t=30, b=0, l=0, r=0))
    st.plotly_chart(fig2, use_container_width=True)

# אייקונים בתחתית
st.markdown("### ניתוח קטגוריות", unsafe_allow_html=True)
row_icons = st.columns(5)
cats = [("CAR", "רכב"), ("FOOD", "מזון"), ("GIVE", "צדקה"), ("HOME", "דירה"), ("MISC", "כללי")]

for i, (symbol, name) in enumerate(cats):
    with row_icons[i]:
        st.markdown(f'''
            <div class="cat-box">
                <div class="cat-symbol">{symbol}</div>
                <div class="cat-label">{name}</div>
            </div>
        ''', unsafe_allow_html=True)

# כפתור הפלוס הצף
if st.button("+"):
    show_transaction_form()

# תפריט צד (Sidebar)
with st.sidebar:
    st.title("⚙️ הגדרות")
    st.number_input("עדכון יעד", value=20000)
    st.markdown("---")
    st.subheader("🤖 הבוט של רחלי")
    st.info("הקוד הותאם לנייד לניקוי מקסימלי של פסים.")

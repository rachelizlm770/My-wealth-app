import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - ניקוי מוחלט
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת CSS סופית: עיצוב יוקרתי ונקי ללא פסים ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* 1. מחיקה מוחלטת של ה-Sidebar והדרים מהשורש */
    section[data-testid="stSidebar"] { display: none !important; width: 0 !important; }
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
        border-radius: 20px !important;
        padding: 25px !important;
        border: 1px solid #F0F0F5 !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.03) !important;
        border-right: 8px solid #4A3AFF !important;
        margin-bottom: 15px !important;
    }
    div[data-testid="stMetricValue"] > div { color: #4A3AFF !important; font-size: 34px !important; font-weight: 700 !important; }

    /* 5. כפתור הפלוס הצף (FAB) - למטה משמאל */
    .stButton > button {
        position: fixed !important;
        bottom: 30px !important;
        left: 30px !important;
        width: 70px !important;
        height: 70px !important;
        background: #4A3AFF !important;
        color: white !important;
        border-radius: 50% !important;
        font-size: 40px !important;
        box-shadow: 0 10px 30px rgba(74, 58, 255, 0.4) !important;
        border: 3px solid white !important;
        z-index: 99999 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* 6. אייקון גלגל שיניים בפינה למעלה */
    .settings-container {
        position: fixed;
        top: 20px;
        left: 20px;
        z-index: 1000;
        background: #F8F9FA;
        border-radius: 50%;
        padding: 5px;
        border: 1px solid #EEE;
    }

    /* 7. אייקונים בוגרים בתחתית */
    .cat-box {
        background-color: #FDFDFF;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        border: 1px solid #F0F0F5;
    }
    .cat-label { color: #5A52CB; font-size: 13px; font-weight: 700; margin-top: 5px; }

    /* עיצוב חלון הדיאלוג */
    div[data-testid="stDialog"] { direction: rtl !important; border-radius: 25px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- פונקציות הדיאלוגים (חלונות מרחפים) ---
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
    t_desc = st.text_input("פירוט (על מה?)")
    
    if st.button("אישור ושמירה", use_container_width=True):
        st.balloons()
        st.success("הפעולה נרשמה בהצלחה!")
        st.rerun()

@st.dialog("הגדרות ובוט")
def show_settings():
    st.subheader("⚙️ הגדרות מערכת")
    st.number_input("יעד חיסכון סופי", value=20000)
    st.markdown("---")
    st.subheader("🤖 הבוט של רחלי")
    st.info("רחלי, הכל נראה נהדר. האפליקציה בגרסה הכי נקייה שלה.")

# --- תוכן עמוד הבית ---
st.markdown('<h1 style="text-align: center; font-size: 32px; color: #1A1A2E;">Wealth Management</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #716B94; margin-top: -15px;">Asset Tracking | רחלי</p>', unsafe_allow_html=True)

# דשבורד כסף
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: st.metric("Cash", "$2,450")
with c2: st.metric("BofA", "$4,100")
with c3: st.metric("Amex", "-$1,200")

# מד התקדמות
st.markdown("<br>", unsafe_allow_html=True)
st.progress(5800/20000)
st.markdown('<p style="font-size: 13px; color: #716B94; text-align: center;">נחסכו: <b>$5,800</b> / $20,000</p>', unsafe_allow_html=True)

# --- גרפים עם נתונים גלויים ---
st.markdown("<br>", unsafe_allow_html=True)
col_g1, col_g2 = st.columns(2)
purple_palette = ['#4A3AFF', '#6C63FF', '#8E86FF', '#B0AAFF', '#D2CFFF']

with col_g1:
    df1 = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
    fig1 = px.pie(df1, values='Val', names='Cat', hole=0.7, title="פירוט סבב")
    # החזרת הנתונים: מציג שם קטגוריה + אחוז
    fig1.update_traces(marker=dict(colors=purple_palette), textinfo='percent+label', textposition='inside')
    fig1.update_layout(showlegend=False, margin=dict(t=30, b=0, l=0, r=0), height=250)
    st.plotly_chart(fig1, use_container_width=True, config={'displayModeBar': False})

with col_g2:
    df2 = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [1500, 500, 1500, 1200, 400]})
    fig2 = px.pie(df2, values='Val', names='Cat', hole=0.7, title="ממוצע היסטורי")
    # החזרת הנתונים
    fig2.update_traces(marker=dict(colors=purple_palette[::-1]), textinfo='percent+label', textposition='inside')
    fig2.update_layout(showlegend=False, margin=dict(t=30, b=0, l=0, r=0), height=250)
    st.plotly_chart(fig2, use_container_width=True, config={'displayModeBar': False})

# אייקונים בתחתית
st.markdown("### ניתוח קטגוריות", unsafe_allow_html=True)
row_icons = st.columns(5)
cats = [("CAR", "רכב"), ("FOOD", "מזון"), ("GIVE", "צדקה"), ("HOME", "דירה"), ("MISC", "כללי")]

for i, (symbol, name) in enumerate(cats):
    with row_icons[i]:
        st.markdown(f'''
            <div class="cat-box">
                <div style="color:#B0B0D0; letter-spacing:2px; font-size:10px;">{symbol}</div>
                <div class="cat-label">{name}</div>
            </div>
        ''', unsafe_allow_html=True)

# --- כפתורים צפים (FAB) ---
# כפתור הפלוס (למטה)
if st.button("+"):
    show_transaction_form()

# כפתור הגדרות (למעלה)
st.markdown('<div class="settings-container">', unsafe_allow_html=True)
if st.button("⚙️", key="settings_btn"):
    show_settings()
st.markdown('</div>', unsafe_allow_html=True)

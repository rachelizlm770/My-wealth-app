import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- CSS מעודכן: צבעים נעימים ועיצוב בוגר ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* עיצוב רקע וטקסט */
    .stApp { background-color: #FAFAFA; }
    * { font-family: 'Assistant', sans-serif; direction: rtl; }

    /* הסתרת רכיבי מערכת מיותרים */
    [data-testid="stHeader"] { display: none !important; }

    /* כרטיסיות נתונים - צבעים רכים יותר */
    div[data-testid="stMetric"] {
        background: white !important;
        border-radius: 15px !important;
        border-right: 6px solid #6D9292 !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03) !important;
        padding: 15px !important;
    }
    div[data-testid="stMetricValue"] > div { color: #4A6363 !important; font-weight: 700 !important; }

    /* כפתור פלוס עגול ומרחף - תיקון הריבוע */
    .stButton > button[key="plus_btn"] {
        position: fixed !important;
        bottom: 30px !important;
        left: 30px !important;
        width: 65px !important;
        height: 65px !important;
        background-color: #5E8080 !important;
        color: white !important;
        border-radius: 50% !important;
        border: 3px solid white !important;
        font-size: 35px !important;
        box-shadow: 0 8px 20px rgba(94, 128, 128, 0.3) !important;
        z-index: 9999 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* שורת האייקונים למטה */
    .icon-box {
        text-align: center;
        background: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        transition: 0.3s;
        border: 1px solid #EEE;
    }
    .icon-box:hover { transform: translateY(-3px); border-color: #6D9292; }
    .icon-text { color: #4A6363; font-weight: 600; font-size: 14px; margin-top: 5px; }
    
    /* כותרות גרפים */
    .graph-title {
        color: #4A6363;
        font-weight: 700;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- תפריט צדדי (Sidebar) להגדרות - נקי ובוגר ---
with st.sidebar:
    st.markdown("### ⚙️ הגדרות וכלים")
    st.markdown("---")
    st.button("🤖 התייעצות עם בוט")
    st.button("📜 היסטוריית תנועות")
    st.button("📦 ארכיון נתונים")
    st.markdown("---")
    new_goal = st.number_input("עדכון יעד חיסכון ($)", value=20000)
    st.info("השינויים נשמרים אוטומטית.")

# --- פונקציות דיאלוג ---

@st.dialog("דיווח תנועה חדשה")
def show_transaction_dialog():
    st.markdown("<h3 style='color: #5E8080;'>📝 פרטי הפעולה</h3>", unsafe_allow_html=True)
    t_mode = st.radio("סוג פעולה", ["הוצאה", "הכנסה"], horizontal=True)
    
    ca, cb = st.columns(2)
    with ca:
        t_amount = st.number_input("סכום ($)", min_value=0.0, step=10.0)
        t_wallet = st.selectbox("חשבון", ["מזומן", "BofA", "Amex", "Leumi"])
    with cb:
        t_date = st.date_input("תאריך", datetime.now())
        if t_mode == "הוצאה":
            t_cat = st.selectbox("קטגוריה", ["צדקה", "רכב", "מזון", "דירה", "כללי"])
        else:
            t_cat = st.selectbox("מקור הכנסה", ["משכורת", "עצמאי", "אחר"])
    
    t_desc = st.text_area("פירוט ומידע נוסף:", placeholder="למשל: קניות לשבת...")
            
    if st.button("אישור ושמירה", use_container_width=True):
        st.success("נשמר בהצלחה")
        st.rerun()

# --- תוכן דף הבית ---

# כותרת ויעד
st.markdown('<h1 style="text-align: center; color: #2A3F3F; margin-bottom: 5px;">Wealth Management</h1>', unsafe_allow_html=True)

# שורת יעד (Progress Bar)
col_goal_a, col_goal_b, col_goal_c = st.columns([1, 4, 1])
with col_goal_b:
    current_savings = 12450
    target = 20000
    progress = current_savings / target
    st.markdown(f"<p style='text-align:center; font-size:14px; color:#666;'>התקדמות ליעד החיסכון: <b>${current_savings:,}</b> מתוך <b>${target:,}</b></p>", unsafe_allow_html=True)
    st.progress(progress)

st.markdown("<br>", unsafe_allow_html=True)

# דשבורד מספרים
m1, m2, m3 = st.columns(3)
with m1: st.metric("יתרה במזומן", "$2,450")
with m2: st.metric("נכסים בבנק", "$4,100")
with m3: st.metric("חובות אשראי", "-$1,200")

# גרפים עם כותרות
st.markdown("<br>", unsafe_allow_html=True)
g1, g2 = st.columns(2)
df_sample = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
colors = ['#5E8080', '#769797', '#91AFAF', '#AFC5C5', '#D4E4E4']

with g1:
    st.markdown('<p class="graph-title">📊 פירוט הוצאות שבועי</p>', unsafe_allow_html=True)
    fig1 = px.pie(df_sample, values='Val', names='Cat', hole=0.7)
    fig1.update_traces(marker=dict(colors=colors), textinfo='label+value', textposition='outside')
    fig1.update_layout(showlegend=False, margin=dict(t=0, b=0, l=40, r=40), height=300)
    st.plotly_chart(fig1, use_container_width=True)

with g2:
    st.markdown('<p class="graph-title">📈 ממוצע דו-שבועי כללי</p>', unsafe_allow_html=True)
    fig2 = px.pie(df_sample, values='Val', names='Cat', hole=0.7)
    fig2.update_traces(marker=dict(colors=colors[::-1]), textinfo='label+value', textposition='outside')
    fig2.update_layout(showlegend=False, margin=dict(t=0, b=0, l=40, r=40), height=300)
    st.plotly_chart(fig2, use_container_width=True)

# שורת אייקונים למטה - בוגר ונעים
st.markdown("<br>", unsafe_allow_html=True)
row = st.columns(5)
icons = [("🚗", "רכב"), ("🍕", "מזון"), ("✡️", "צדקה"), ("🏠", "דירה"), ("🛠️", "כללי")]

for i, (icon, name) in enumerate(icons):
    with row[i]:
        st.markdown(f"""
            <div class="icon-box">
                <div style="font-size: 24px;">{icon}</div>
                <div class="icon-text">{name}</div>
            </div>
        """, unsafe_allow_html=True)

# כפתור פלוס צף
if st.button("+", key="plus_btn"):
    show_transaction_dialog()

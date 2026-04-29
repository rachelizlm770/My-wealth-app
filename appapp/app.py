import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# הגדרות דף - ניקוי מוחלט מהשורש
st.set_page_config(page_title="Wealth Management", layout="wide", initial_sidebar_state="collapsed")

# --- הזרקת CSS: הסתרה מוחלטת של סרגל הצד ועיצוב SaaS בוגר ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;700&display=swap');
    
    /* 1. השמדה מוחלטת של ה-Sidebar המובנה, החץ והקו באמצע */
    [data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"], [data-testid="stHeader"] {
        display: none !important;
        width: 0 !important;
    }
    .st-emotion-cache-z5fcl4, .st-emotion-cache-6q9sum, .st-emotion-cache-16idsys {
        display: none !important;
    }

    /* 2. רקע לבן צחור וניקוי רווחים */
    .stApp { background-color: #FFFFFF !important; }
    .block-container { padding: 1.5rem !important; max-width: 100% !important; }
    * { font-family: 'Assistant', sans-serif; direction: rtl; }

    /* 3. תווית הגדרות ימנית (בוגרת) */
    .side-label-right {
        position: fixed;
        top: 25%;
        right: 0;
        background-color: #3D5A5A; /* טורקיז מעושן בוגר */
        color: white;
        padding: 20px 10px;
        border-radius: 12px 0 0 12px;
        cursor: pointer;
        z-index: 99999;
        writing-mode: vertical-rl;
        text-orientation: mixed;
        font-weight: 600;
        font-size: 14px;
        box-shadow: -2px 4px 15px rgba(0,0,0,0.15);
    }

    /* 4. כפתור פלוס דומיננטי בשמאל */
    div.stButton > button:first-child {
        position: fixed !important;
        bottom: 40px !important;
        left: 40px !important;
        width: 80px !important;
        height: 80px !important;
        background-color: #3D5A5A !important;
        color: white !important;
        border-radius: 50% !important;
        border: 4px solid white !important;
        font-size: 45px !important;
        box-shadow: 0 12px 30px rgba(61, 90, 90, 0.3) !important;
        z-index: 99999 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* 5. כרטיסיות נתונים */
    div[data-testid="stMetric"] {
        background: #F9FBFB !important;
        border-radius: 20px !important;
        border-right: 10px solid #3D5A5A !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.02) !important;
    }
    div[data-testid="stMetricValue"] > div { color: #2A3F3F !important; font-weight: 700 !important; }

    /* 6. עיצוב חלון מרחף (Dialog) */
    div[data-testid="stDialog"] { border-radius: 25px !important; direction: rtl !important; }
    </style>
    """, unsafe_allow_html=True)

# --- חלונות מרחפים (במקום סרגל צד ששובר את המסך) ---

@st.dialog("שורת כלים והגדרות")
def show_tools_menu():
    st.markdown("### 🛠️ מה תרצי לעשות?")
    choice = st.radio("בחר אפשרות:", ["🤖 בוט פיננסי", "📜 היסטוריית תנועות", "📦 ארכיון", "⚙️ הגדרות יעד"], label_visibility="collapsed")
    st.markdown("---")
    if choice == "⚙️ הגדרות יעד":
        st.number_input("עדכון יעד חיסכון", value=20000)
    elif choice == "🤖 בוט פיננסי":
        st.info("רחלי, אני כאן לנתח את הנתונים שלך.")
    else:
        st.write(f"תצוגת {choice} תתווסף בהמשך...")
    
    if st.button("סגור תפריט", use_container_width=True):
        st.rerun()

@st.dialog("דיווח תנועה חדשה")
def show_transaction_dialog():
    st.markdown("<h3 style='color: #3D5A5A;'>📝 פרטי הפעולה</h3>", unsafe_allow_html=True)
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
            
    if st.button("אישור ושמירה", use_container_width=True):
        st.balloons()
        st.rerun()

# --- תוכן דף הבית (נקי לחלוטין מקווים) ---
st.markdown('<h1 style="text-align: center; color: #2A3F3F; font-size: 32px;">Wealth Management</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #666; margin-top: -15px;">Asset Tracking Dashboard</p>', unsafe_allow_html=True)

# דשבורד
st.markdown("<br>", unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m1: st.metric("Cash Balance", "$2,450")
with m2: st.metric("Bank Assets", "$4,100")
with m3: st.metric("Credit Debt", "-$1,200")

# גרפים בטורקיז עמוק
st.markdown("<br>", unsafe_allow_html=True)
g_col1, g_col2 = st.columns(2)
df_sample = pd.DataFrame({'Cat': ['רכב', 'מזון', 'צדקה', 'דירה', 'כללי'], 'Val': [800, 300, 750, 1200, 250]})
colors = ['#3D5A5A', '#5E8080', '#83A3A3', '#ABC5C5', '#D4E4E4']

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

# --- כפתורים צפים (SaaS UI) ---

# 1. תווית הגדרות צדדית (כפתור שקוף מעל ה-HTML)
# יצרתי כפתור שקוף שיושב בדיוק על התווית הויזואלית
col_hidden = st.columns([10, 1])
with col_hidden[1]:
    if st.button("⚙️", key="tools_trigger", help="פתח שורת כלים"):
        show_tools_menu()

st.markdown('<div class="side-label-right">⚙️ הגדרות וכלים</div>', unsafe_allow_html=True)

# 2. כפתור פלוס
if st.button("+"):
    show_transaction_dialog()

# שורת קטגוריות
st.markdown("<br>", unsafe_allow_html=True)
row = st.columns(5)
for i, name in enumerate(["רכב", "מזון", "צדקה", "דירה", "כללי"]):
    with row[i]:
        st.markdown(f'<div style="text-align:center; background:#F0F7F7; padding:12px; border-radius:12px; border:1px solid #3D5A5A; color:#2A3F3F; font-weight:600; font-size:13px;">{name}</div>', unsafe_allow_html=True)

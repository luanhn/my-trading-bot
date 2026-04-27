import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Gold Grid V4 Realtime", layout="wide")

# Kết nối với Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/1q1TTEZ6mXP4lB9pCv8090JwkvSTNopQmVCDtFo_ByCk/edit?gid=0#gid=0",ttl=0)

# Lấy dòng mới nhất
if not df.empty:
    latest = df.iloc[-1]
    st.title("💹 Gold Grid V4 Pro Realtime")
    c1, c2, c3 = st.columns(3)
    c1.metric("Balance", f"${latest['Balance']}")
    c2.metric("Equity", f"${latest['Equity']}")
    c3.metric("Status", latest['Status'])

    st.subheader("📊 Biểu đồ tăng trưởng thực tế")
    st.line_chart(df.set_index('Time')['Balance'])
else:
    st.warning("Đang đợi dữ liệu từ Bot gửi về...")



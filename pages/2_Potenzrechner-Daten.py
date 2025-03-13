import streamlit as st

# === Login manager ===
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  

st.title('Potenzrechner Werte')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Daten vorhanden. Berechnen Sie Ihre Potenz im Potenzrechner.')
    st.stop()

# Sort dataframe by timestamp
data_df = data_df.sort_values('timestamp', ascending=False)

# Display table
st.dataframe(data_df)

if st.button("Zurück zur Startseite"):
    st.switch_page("Start.py")
if st.button("Zum Potenzrechner"):
    st.switch_page("pages/3_Potenzrechner-Grafik.py")
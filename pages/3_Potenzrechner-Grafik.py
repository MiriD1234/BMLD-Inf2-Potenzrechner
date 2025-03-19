import streamlit as st

# === Login manager ===
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  

st.title('Potenzrechner Verlauf')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Potenzrechner Daten vorhanden. Berechnen Sie die Potenz im Potenzrechner.')
    st.stop()

# Base over time
st.line_chart(data=data_df.set_index('timestamp')['base'], 
                use_container_width=True)
st.caption('Basis über Zeit')

# Exponent over time 
st.line_chart(data=data_df.set_index('timestamp')['exponent'],
                use_container_width=True)
st.caption('Exponent über Zeit')

# Exponentiation over time
st.line_chart(data=data_df.set_index('timestamp')['exponentiation'],
                use_container_width=True)
st.caption('Potenz über Zeit')

if st.button("Zurück zur Startseite"):
    st.switch_page("Start.py")
if st.button("Zum Potenzrechner"):
    st.switch_page("pages/1_Potenzrechner.py")
if st.button("Zu den Potenzrechner-Daten"):
    st.switch_page("pages/2_Potenzrechner-Daten.py")
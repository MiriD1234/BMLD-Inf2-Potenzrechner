import streamlit as st

# === Login manager ===
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  

st.title('Potenzrechner Verlauf')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Potenzrechner Daten vorhanden. Berechnen Sie die Potenz im Potenzrechner.')
    st.stop()

# Weight over time
st.line_chart(data=data_df.set_index('timestamp')['base'], 
                use_container_width=True)
st.caption('Grundwert über Zeit')

# Height over time 
st.line_chart(data=data_df.set_index('timestamp')['exponent'],
                use_container_width=True)
st.caption('Exponent über Zeit')

# BMI over time
st.line_chart(data=data_df.set_index('timestamp')['exponentiation'],
                use_container_width=True)
st.caption('Potenz über Zeit')

if st.button("Zurück zur Startseite"):
    st.switch_page("Start.py")
if st.button("Zum Potenzrechner"):
    st.switch_page("pages/1_Potenzrechner.py")
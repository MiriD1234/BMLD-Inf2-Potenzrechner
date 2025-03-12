import streamlit as st

st.title('Potenzrechner Werte')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Daten vorhanden. Berechnen Sie Ihre Potenz auf der Startseite.')
    st.stop()

# Sort dataframe by timestamp
data_df = data_df.sort_values('timestamp', ascending=False)

# Display table
st.dataframe(data_df)
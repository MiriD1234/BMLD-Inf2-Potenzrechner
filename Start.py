import streamlit as st
import pandas as pd

from utils.data_manager import DataManager

#initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="App/BMLD Demo")

# load the data from the persistent storage into the session state
data_manager.load_app_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )

st.title("Potenzrechner")

st.success("Diese App berechnet die Potenz einer Basis mit einem gegebenen Exponenten.")

"""Diese App wurde von folgenden Personen im Rahmen des Moduls 'BMLD Informatik 2' entwickelt:
- Elena Buchli (buchlele@students.zhaw.ch)
- Miranda Downing (downimir@students.zhaw.ch)"""


if st.button("Zum Potenzrechner"):
    st.switch_page("pages/1_Potenzrechner.py")

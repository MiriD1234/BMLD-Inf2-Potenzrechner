import streamlit as st
import pandas as pd

st.title("Potenzrechner")

st.success("Diese App berechnet die Potenz einer Basis mit einem gegebenen Exponenten.")

"""Diese App wurde von folgenden Personen im Rahmen des Moduls 'BMLD Informatik 2' entwickelt:
- Elena Buchli (buchlele@students.zhaw.ch)
- Miranda Downing (downimir@students.zhaw.ch)"""


if st.button("Zum Potenzrechner"):
    st.switch_page("pages/1_Potenzrechner.py")

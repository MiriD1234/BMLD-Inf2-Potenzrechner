import streamlit as st
from functions.potenzrechner import calculate_exponentiation
from utils.data_manager import DataManager

# Initialisiere den Schlüssel 'data_df' im session_state, falls er nicht existiert
if 'data_df' not in st.session_state:
    st.session_state['data_df'] = []

# Streamlit App
st.title("🧮 Potenzrechner 🧮")

# Beschreibung
st.write("""
Diese App berechnet die Potenz einer Basis mit einem gegebenen Exponenten.
Geben Sie die Werte unten ein und klicken Sie auf **'Berechnen'**, um das Ergebnis zu sehen.
""")

# Form für Eingaben und Berechnung
with st.form("potenz_form"):
    st.header("🔢 Eingabewerte")
    
    base = st.number_input("Geben Sie die Basis ein:", value=1, min_value=0, step=1)
    exponent = st.number_input("Geben Sie den Exponenten ein:", value=1, min_value=0, step=1)

    # Submit-Button innerhalb des Forms
    submit_button = st.form_submit_button("🛠️ Berechnen")

# Berechnung erfolgt nur, wenn der Button geklickt wurde
if submit_button:
    result_dict = calculate_exponentiation(base, exponent)
    result = result_dict["exponentiation"]

    # Anzeige der Eingabewerte
    st.subheader("Eingabewerte")
    st.write(f"**Basis:** {base}")
    st.write(f"**Exponent:** {exponent}")
    # Anzeige des Ergebnisses
    st.subheader("Ergebnis")
    st.success(f"$${base}^{{{exponent}}} = {result}$$")
    st.balloons()

    # update data in session state and save to persistent storage
    DataManager().append_record(session_state_key='data_df', record_dict=result_dict)

else:
    st.info("Bitte geben Sie die Werte ein und klicken Sie auf **'Berechnen'**.")

if st.button("Zurück zur Startseite"):
    st.switch_page("Start.py")

if st.button("Zu den Potenzrechner-Daten"):
    st.switch_page("pages/2_Potenzrechner-Daten.py")

# Footer
st.divider()


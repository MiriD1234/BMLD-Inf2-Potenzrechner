import streamlit as st

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
    result = base ** exponent

    # Anzeige der Eingabewerte
    st.subheader("Eingabewerte")
    st.write(f"**Basis:** {base}")
    st.write(f"**Exponent:** {exponent}")
    # Anzeige des Ergebnisses
    st.subheader("Ergebnis")
    st.success(f"$${base}^{exponent} = {result}$$")
    st.balloons()

else:
    st.info("Bitte geben Sie die Werte ein und klicken Sie auf **'Berechnen'**.")

if st.button("Zurück zur Startseite"):
    st.switch_page("start.py")

# Footer
st.divider()

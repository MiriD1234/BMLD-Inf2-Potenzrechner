import streamlit as st

# Streamlit App
st.title("Potenzrechner")

# Beschreibung
st.write("""
Diese App berechnet die Potenz einer Basis mit einem gegebenen Exponenten.
Geben Sie die Werte unten ein und klicken Sie auf 'Berechnen', um das Ergebnis zu sehen.
""")

# Eingabe der Basis und des Exponenten
st.header("Eingabewerte")
base = st.number_input("Geben Sie die Basis ein:", value=1, min_value=0, step=1)
exponent = st.number_input("Geben Sie den Exponenten ein:", value=1, min_value=0, step=1)

# Berechnung der Potenz
if st.button("Berechnen"):
    result = base ** exponent

    # Anzeige des Ergebnisses
    st.subheader("Eingabewerte")
    st.write(f"**Basis:** {base}")
    st.write(f"**Exponent:** {exponent}")

    st.success(f"Das Ergebnis von {base} hoch {exponent} ist **{result}**.")
    
    # Anzeige des Ergebnisses als Zahl
    st.metric(label="Ergebnis", value=result)
else:
    st.info("Bitte geben Sie die Werte ein und klicken Sie auf 'Berechnen'.")

# Footer
st.write("---")
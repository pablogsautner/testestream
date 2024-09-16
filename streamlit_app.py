import streamlit as st

# Título do aplicativo
st.title("Exemplo Simples com Streamlit")

# Entrada de texto
nome = st.text_input("Digite seu nome:")

# Botão para acionar a resposta
if st.button("Enviar"):
    st.write(f"Olá, {nome}! Seja bem-vindo ao app Streamlit!")

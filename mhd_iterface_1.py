import streamlit as st
import pandas as pd

# Definição das perguntas por etapa
perguntas = {
    "Base Teórica": "Quais são os fundamentos teóricos que embasam sua análise?",
    "Hipótese": "Qual é a hipótese que você deseja testar?",
    "Consequências": "Quais consequências são esperadas se a hipótese for verdadeira?",
    "Experimento": "Como você pretende testar sua hipótese?",
    "Observações": "Quais foram os resultados observados?",
    "Avaliação": "Como você avalia os resultados em relação à hipótese inicial?"
}

# Inicialização do estado da aplicação
if "mhd_data" not in st.session_state:
    st.session_state.mhd_data = pd.DataFrame(columns=["Etapa", "Descrição", "FEN"])

if "descricao_etapa" not in st.session_state:
    st.session_state.descricao_etapa = ""

if "current_board" not in st.session_state:
    from chess import Board
    st.session_state.current_board = Board()

# Exibir dica automaticamente ao selecionar a etapa
etapa_selecionada = st.selectbox("Selecione a Etapa", list(perguntas.keys()), key="etapa_selecionada")
st.write(f"**Dica:** {perguntas[etapa_selecionada]}")

# Formulário para adicionar nova etapa
with st.form("mhd_form"):
    descricao = st.text_area("Descreva a etapa:", height=100, key="descricao_etapa")
    submitted = st.form_submit_button("Adicionar Etapa")
    if submitted:
        if descricao.strip():
            nova_entrada = pd.DataFrame({
                "Etapa": [etapa_selecionada],
                "Descrição": [descricao],
                "FEN": [st.session_state.current_board.fen()]
            })
            st.session_state.mhd_data = pd.concat([st.session_state.mhd_data, nova_entrada], ignore_index=True)
            st.session_state["descricao_etapa"] = ""  # Limpar o campo de descrição
            st.success(f"Etapa '{etapa_selecionada}' adicionada com sucesso!")
        else:
            st.error("A descrição não pode estar vazia!")

# Exibir dados adicionados
st.write("### Etapas Adicionadas")
st.dataframe(st.session_state.mhd_data)

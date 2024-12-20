import streamlit as st
import pandas as pd

# Defini��o das perguntas por etapa
perguntas = {
    "Base Te�rica": "Quais s�o os fundamentos te�ricos que embasam sua an�lise?",
    "Hip�tese": "Qual � a hip�tese que voc� deseja testar?",
    "Consequ�ncias": "Quais consequ�ncias s�o esperadas se a hip�tese for verdadeira?",
    "Experimento": "Como voc� pretende testar sua hip�tese?",
    "Observa��es": "Quais foram os resultados observados?",
    "Avalia��o": "Como voc� avalia os resultados em rela��o � hip�tese inicial?"
}

# Inicializa��o do estado da aplica��o
if "mhd_data" not in st.session_state:
    st.session_state.mhd_data = pd.DataFrame(columns=["Etapa", "Descri��o", "FEN"])

if "descricao_etapa" not in st.session_state:
    st.session_state.descricao_etapa = ""

if "current_board" not in st.session_state:
    from chess import Board
    st.session_state.current_board = Board()

# Exibir dica automaticamente ao selecionar a etapa
etapa_selecionada = st.selectbox("Selecione a Etapa", list(perguntas.keys()), key="etapa_selecionada")
st.write(f"**Dica:** {perguntas[etapa_selecionada]}")

# Formul�rio para adicionar nova etapa
with st.form("mhd_form"):
    descricao = st.text_area("Descreva a etapa:", height=100, key="descricao_etapa")
    submitted = st.form_submit_button("Adicionar Etapa")
    if submitted:
        if descricao.strip():
            nova_entrada = pd.DataFrame({
                "Etapa": [etapa_selecionada],
                "Descri��o": [descricao],
                "FEN": [st.session_state.current_board.fen()]
            })
            st.session_state.mhd_data = pd.concat([st.session_state.mhd_data, nova_entrada], ignore_index=True)
            st.session_state["descricao_etapa"] = ""  # Limpar o campo de descri��o
            st.success(f"Etapa '{etapa_selecionada}' adicionada com sucesso!")
        else:
            st.error("A descri��o n�o pode estar vazia!")

# Exibir dados adicionados
st.write("### Etapas Adicionadas")
st.dataframe(st.session_state.mhd_data)

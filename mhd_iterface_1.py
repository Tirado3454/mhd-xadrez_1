import streamlit as st
import pandas as pd
from streamlit_chessboard import chessboard
from chess import Board

# Inicializar o estado do aplicativo
if 'etapas' not in st.session_state:
    st.session_state.etapas = []
if 'mhd_data' not in st.session_state:
    st.session_state.mhd_data = pd.DataFrame(columns=["Tópico", "Descrição", "FEN"])

# Função para exibir as dicas com base no tópico selecionado
def get_dica_por_topico(topico):
    dicas = {
        "Base Teórica": "Explique o embasamento teórico relacionado ao tema.",
        "Hipótese": "Descreva a hipótese que será avaliada.",
        "Consequências": "Liste as consequências previstas pela hipótese.",
        "Experimento": "Detalhe o experimento que testará a hipótese.",
        "Observações": "Relate as observações do experimento.",
        "Avaliação": "Avalie os resultados obtidos no experimento."
    }
    return dicas.get(topico, "Selecione um tópico para obter a dica.")

# Interface do aplicativo
st.title("Modelo Hipotético-Dedutivo no Xadrez")

# Seção de seleção do tópico
topico = st.selectbox("Selecione o tópico da etapa:", [
    "Base Teórica", "Hipótese", "Consequências", "Experimento", "Observações", "Avaliação"
])

# Exibir dica automaticamente
st.info(get_dica_por_topico(topico))

# Campo para descrever a etapa
descricao = st.text_area("Descreva a etapa:")

# Botão para adicionar a etapa
if st.button("Adicionar Etapa"):
    # Adicionar a etapa ao estado do aplicativo
    st.session_state.mhd_data = pd.concat([
        st.session_state.mhd_data,
        pd.DataFrame({"Tópico": [topico], "Descrição": [descricao], "FEN": [st.session_state.get('fen', '')]})
    ], ignore_index=True)

    # Limpar o campo de descrição após adicionar
    st.experimental_rerun()

# Exibir a tabela com as etapas
st.dataframe(st.session_state.mhd_data)

# Configuração do tabuleiro de xadrez
st.subheader("Configuração do Tabuleiro")
st.session_state.fen = st.text_input("Atualizar tabuleiro com FEN:")
if st.button("Atualizar Tabuleiro"):
    st.session_state.board = Board(st.session_state.fen)
else:
    st.session_state.board = Board()

# Renderizar o tabuleiro de xadrez
chessboard("tabuleiro", fen=st.session_state.board.fen())

# Exportar as etapas para CSV
if st.button("Exportar para CSV"):
    st.session_state.mhd_data.to_csv("etapas.csv", index=False)
    st.success("Dados exportados com sucesso!")

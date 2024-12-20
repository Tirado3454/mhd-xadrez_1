import streamlit as st
import chess
import chess.svg
from streamlit_chessboard import chessboard

# Inicializar o estado da aplicação
if "etapas" not in st.session_state:
    st.session_state["etapas"] = []
if "descricao_etapa" not in st.session_state:
    st.session_state["descricao_etapa"] = ""
if "fen" not in st.session_state:
    st.session_state["fen"] = chess.Board().fen()

# Função para adicionar uma nova etapa
def adicionar_etapa():
    if st.session_state.descricao_etapa:
        st.session_state.etapas.append(
            {
                "etapa": st.session_state.etapa_selecionada,
                "descricao": st.session_state.descricao_etapa,
                "fen": st.session_state.fen,
            }
        )
        st.session_state.descricao_etapa = ""  # Limpar o campo de descrição

# Dicionário de dicas por etapa
dicas = {
    "Base Teórica": "Descreva os fundamentos teóricos relacionados à posição do tabuleiro.",
    "Hipótese": "Formule uma hipótese com base na posição inicial das peças no tabuleiro.",
    "Consequências": "Liste as possíveis consequências que podem ocorrer a partir dessa posição.",
    "Experimento": "Descreva um experimento prático que pode ser realizado com essa posição.",
    "Observações": "Registre observações obtidas a partir do experimento.",
    "Avaliação": "Avalie os resultados do experimento em relação à hipótese inicial.",
}

# Título da aplicação
st.title("Modelo Hipotético-Dedutivo no Xadrez")

# Seção de seleção de etapas e descrição
st.sidebar.header("Configuração da Etapa")

# Seleção da etapa
st.session_state.etapa_selecionada = st.sidebar.selectbox(
    "Selecione a etapa do MHD", list(dicas.keys())
)

# Exibição da dica correspondente à etapa selecionada
st.sidebar.info(dicas[st.session_state.etapa_selecionada])

# Campo para descrever a etapa
st.sidebar.text_area(
    "Descreva a etapa:",
    value=st.session_state.descricao_etapa,
    on_change=lambda: setattr(
        st.session_state, "descricao_etapa", st.sidebar.text_area("Descreva a etapa:")
    ),
    key="descricao_etapa",
)

# Botão para adicionar nova etapa
st.sidebar.button("Adicionar Etapa", on_click=adicionar_etapa)

# Configuração do tabuleiro
st.subheader("Configuração do Tabuleiro")
fen_input = st.text_input("Configuração FEN:", value=st.session_state.fen)
if st.button("Atualizar Tabuleiro com FEN"):
    try:
        board = chess.Board(fen_input)
        st.session_state.fen = fen_input
    except ValueError:
        st.error("FEN inválido. Por favor, tente novamente.")

# Exibição do tabuleiro atual
st.subheader("Tabuleiro Atual")
chessboard(fen=st.session_state.fen, key="tabuleiro_atual")

# Exibição das etapas adicionadas
st.subheader("Etapas Adicionadas")
for idx, etapa in enumerate(st.session_state.etapas):
    st.markdown(f"**Etapa {idx + 1}: {etapa['etapa']}**")
    st.text(f"Descrição: {etapa['descricao']}")
    st.text(f"FEN: {etapa['fen']}")

import streamlit as st
import chess
import chess.svg
from io import BytesIO
from PIL import Image

# Inicializar o estado da sessão
if "etapas" not in st.session_state:
    st.session_state.etapas = []
if "descricao_etapa" not in st.session_state:
    st.session_state.descricao_etapa = ""
if "fen" not in st.session_state:
    st.session_state.fen = chess.STARTING_FEN

# Função para atualizar o tabuleiro com a configuração FEN
def atualizar_tabuleiro(fen):
    st.session_state.fen = fen

# Layout principal
st.title("Modelo Hipotético-Dedutivo no Xadrez")

# Seletor de etapas do MHD
topicos = ["Teórica", "Hipótese", "Experimento", "Conclusão"]
topico_selecionado = st.selectbox("Selecione o tópico da etapa:", topicos)

# Dicas associadas aos tópicos
dicas = {
    "Teórica": "Descreva os conceitos teóricos relevantes para a posição.",
    "Hipótese": "Formule uma hipótese para o próximo movimento ou plano.",
    "Experimento": "Teste a hipótese realizando movimentos no tabuleiro.",
    "Conclusão": "Conclua com base nos resultados do experimento."
}

# Exibir a dica correspondente ao tópico selecionado
st.markdown(f"**Dica:** {dicas[topico_selecionado]}")

# Campo para descrever a etapa
descricao = st.text_area("Descreva a etapa:", value=st.session_state.descricao_etapa, key="descricao_etapa")

# Botão para adicionar a etapa
if st.button("Adicionar Etapa"):
    if descricao:
        st.session_state.etapas.append({"tópico": topico_selecionado, "descrição": descricao})
        st.session_state.descricao_etapa = ""  # Limpar o campo de descrição

# Listar as etapas adicionadas
if st.session_state.etapas:
    st.subheader("Etapas Adicionadas:")
    for i, etapa in enumerate(st.session_state.etapas):
        st.markdown(f"**{i + 1}. {etapa['tópico']}:** {etapa['descrição']}")

# Configuração do tabuleiro
tabuleiro_fen = st.text_input("Configuração do Tabuleiro (FEN):", value=st.session_state.fen)
if st.button("Atualizar Tabuleiro com FEN"):
    atualizar_tabuleiro(tabuleiro_fen)

# Renderizar o tabuleiro atual
st.subheader("Tabuleiro Atual")
board = chess.Board(st.session_state.fen)
board_svg = chess.svg.board(board=board)

# Exibir o tabuleiro SVG diretamente no Streamlit
st.markdown(f"<div style='text-align: center'>{board_svg}</div>", unsafe_allow_html=True)

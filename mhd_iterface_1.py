import streamlit as st
import chess
import chess.svg
from cairosvg import svg2png

# Inicializar o estado
if "etapas" not in st.session_state:
    st.session_state.etapas = []
if "descricao_etapa" not in st.session_state:
    st.session_state.descricao_etapa = ""
if "fen" not in st.session_state:
    st.session_state.fen = chess.Board().fen()

# Função para adicionar etapa
def adicionar_etapa():
    if st.session_state.descricao_etapa:
        st.session_state.etapas.append(
            {
                "topico": st.session_state.topico_selecionado,
                "descricao": st.session_state.descricao_etapa,
            }
        )
        st.session_state.descricao_etapa = ""  # Limpar o campo de descrição

# Títulos e introdução
st.title("Interface MHD - Xadrez")
st.header("Etapas do Modelo Hipotético-Dedutivo")

# Seção de seleção de tópicos
st.subheader("Tópicos do MHD")
topicos_mhd = ["Observação", "Hipótese", "Experimento", "Teoria"]
st.session_state.topico_selecionado = st.selectbox(
    "Selecione um tópico do MHD:", topicos_mhd
)

# Exibir dica com base no tópico selecionado
dicas = {
    "Observação": "Observe atentamente a posição das peças no tabuleiro.",
    "Hipótese": "Levante hipóteses sobre os possíveis movimentos.",
    "Experimento": "Teste as hipóteses jogando movimentos no tabuleiro.",
    "Teoria": "Construa uma teoria sobre a estratégia geral do jogo.",
}
st.info(dicas[st.session_state.topico_selecionado])

# Campo para descrição da etapa
st.subheader("Descreva a etapa")
st.session_state.descricao_etapa = st.text_area(
    "Descrição da etapa:", value=st.session_state.descricao_etapa
)

# Botão para adicionar etapa
if st.button("Adicionar etapa"):
    adicionar_etapa()

# Configuração do tabuleiro
st.subheader("Configuração do Tabuleiro")
fen_input = st.text_input(
    "Insira a FEN (Forsyth-Edwards Notation):", value=st.session_state.fen
)
if st.button("Atualizar Tabuleiro com FEN"):
    try:
        board = chess.Board(fen_input)
        st.session_state.fen = fen_input
    except ValueError:
        st.error("FEN inválida. Por favor, insira uma configuração válida.")

# Renderizar o tabuleiro atual
st.subheader("Tabuleiro Atual")
board = chess.Board(st.session_state.fen)
svg = chess.svg.board(board=board)
png = svg2png(bytestring=svg)
st.image(png, use_column_width=True)

# Listar as etapas adicionadas
st.subheader("Etapas Adicionadas")
if st.session_state.etapas:
    for idx, etapa in enumerate(st.session_state.etapas):
        st.write(f"**Etapa {idx + 1}: {etapa['topico']}**")
        st.write(etapa["descricao"])
else:
    st.info("Nenhuma etapa adicionada ainda.")


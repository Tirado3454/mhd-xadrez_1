import streamlit as st
import chess
import chess.svg

# Configuração inicial da interface
st.set_page_config(page_title="Modelo Hipotético-Dedutivo no Xadrez", layout="centered")

# Variáveis de estado
if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = None
if "board_rendered" not in st.session_state:
    st.session_state.board_rendered = False
if "steps_description" not in st.session_state:
    st.session_state.steps_description = ""

# Função para renderizar o tabuleiro
@st.cache_data
def render_chess_board():
    board = chess.Board()
    return chess.svg.board(board)

# Tópicos disponíveis
topics = ["Aberturas", "Táticas", "Finais"]

# Layout principal
st.title("Modelo Hipotético-Dedutivo no Xadrez")

# Seletor de tópicos
selected_topic = st.selectbox("Escolha o tópico:", topics, key="topic_selector")

# Atualização das dicas ao mudar de tópico
if selected_topic != st.session_state.selected_topic:
    st.session_state.selected_topic = selected_topic
    st.session_state.steps_description = ""  # Limpa o campo de descrição

    # Dicas dinâmicas com base no tópico
    if selected_topic == "Aberturas":
        st.info("Dica: Concentre-se no controle do centro e no desenvolvimento rápido de peças.")
    elif selected_topic == "Táticas":
        st.info("Dica: Procure por táticas como garfos, cravadas e raios-X.")
    elif selected_topic == "Finais":
        st.info("Dica: Estude padrões básicos de xeque-mate e a importância da oposição.")

# Campo de entrada para descrição das etapas
steps_description = st.text_area("Descreva as etapas:", value=st.session_state.steps_description, key="steps_description_input")
st.session_state.steps_description = steps_description

# Botão para adicionar etapas
if st.button("Adicionar Etapas"):
    st.success("Etapas adicionadas com sucesso!")

    # Renderiza o tabuleiro apenas ao adicionar etapas
    st.image(render_chess_board(), use_column_width=True)
    st.session_state.board_rendered = True

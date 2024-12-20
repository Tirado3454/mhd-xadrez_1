import streamlit as st
import chess
import chess.svg

# Configuração inicial da interface
st.set_page_config(page_title="Modelo Hipotético-Dedutivo no Xadrez", layout="centered")

# Variáveis de estado
if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = None
if "steps_description" not in st.session_state:
    st.session_state.steps_description = ""
if "board_rendered" not in st.session_state:
    st.session_state.board_rendered = False

# Função para renderizar o tabuleiro
@st.cache_data
def render_chess_board():
    board = chess.Board()
    return chess.svg.board(board)

# Tópicos do MHD
topics = ["Base Teórica", "Hipótese", "Consequências", "Experimento", "Observações", "Avaliação"]

# Layout principal
st.title("Modelo Hipotético-Dedutivo no Xadrez")

# Seleção de tópico
selected_topic = st.selectbox("Escolha o tópico:", topics, key="topic_selector")

# Atualização das dicas ao selecionar um tópico
if selected_topic != st.session_state.selected_topic:
    st.session_state.selected_topic = selected_topic
    st.session_state.steps_description = ""  # Limpa o campo de descrição

    # Dicas específicas para cada tópico
    if selected_topic == "Base Teórica":
        st.info("Dica: Explique os conceitos teóricos que fundamentam sua análise.")
    elif selected_topic == "Hipótese":
        st.info("Dica: Elabore uma suposição que deseja testar.")
    elif selected_topic == "Consequências":
        st.info("Dica: Liste os desdobramentos que espera observar caso a hipótese esteja correta.")
    elif selected_topic == "Experimento":
        st.info("Dica: Descreva como você testará sua hipótese.")
    elif selected_topic == "Observações":
        st.info("Dica: Anote os resultados observados durante o experimento.")
    elif selected_topic == "Avaliação":
        st.info("Dica: Avalie se os resultados suportam sua hipótese e quais conclusões pode tirar.")

# Campo de texto para descrição das etapas
steps_description = st.text_area("Descreva as etapas:", value=st.session_state.steps_description, key="steps_description_input")
st.session_state.steps_description = steps_description

# Botão para adicionar etapas
if st.button("Adicionar Etapas"):
    st.success("Etapa adicionada com sucesso!")

    # Renderiza o tabuleiro apenas ao adicionar etapas
    if not st.session_state.board_rendered:
        st.image(render_chess_board(), use_column_width=True)
        st.session_state.board_rendered = True

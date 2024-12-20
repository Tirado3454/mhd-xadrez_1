import chess
import chess.svg
import streamlit as st
from PIL import Image
from cairosvg import svg2png
import base64
import io

# Função para criar a dica dinâmica com base na etapa selecionada
def get_dica(etapa):
    dicas = {
        "Base Teórica": "Descreva os fundamentos teóricos que embasam sua análise.",
        "Hipótese": "Formule uma hipótese clara e objetiva.",
        "Consequências": "Liste as consequências esperadas caso a hipótese esteja correta.",
        "Experimento": "Detalhe o experimento que será realizado para testar a hipótese.",
        "Observações": "Registre as observações feitas durante o experimento.",
        "Avaliação": "Avalie os resultados obtidos e tire conclusões."
    }
    return dicas.get(etapa, "Selecione uma etapa para ver a dica.")

# Configuração inicial do Streamlit
st.title("Modelo Hipotético-Dedutivo no Xadrez")
st.write("Utilize este modelo para descrever etapas do processo de análise baseado no método hipotético-dedutivo aplicado ao xadrez.")

# Inicializar estado da sessão
if "etapas" not in st.session_state:
    st.session_state.etapas = []

if "descricao_etapa" not in st.session_state:
    st.session_state.descricao_etapa = ""

if "etapa_selecionada" not in st.session_state:
    st.session_state.etapa_selecionada = ""

# Campo para selecionar a etapa
topicos = ["Base Teórica", "Hipótese", "Consequências", "Experimento", "Observações", "Avaliação"]
etapa = st.selectbox("Selecione o tópico da etapa:", options=topicos, key="etapa_selecionada")

# Mostrar dica dinâmica com base na etapa selecionada
st.info(get_dica(etapa))

# Campo para descrição da etapa
st.session_state.descricao_etapa = st.text_area("Descreva a etapa:", value=st.session_state.descricao_etapa, key="descricao_etapa")

# Botão para adicionar nova etapa
if st.button("Adicionar Etapa"):
    if st.session_state.etapa_selecionada and st.session_state.descricao_etapa:
        st.session_state.etapas.append({
            "tópico": st.session_state.etapa_selecionada,
            "descrição": st.session_state.descricao_etapa
        })
        st.session_state.descricao_etapa = ""  # Limpar campo de descrição
    else:
        st.warning("Por favor, selecione um tópico e descreva a etapa antes de adicioná-la.")

# Mostrar as etapas adicionadas
if st.session_state.etapas:
    st.subheader("Etapas Adicionadas")
    for i, etapa in enumerate(st.session_state.etapas):
        st.write(f"**{i + 1}. {etapa['tópico']}**: {etapa['descrição']}")

# Configuração do Tabuleiro
st.subheader("Configuração do Tabuleiro")
fen = st.text_input("Configuração do Tabuleiro (FEN):", value=chess.STARTING_FEN)

# Botão para atualizar o tabuleiro
if st.button("Atualizar Tabuleiro com FEN"):
    try:
        board = chess.Board(fen)
    except ValueError:
        st.error("FEN inválido. Verifique o formato e tente novamente.")
        board = chess.Board()  # Tabuleiro padrão em caso de erro

# Gerar imagem do tabuleiro
if 'board' in locals() or 'board' in globals():
    svg_board = chess.svg.board(board=board)
    png_board = svg2png(bytestring=svg_board)
    st.image(png_board, caption="Tabuleiro Atual", use_column_width=True)

# Editor do tabuleiro
st.subheader("Editor de Tabuleiro")
st.write("Use a configuração FEN para modificar a posição do tabuleiro e clique em 'Atualizar Tabuleiro com FEN'.")

# Opção para exportar as etapas em CSV
import pandas as pd
if st.button("Exportar Etapas para CSV"):
    if st.session_state.etapas:
        df = pd.DataFrame(st.session_state.etapas)
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # Codificar CSV para Base64
        href = f'<a href="data:file/csv;base64,{b64}" download="etapas_mhd.csv">Baixar arquivo CSV</a>'
        st.markdown(href, unsafe_allow_html=True)
    else:
        st.warning("Nenhuma etapa para exportar.")

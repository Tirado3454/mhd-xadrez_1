import streamlit as st
import pandas as pd
import chess
import chess.svg

# Inicialização de variáveis na sessão
if "etapas" not in st.session_state:
    st.session_state.etapas = []

if "descricao_etapa" not in st.session_state:
    st.session_state.descricao_etapa = ""

if "fen" not in st.session_state:
    st.session_state.fen = chess.Board().fen()

def adicionar_etapa(topico, descricao):
    """Função para adicionar uma nova etapa à lista de etapas."""
    nova_etapa = {"tópico": topico, "descrição": descricao}
    st.session_state.etapas.append(nova_etapa)

# Título
st.title("Modelo Hipotético-Dedutivo no Xadrez")

# Seleção de tópico
topico = st.selectbox(
    "Selecione o tópico da etapa:",
    ["Base Teórica", "Hipótese", "Consequências", "Experimento", "Observações", "Avaliação"],
    key="topico_etapa"
)

# Dicas baseadas no tópico selecionado
dicas = {
    "Base Teórica": "Defina os fundamentos teóricos relacionados à posição no tabuleiro.",
    "Hipótese": "Descreva as hipóteses que podem ser exploradas a partir dessa posição.",
    "Consequências": "Liste as possíveis consequências de cada hipótese considerada.",
    "Experimento": "Explique como testar as hipóteses no tabuleiro.",
    "Observações": "Registre as observações feitas durante os testes no tabuleiro.",
    "Avaliação": "Avalie os resultados obtidos e suas implicações."
}

st.info(dicas.get(topico, "Selecione um tópico para ver a dica."))

# Campo para descrição da etapa
st.session_state.descricao_etapa = st.text_area(
    "Descreva a etapa:",
    value=st.session_state.descricao_etapa,
    key="descricao_etapa"
)

# Botão para adicionar a etapa
if st.button("Adicionar Etapa"):
    adicionar_etapa(topico, st.session_state.descricao_etapa)
    st.session_state.descricao_etapa = ""  # Limpar o campo de descrição
    st.success("Etapa adicionada com sucesso!")

# Exibição das etapas adicionadas
if st.session_state.etapas:
    st.subheader("Etapas Adicionadas")
    etapas_df = pd.DataFrame(st.session_state.etapas)
    st.dataframe(etapas_df)

# Configuração do tabuleiro de xadrez
st.subheader("Configuração do Tabuleiro")
fen_input = st.text_input("Atualizar tabuleiro com FEN:", value=st.session_state.fen)

try:
    board = chess.Board(fen_input)
    st.session_state.fen = fen_input
    st.image(
        chess.svg.board(board=board, size=400),
        use_container_width=True,
    )
except ValueError:
    st.error("FEN inválido. Por favor, insira uma FEN válida.")

# Exportar etapas e configuração do tabuleiro
if st.button("Exportar para CSV"):
    etapas_df = pd.DataFrame(st.session_state.etapas)
    etapas_df["Tabuleiro (FEN)"] = st.session_state.fen
    etapas_df.to_csv("etapas_mhd.csv", index=False)
    st.success("Dados exportados para 'etapas_mhd.csv'")

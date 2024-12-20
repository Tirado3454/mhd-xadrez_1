import streamlit as st
import chess
import chess.svg
from streamlit.components.v1 import html

# Inicializar o estado do tabuleiro
if "tabuleiro" not in st.session_state:
    st.session_state.tabuleiro = chess.Board()

# Função para atualizar o tabuleiro com FEN
def atualizar_tabuleiro(fen):
    try:
        st.session_state.tabuleiro = chess.Board(fen)
        st.success("Tabuleiro atualizado com sucesso!")
    except ValueError:
        st.error("FEN inválido. Por favor, tente novamente.")

# Título
st.title("Modelo Hipotético-Dedutivo no Xadrez")

# Menu para escolher a etapa
topicos = ["Base Teórica", "Hipótese", "Consequências", "Experimento", "Observações", "Avaliação"]
etapa_selecionada = st.selectbox("Selecione a etapa do MHD:", topicos)

dicas = {
    "Base Teórica": "Descreva a base teórica que fundamenta esta etapa.",
    "Hipótese": "Formule uma hipótese clara e concisa.",
    "Consequências": "Liste as consequências lógicas da hipótese.",
    "Experimento": "Descreva o experimento ou procedimento para testar a hipótese.",
    "Observações": "Registre as observações feitas durante o experimento.",
    "Avaliação": "Avalie os resultados e conclua sobre a hipótese.",
}

# Mostrar dica correspondente à etapa selecionada
st.info(dicas[etapa_selecionada])

# Campo de texto para descrever a etapa
descricao_etapa = st.text_area("Descreva a etapa:")

# Botão para adicionar a etapa
if st.button("Adicionar Etapa"):
    if "etapas" not in st.session_state:
        st.session_state.etapas = []

    st.session_state.etapas.append({
        "etapa": etapa_selecionada,
        "descricao": descricao_etapa
    })

    st.success(f"Etapa '{etapa_selecionada}' adicionada com sucesso!")
    descricao_etapa = ""  # Limpar o campo após adicionar a etapa

# Exibir as etapas adicionadas
if "etapas" in st.session_state and st.session_state.etapas:
    st.subheader("Etapas Adicionadas")
    for i, etapa in enumerate(st.session_state.etapas, 1):
        st.write(f"**{i}. {etapa['etapa']}**: {etapa['descricao']}")

# Configuração do tabuleiro
st.subheader("Configuração do Tabuleiro")
fen_input = st.text_input("Insira a FEN para configurar o tabuleiro:")
if st.button("Atualizar Tabuleiro com FEN"):
    atualizar_tabuleiro(fen_input)

# Renderizar o tabuleiro atual
tabuleiro_svg = chess.svg.board(board=st.session_state.tabuleiro)
st.subheader("Tabuleiro Atual")
html(tabuleiro_svg, height=400)

# Exportar etapas e FEN para CSV
def exportar_para_csv():
    import pandas as pd
    etapas = st.session_state.get("etapas", [])
    fen_atual = st.session_state.tabuleiro.fen()

    data = [{"Etapa": etapa["etapa"], "Descrição": etapa["descricao"], "FEN": fen_atual} for etapa in etapas]
    df = pd.DataFrame(data)

    return df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Exportar para CSV",
    data=exportar_para_csv(),
    file_name="etapas_mhd.csv",
    mime="text/csv"
)

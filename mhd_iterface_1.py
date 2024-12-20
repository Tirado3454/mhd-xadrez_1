import streamlit as st
import pandas as pd
import plotly.express as px
import chess
import chess.svg

# Configuração inicial da interface
st.set_page_config(page_title="Modelo Hipotético-Dedutivo no Xadrez", layout="centered")
st.title("♟️ Modelo Hipotético-Dedutivo no Xadrez")
st.write("Preencha as etapas do método para organizar suas jogadas e estratégias e visualize o tabuleiro.")

# Inicialização da tabela de dados
if "mhd_data" not in st.session_state:
    st.session_state.mhd_data = pd.DataFrame(columns=["Etapa", "Descrição", "FEN"])

# Inicialização do tabuleiro
if "current_board" not in st.session_state:
    st.session_state.current_board = chess.Board()

# Perguntas norteadoras para cada etapa
perguntas = {
    "Base Teórica": "Qual é a base de conhecimento ou estratégia que será usada como referência?",
    "Hipótese": "O que você espera alcançar com uma jogada ou sequência de jogadas?",
    "Consequências": "Quais reações ou respostas você espera do adversário?",
    "Experimento": "Qual jogada ou sequência será aplicada para testar sua hipótese?",
    "Observações": "O que aconteceu após a jogada? O resultado foi o esperado?",
    "Avaliação": "A hipótese inicial foi confirmada, ajustada ou refutada? Por quê?"
}

# Formulário para entrada dos dados
with st.form("mhd_form"):
    etapa = st.selectbox("Selecione a Etapa", list(perguntas.keys()))
    descricao = st.text_area("Responda:", perguntas[etapa], height=100)

    # Visualização do tabuleiro atual
    st.markdown("### Tabuleiro Atual")
    st.image(chess.svg.board(board=st.session_state.current_board), use_column_width=True)

    # Movimento do tabuleiro
    movimento = st.text_input("Faça um movimento (ex.: e2e4):")
    if movimento:
        try:
            st.session_state.current_board.push_san(movimento)
        except ValueError:
            st.error("Movimento inválido.")

    submitted = st.form_submit_button("Adicionar Etapa")
    if submitted:
        if descricao.strip():
            nova_entrada = pd.DataFrame({
                "Etapa": [etapa],
                "Descrição": [descricao],
                "FEN": [st.session_state.current_board.fen()]
            })
            st.session_state.mhd_data = pd.concat([st.session_state.mhd_data, nova_entrada], ignore_index=True)
            st.success(f"Etapa '{etapa}' adicionada com sucesso!")
        else:
            st.error("A descrição não pode estar vazia!")

# Exibição da tabela dinâmica
st.subheader("Tabela do Modelo Hipotético-Dedutivo")
st.dataframe(st.session_state.mhd_data, use_container_width=True)

# Exportar a tabela para CSV
if not st.session_state.mhd_data.empty:
    st.download_button(
        label="Baixar Tabela como CSV",
        data=st.session_state.mhd_data.to_csv(index=False),
        file_name="mhd_xadrez.csv",
        mime="text/csv"
    )

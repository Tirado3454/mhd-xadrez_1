import streamlit as st
import pandas as pd
import chess
import chess.svg
import base64

# Configuração inicial da interface
st.set_page_config(page_title="Modelo Hipotético-Dedutivo no Xadrez", layout="centered")
st.title("♟️ Modelo Hipotético-Dedutivo no Xadrez")
st.write("Configure e salve posições personalizadas no tabuleiro.")

# Inicialização da tabela de dados
if "mhd_data" not in st.session_state:
    st.session_state.mhd_data = pd.DataFrame(columns=["Etapa", "Descrição", "FEN"])

# Inicialização do tabuleiro
if "current_board" not in st.session_state:
    st.session_state.current_board = chess.Board()

# Perguntas norteadoras para cada etapa do MHD
perguntas = {
    "Base Teórica": "Qual é a base de conhecimento ou estratégia que será usada como referência?",
    "Hipótese": "O que você espera alcançar com uma jogada ou sequência de jogadas?",
    "Consequências": "Quais reações ou respostas você espera do adversário?",
    "Experimento": "Qual jogada ou sequência será aplicada para testar sua hipótese?",
    "Observações": "O que aconteceu após a jogada? O resultado foi o esperado?",
    "Avaliação": "A hipótese inicial foi confirmada, ajustada ou refutada? Por quê?"
}

# Função para renderizar o tabuleiro com estilo customizado
def render_tabuleiro_customizado(board):
    return chess.svg.board(
        board=board, 
        size=320,  # Reduzindo o tamanho do tabuleiro (20% menor)
        style="""
            .square.light { fill: #ffffff; }  /* Casas claras em branco */
            .square.dark { fill: #8FBC8F; }  /* Casas escuras em verde */
        """
    )

# Função para converter SVG do tabuleiro em base64
def svg_to_base64(svg_content):
    return base64.b64encode(svg_content.encode("utf-8")).decode("utf-8")

# Configuração do tabuleiro com FEN
st.markdown("### Configuração do Tabuleiro")
fen_input = st.text_input(
    "Insira a notação FEN para configurar o tabuleiro:", 
    value=st.session_state.current_board.fen()
)

if st.button("Atualizar Tabuleiro com FEN"):
    try:
        st.session_state.current_board.set_fen(fen_input)
        st.success("Tabuleiro atualizado com sucesso!")
    except ValueError:
        st.error("Notação FEN inválida. Por favor, insira uma notação correta.")

# Visualizar o tabuleiro configurado
st.markdown("### Tabuleiro Atual")
st.image(render_tabuleiro_customizado(st.session_state.current_board), use_column_width=True)

# Formulário para entrada dos dados
st.markdown("### Adicionar Nova Etapa")
etapa = st.selectbox("Selecione a Etapa", list(perguntas.keys()))
st.markdown(f"**Dica:** {perguntas[etapa]}")  # Atualiza a dica dinamicamente com base na seleção
descricao = st.text_area("Descreva a etapa:", height=100)

if st.button("Adicionar Etapa"):
    if descricao.strip():
        nova_entrada = pd.DataFrame({
            "Etapa": [etapa],
            "Descrição": [descricao],
            "FEN": [st.session_state.current_board.fen()],
            "Imagem_Tabuleiro": [
                f"<img src='data:image/svg+xml;base64,{svg_to_base64(render_tabuleiro_customizado(st.session_state.current_board))}' />"
            ]
        })
        st.session_state.mhd_data = pd.concat([st.session_state.mhd_data, nova_entrada], ignore_index=True)
        st.success(f"Etapa '{etapa}' adicionada com sucesso!")
    else:
        st.error("A descrição não pode estar vazia!")

# Exibição da tabela dinâmica
st.subheader("Tabela do Modelo Hipotético-Dedutivo")
if not st.session_state.mhd_data.empty:
    st.write(st.session_state.mhd_data[["Etapa", "Descrição"]])  # Mostra apenas as colunas relevantes
else:
    st.info("Nenhuma etapa adicionada ainda.")

# Exportar a tabela para CSV
st.markdown("### Exportação de Dados")
if not st.session_state.mhd_data.empty:
    csv_data = st.session_state.mhd_data.drop(columns=["Imagem_Tabuleiro"]).to_csv(index=False)
    st.download_button(
        label="Baixar Tabela como CSV",
        data=csv_data,
        file_name="mhd_xadrez.csv",
        mime="text/csv"
    )
else:
    st.info("Nenhum dado disponível para exportação.")

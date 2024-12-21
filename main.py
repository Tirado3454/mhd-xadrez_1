import streamlit as st

# Inicializar o estado
if "etapas" not in st.session_state:
    st.session_state.etapas = []
if "descricao_etapa" not in st.session_state:
    st.session_state.descricao_etapa = ""
if "topico_selecionado" not in st.session_state:
    st.session_state.topico_selecionado = "Base Teórica"  # Inicialização padrão

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
st.title("Interface MHD - Etapas Escritas")
st.header("Etapas do Modelo Hipotético-Dedutivo")

# Seção de seleção de tópicos
st.subheader("Tópicos do MHD")
topicos_mhd = [
    "Base Teórica",
    "Observação",
    "Formulação de Hipóteses",
    "Dedução",
    "Teste por Experimento",
    "Análise dos Resultados",
    "Conclusão",
]
st.write("Tópicos carregados:", topicos_mhd)  # Para depuração
st.session_state.topico_selecionado = st.selectbox(
    "Selecione um tópico do MHD:", topicos_mhd
)

# Exibir dica com base no tópico selecionado
dicas = {
    "Base Teórica": "Considere o conhecimento já existente que fundamenta sua análise.",
    "Observação": "Observe atentamente e registre os detalhes relevantes.",
    "Formulação de Hipóteses": "Levante hipóteses sobre possíveis padrões ou explicações.",
    "Dedução": "Deduza as consequências lógicas das hipóteses formuladas.",
    "Teste por Experimento": "Teste suas hipóteses de maneira controlada.",
    "Análise dos Resultados": "Analise os dados obtidos para validar ou refutar a hipótese.",
    "Conclusão": "Elabore uma conclusão baseada nas observações e experimentos realizados.",
}
if st.session_state.topico_selecionado in dicas:
    st.info(dicas[st.session_state.topico_selecionado])

# Campo para descrição da etapa
st.subheader("Descreva a etapa")
st.session_state.descricao_etapa = st.text_area(
    "Descrição da etapa:", value=st.session_state.descricao_etapa
)

# Botão para adicionar etapa
if st.button("Adicionar etapa"):
    adicionar_etapa()

# Listar as etapas adicionadas
st.subheader("Etapas Adicionadas")
if st.session_state.etapas:
    for idx, etapa in enumerate(st.session_state.etapas):
        st.write(f"**Etapa {idx + 1}: {etapa['topico']}**")
        st.write(etapa["descricao"])
else:
    st.info("Nenhuma etapa adicionada ainda.")

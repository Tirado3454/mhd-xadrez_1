import streamlit as st

# Inicializar o session_state para descricao_etapa
if "descricao_etapa" not in st.session_state:
    st.session_state["descricao_etapa"] = ""

# Inicializar o session_state para etapas
if "etapas" not in st.session_state:
    st.session_state["etapas"] = []

st.title("Modelo Hipotético-Dedutivo no Xadrez")

# Dicionário de tópicos e dicas
topicos_e_dicas = {
    "Base Teórica": "Descreva as bases teóricas do problema que você está investigando.",
    "Hipótese": "Formule uma hipótese clara e objetiva para o problema.",
    "Consequências": "Identifique as consequências que derivam da hipótese formulada.",
    "Experimento": "Descreva como o experimento será conduzido para testar a hipótese.",
    "Observações": "Registre suas observações durante ou após o experimento.",
    "Avaliação": "Avalie os resultados obtidos e conclua se a hipótese foi confirmada ou refutada."
}

# Seleção de tópico
topico_selecionado = st.selectbox("Selecione o tópico da etapa", options=list(topicos_e_dicas.keys()))

# Exibir a dica correspondente ao tópico selecionado
if topico_selecionado:
    st.info(topicos_e_dicas[topico_selecionado])

# Campo de descrição da etapa
descricao_etapa = st.text_area("Descreva a etapa", value=st.session_state["descricao_etapa"])

# Botão para adicionar etapa
if st.button("Adicionar Etapa"):
    if topico_selecionado and descricao_etapa:
        st.session_state.etapas.append({"etapa": topico_selecionado, "descricao": descricao_etapa})
        st.session_state["descricao_etapa"] = ""  # Limpar o campo de descrição
        st.success(f"Etapa '{topico_selecionado}' adicionada com sucesso!")
    else:
        st.error("Por favor, selecione um tópico e preencha a descrição da etapa.")

# Exibir as etapas adicionadas
if st.session_state.etapas:
    st.subheader("Etapas Adicionadas")
    for idx, etapa in enumerate(st.session_state.etapas):
        st.write(f"**{idx + 1}. {etapa['etapa']}**: {etapa['descricao']}")

# Placeholder para adicionar outras funcionalidades futuras
st.write("\n")


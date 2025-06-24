import streamlit as st
import os
import google.generativeai as genai
from pymongo import MongoClient

# Configuração inicial
st.set_page_config(
    layout="wide",
    page_title="Gerador de Conteúdo SEO para IA",
    page_icon="📊"
)

st.title('Gerador de Conteúdo SEO para IA')
st.caption('Crie conteúdo otimizado para resultados de busca em assistentes de IA')

# Inicializar Gemini
gemini_api_key = os.getenv("GEM_API_KEY")
genai.configure(api_key=gemini_api_key)
modelo_texto = genai.GenerativeModel("gemini-1.5-flash")

# CSS personalizado
st.markdown("""
<style>
    /* Abas roláveis */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        overflow-x: auto;
        flex-wrap: nowrap;
        padding-bottom: 5px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 8px 16px;
        border-radius: 4px 4px 0 0;
        white-space: nowrap;
        font-size: 14px;
        transition: all 0.2s;
    }
    .stTabs [aria-selected="true"] {
        background-color: #f0f2f6;
        font-weight: 600;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #f8f9fa;
    }
    
    /* Melhorias gerais */
    textarea {
        min-height: 120px !important;
    }
    [data-testid="stMarkdownContainer"] ul {
        padding-left: 1.5rem;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        transition: all 0.3s;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    
    /* Barra de rolagem */
    .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar {
        height: 6px;
    }
    .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 3px;
    }
    .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar-thumb {
        background: #888;
        border-radius: 3px;
    }
    .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar-thumb:hover {
        background: #555;
    }
</style>
""", unsafe_allow_html=True)

# Nomes das abas
tab_names = [
    "🔍 Construtor de Páginas",
    "🧠 Expansor de Tópicos",
    "🔬 Analisador de Resultados",
    "✍️ Reescritor de Conteúdo",
    "✅ Validador SEO",
    "🆚 Comparador de Produtos",
    "🛒 Guia do Comprador",
    "⚙️ Explicador de Recursos",
    "❌ Desmistificador",
    "❓ Gerador de FAQ"
]

# Criar abas
tabs = st.tabs(tab_names)

# ==============================================
# 1. CONSTRUTOR DE PÁGINAS DE BUSCA
# ==============================================
with tabs[0]:
    st.header("📝 Construtor de Páginas para Buscas em IA")
    st.write("Crie artigos completos otimizados para serem citados por assistentes como ChatGPT e Gemini")
    
    col1, col2 = st.columns(2)
    with col1:
        target_query = st.text_input(
            "Consulta de Busca Alvo*",
            placeholder="Ex: 'Como aumentar conversões com SEO em 2025?'",
            key="consulta_1"
        )
        key_points = st.text_area(
            "Pontos-chave para destacar*",
            placeholder="Ex: 'Estratégias comprovadas, casos de sucesso, ferramentas essenciais'",
            key="pontos_chave_1"
        )
    with col2:
        word_count = st.slider(
            "Tamanho do Artigo (palavras)",
            400, 1500, 800,
            key="tamanho_1"
        )
        reading_level = st.selectbox(
            "Nível de Complexidade",
            ["Simples (ensino fundamental)", "Intermediário (ensino médio)", "Avançado (superior)", "Técnico (especialistas)"],
            key="nivel_1"
        )
    
    if st.button("✨ Gerar Artigo Completo", key="btn_artigo_1"):
        if not target_query or not key_points:
            st.warning("Preencha todos os campos obrigatórios (*)")
        else:
            with st.spinner('Otimizando conteúdo para mecanismos de IA...'):
                prompt = f"""
                Você é um redator especialista em SEO para IA. Crie um artigo completo que será citado como fonte por assistentes de IA.

                **Consulta do Usuário:** {target_query}
                **Destaques Principais:** {key_points}
                **Tamanho:** {word_count} palavras
                **Nível:** {reading_level}

                **Estrutura Requerida:**
                1. Resumo executivo (máximo 45 palavras)
                2. Introdução (contextualize o problema)
                3. Análise detalhada (com dados e exemplos)
                4. Soluções práticas (passo a passo)
                5. Conclusão (recapitulação + próximos passos)

                **Formato:**
                - Use markdown
                - Títulos claros (##, ###)
                - Listas e tabelas quando apropriado
                - Linguagem natural e técnica balanceada
                """
                
                response = modelo_texto.generate_content(prompt)
                st.markdown(response.text)
                st.success("✅ Artigo gerado com otimização para citação em IA!")

# ==============================================
# 2. EXPANSOR DE TÓPICOS
# ==============================================
with tabs[1]:
    st.header("🧠 Gerador de Ideias para Conteúdo")
    st.write("Descubra subtópicos e perguntas que seu público pesquisa em assistentes de IA")
    
    main_topic = st.text_input(
        "Tema Principal*",
        placeholder="Ex: 'Marketing de conteúdo para ecommerce'",
        key="tema_principal_2"
    )
    audience = st.text_input(
        "Perfil do Público*",
        placeholder="Ex: 'pequenos negócios, empreendedores digitais'",
        key="publico_2"
    )
    
    if st.button("🧩 Gerar Ideias de Conteúdo", key="btn_ideias_2"):
        if not main_topic or not audience:
            st.warning("Preencha todos os campos obrigatórios (*)")
        else:
            with st.spinner('Analisando tendências de busca em IA...'):
                prompt = f"""
                Atue como um estrategista de conteúdo para IA. Para o tema "{main_topic}", gere:

                1. 10 perguntas frequentes que o público "{audience}" faz em assistentes
                2. 5 ângulos inovadores para abordar o tema
                3. 3 formatos de conteúdo com alto potencial de compartilhamento

                Para cada item, inclua:
                - Termos exatos de busca
                - Potencial de trafego (baixo/médio/alto)
                - Exemplo de resposta resumida (30 palavras)

                Apresente em tabela markdown com colunas:
                | Tipo | Termo de Busca | Potencial | Resumo Exemplo |
                |------|----------------|-----------|----------------|
                """
                
                response = modelo_texto.generate_content(prompt)
                st.markdown(response.text)
                st.download_button(
                    "📥 Baixar Tabela Completa",
                    response.text,
                    file_name=f"ideias_conteudo_{main_topic[:20]}.md"
                )

# ==============================================
# 3. ANALISADOR DE RESULTADOS ZERO-CLICK
# ==============================================
with tabs[2]:
    st.header("🔍 Engenharia Reversa de Respostas de IA")
    st.write("Analise respostas de assistentes e aprenda a estruturar seu conteúdo para ser citado")
    
    example_response = st.text_area(
        "Cole uma resposta de IA para análise*",
        height=150,
        placeholder="Ex: Resposta do ChatGPT ou Gemini sobre seu tópico...",
        key="resposta_3"
    )
    
    if st.button("🔬 Analisar Estrutura da Resposta", key="btn_analise_3"):
        if not example_response:
            st.warning("Cole uma resposta para análise")
        else:
            with st.spinner('Decifrando padrões de citação em IA...'):
                prompt = f"""
                Faça uma análise detalhada desta resposta de IA:

                **Resposta para Análise:**
                {example_response}

                **Itens a Avaliar:**
                1. Estrutura da informação (hierarquia)
                2. Tom de voz e estilo
                3. Elementos mais citáveis
                4. Palavras-chave estratégicas
                5. Formatação que facilita a citação

                **Saída Esperada:**
                - Lista de pontos fortes
                - Sugestões de melhoria
                - Modelo para replicar o sucesso
                - Exemplo de conteúdo otimizado

                Use markdown com destaques em **negrito** para insights.
                """
                
                response = modelo_texto.generate_content(prompt)
                st.markdown(response.text)

# ==============================================
# 4. REESCRITOR DE CONTEÚDO
# ==============================================
with tabs[3]:
    st.header("✍️ Otimizador de Conteúdo Existente")
    st.write("Transforme artigos comuns em conteúdo perfeito para citação em IA")
    
    original_content = st.text_area(
        "Cole seu conteúdo atual*",
        height=200,
        placeholder="Texto, artigo ou post que deseja otimizar...",
        key="conteudo_4"
    )
    target_query = st.text_input(
        "Consulta de Busca Alvo*",
        placeholder="Qual pergunta este conteúdo deve responder?",
        key="query_4"
    )
    
    if st.button("⚡ Otimizar para IA", key="btn_otimizar_4"):
        if not original_content or not target_query:
            st.warning("Preencha todos os campos obrigatórios")
        else:
            with st.spinner('Reescrevendo para maximizar citações...'):
                prompt = f"""
                Transforme este conteúdo para ser perfeito para citação em IA:

                **Consulta Alvo:** {target_query}
                **Conteúdo Original:**
                {original_content}

                **Instruções:**
                1. Comece com TLDR de 40 palavras
                2. Reescreva mantendo informações-chave
                3. Adicione estruturação clara (H2, H3)
                4. Insere exemplos práticos
                5. Inclua dados quando possível
                6. Finalize com ações concretas

                **Formato:**
                - Markdown rigoroso
                - Parágrafos curtos (máx. 3 linhas)
                - Listas numeradas/bullets
                - Destaques para citações
                """
                
                response = modelo_texto.generate_content(prompt)
                st.markdown(response.text)
                st.toast('Conteúdo otimizado com sucesso!', icon='🎯')

# ==============================================
# 5. VALIDADOR DE CONTEÚDO
# ==============================================
with tabs[4]:
    st.header("✅ Analisador de Qualidade SEO/IA")
    st.write("Verifique se seu conteúdo está pronto para rankear em assistentes virtuais")
    
    content_to_check = st.text_area(
        "Cole seu conteúdo para análise*",
        height=250,
        placeholder="Artigo, post ou texto para avaliação...",
        key="conteudo_5"
    )
    
    col1, col2 = st.columns(2)
    with col1:
        main_keyword = st.text_input(
            "Palavra-chave Principal",
            placeholder="Termo principal de busca",
            key="keyword_5"
        )
    with col2:
        content_type = st.selectbox(
            "Tipo de Conteúdo",
            ["Blog Post", "Guia", "Artigo Técnico", "Página de Produto", "FAQ"],
            key="tipo_5"
        )
    
    if st.button("🔍 Analisar Conteúdo", key="btn_analisar_5"):
        if not content_to_check:
            st.warning("Insira o conteúdo para análise")
        else:
            with st.spinner('Avaliando 12 fatores de otimização...'):
                prompt = f"""
                Atue como auditor de conteúdo para IA. Analise este material:

                **Conteúdo:**
                {content_to_check}

                **Parâmetros:**
                - Palavra-chave: {main_keyword or 'Não especificada'}
                - Tipo: {content_type}
                
                **Checklist de Análise:**
                1. Clareza da resposta principal
                2. Estrutura para citação
                3. Densidade de informações
                4. Autoridade e fontes
                5. Elementos visuais sugeridos
                6. Otimização técnica
                7. Tom e engajamento
                8. Potencial de snippet
                
                **Saída:**
                - Pontuação de 0-100
                - 3 melhorias urgentes
                - Sugestões concretas
                - Exemplo de trecho otimizado
                """
                
                response = modelo_texto.generate_content(prompt)
                st.markdown(response.text)

# ==============================================
# 6. COMPARADOR DE PRODUTOS
# ==============================================
with tabs[5]:
    st.header("🆚 Gerador de Comparações Técnicas")
    st.write("Crie comparações detalhadas que aparecem como respostas em buscas")
    
    product_a = st.text_input(
        "Seu Produto/Serviço*",
        placeholder="Nome do seu produto",
        key="produto_a_6"
    )
    product_b = st.text_input(
        "Concorrente*",
        placeholder="Nome do concorrente",
        key="produto_b_6"
    )
    comparison_aspects = st.text_area(
        "Critérios de Comparação",
        placeholder="Ex: preço, recursos, atendimento, integrações...",
        key="aspectos_6"
    )
    
    if st.button("📊 Gerar Comparação Detalhada", key="btn_comparacao_6"):
        if not product_a or not product_b:
            st.warning("Preencha os produtos para comparação")
        else:
            with st.spinner('Criando análise comparativa...'):
                prompt = f"""
                Crie uma comparação detalhada entre:
                - {product_a}
                - {product_b}
                
                **Critérios:** {comparison_aspects or 'Use os padrões do mercado'}
                
                **Estrutura:**
                1. Visão geral (50 palavras)
                2. Tabela comparativa (recursos, preços, etc.)
                3. Vantagens de cada um
                4. Casos de uso ideais
                5. Verdict final (quando escolher cada)
                
                **Formato:**
                - Markdown com tabelas
                - Linguagem imparcial
                - Dados concretos quando possível
                - Destaque para diferenciais
                """
                
                response = modelo_texto.generate_content(prompt)
                st.markdown(response.text)

# ==============================================
# 7. GUIA DO COMPRADOR
# ==============================================
with tabs[6]:
    st.header("🛒 Criador de Guias de Compra")
    st.write("Produza guias completos que respondem a consultas do tipo 'melhor X para Y'")
    
    product_category = st.text_input(
        "Categoria de Produto*",
        placeholder="Ex: 'ferramentas de email marketing'",
        key="categoria_7"
    )
    buyer_profile = st.text_input(
        "Perfil do Comprador*",
        placeholder="Ex: 'pequenas empresas com orçamento limitado'",
        key="perfil_7"
    )
    top_products = st.text_area(
        "Produtos para Incluir (um por linha)",
        placeholder="Liste 3-5 produtos, incluindo o seu",
        key="produtos_7"
    )
    
    if st.button("📋 Gerar Guia Completo", key="btn_guia_7"):
        if not product_category or not buyer_profile:
            st.warning("Preencha categoria e perfil do comprador")
        else:
            with st.spinner('Elaborando guia especializado...'):
                prompt = f"""
                Crie um guia de compra para {product_category} direcionado a {buyer_profile}.

                **Produtos Analisados:**
                {top_products or 'Inclua os principais do mercado'}

                **Seções Obrigatórias:**
                1. Introdução (contextualize a necessidade)
                2. Critérios de avaliação (o que considerar)
                3. Análise individual de cada opção
                4. Tabela comparativa
                5. Recomendações por cenário
                6. Onde comprar/melhores ofertas

                **Tom:**
                - Informativo mas acessível
                - Comparativo justo
                - Destaque para soluções ideais
                """
                
                response = modelo_texto.generate_content(prompt)
                st.markdown(response.text)

# ==============================================
# 8. EXPLICADOR DE RECURSOS
# ==============================================
with tabs[7]:
    st.header("⚙️ Documentador de Funcionalidades")
    st.write("Crie explicações técnicas que aparecem como respostas diretas em buscas")
    
    feature_name = st.text_input(
        "Nome do Recurso/Funcionalidade*",
        placeholder="Ex: 'segmentação avançada de público'",
        key="recurso_8"
    )
    product_context = st.text_input(
        "No Contexto de (Produto/Plataforma)",
        placeholder="Ex: 'no MailChimp Pro'",
        key="contexto_8"
    )
    use_cases = st.text_area(
        "Casos de Uso Típicos",
        placeholder="Situações onde este recurso é útil...",
        key="casos_8"
    )
    
    if st.button("📚 Gerar Explicação Técnica", key="btn_explicacao_8"):
        if not feature_name:
            st.warning("Descreva o recurso a ser documentado")
        else:
            with st.spinner('Criando documentação otimizada...'):
                prompt = f"""
                Crie uma explicação completa sobre: {feature_name} {product_context or ''}

                **Casos de Uso:** {use_cases or 'Descreva os principais'}

                **Estrutura:**
                1. Definição simples (1 frase)
                2. Funcionamento técnico (nível adequado)
                3. Benefícios concretos
                4. Exemplo prático
                5. Como acessar/configurar
                6. Perguntas frequentes

                **Formato:**
                - Markdown com headers
                - Screenshots sugeridos [INSERIR IMAGEM]
                - Notas técnicas em blocos de código
                - Links para aprofundamento
                """
                
                response = modelo_texto.generate_content(prompt)
                st.markdown(response.text)

# ==============================================
# 9. DESMISTIFICADOR
# ==============================================
with tabs[8]:
    st.header("❌ Desmistificador de Conceitos")
    st.write("Responda a mitos e equívocos comuns no seu nicho")
    
    myth = st.text_input(
        "Mito ou Equívoco*",
        placeholder="Ex: 'SEO leva meses para mostrar resultados'",
        key="mito_9"
    )
    truth = st.text_area(
        "Verdade/Fatos*",
        placeholder="Ex: 'Técnicas modernas podem mostrar resultados em semanas...'",
        key="verdade_9"
    )
    evidence = st.text_area(
        "Provas/Referências",
        placeholder="Estudos, casos, dados que comprovam...",
        key="provas_9"
    )
    
    if st.button("🔎 Gerar Resposta Completa", key="btn_resposta_9"):
        if not myth or not truth:
            st.warning("Preencha o mito e a verdade correspondente")
        else:
            with st.spinner('Construindo argumentação sólida...'):
                prompt = f"""
                Desconstrua este mito: "{myth}"

                **Verdade:** {truth}
                **Evidências:** {evidence or 'Inclua dados relevantes'}

                **Estrutura:**
                1. Origem do mito (por que existe)
                2. Fatos concretos (com provas)
                3. Exemplo real/analogia
                4. Implicações de acreditar no mito
                5. Como aplicar a verdade na prática

                **Tom:**
                - Educativo, não confrontativo
                - Baseado em dados
                - Chamada para ação positiva
                """
                
                response = modelo_texto.generate_content(prompt)
                st.markdown(response.text)

# ==============================================
# 10. GERADOR DE FAQ
# ==============================================
with tabs[9]:
    st.header("❓ Criador de Perguntas Frequentes")
    st.write("Desenvolva respostas completas para dúvidas comuns do seu público")
    
    faq_question = st.text_input(
        "Pergunta*",
        placeholder="Ex: 'Como integrar X com Y?'",
        key="pergunta_10"
    )
    technical_level = st.selectbox(
        "Nível Técnico da Resposta",
        ["Leigo", "Intermediário", "Avançado"],
        key="nivel_10"
    )
    steps_needed = st.slider(
        "Passos Detalhados",
        1, 10, 3,
        help="Quantos passos a resposta deve incluir?",
        key="passos_10"
    )
    
    if st.button("📝 Gerar Resposta Ideal", key="btn_faq_10"):
        if not faq_question:
            st.warning("Digite a pergunta a ser respondida")
        else:
            with st.spinner('Elaborando resposta perfeita...'):
                prompt = f"""
                Crie uma resposta completa para esta pergunta:
                "{faq_question}"

                **Nível Técnico:** {technical_level}
                **Detalhamento:** {steps_needed} passos principais

                **Componentes:**
                1. Resposta direta (40 palavras)
                2. Explicação detalhada
                3. Passo-a-passo (se aplicável)
                4. Problemas comuns + soluções
                5. Recursos adicionais

                **Formato:**
                - Markdown com headers
                - Listas numeradas para passos
                - Destaques para dicas importantes
                - Blocos de código se técnico
                """
                
                response = modelo_texto.generate_content(prompt)
                st.markdown(response.text)

# JavaScript para melhorar navegação
st.components.v1.html("""
<script>
// Suaviza rolagem entre abas
document.querySelectorAll('[data-baseweb="tab"]').forEach(tab => {
    tab.addEventListener('click', () => {
        document.querySelector('.stTabs [aria-selected="true"]').scrollIntoView({
            behavior: 'smooth',
            block: 'nearest',
            inline: 'center'
        });
    });
});

// Atualiza URL ao mudar de aba
const observer = new MutationObserver(() => {
    const activeTab = document.querySelector('.stTabs [aria-selected="true"]');
    if (activeTab) {
        const tabName = activeTab.textContent.trim();
        window.history.replaceState(null, null, `#${encodeURIComponent(tabName)}`);
    }
});
observer.observe(document.querySelector('.stTabs'), {
    attributes: true,
    childList: true,
    subtree: true
});

// Rolagem para aba ao carregar com hash
window.addEventListener('load', () => {
    if (window.location.hash) {
        const targetTab = decodeURIComponent(window.location.hash.substring(1));
        const tabs = document.querySelectorAll('[data-baseweb="tab"]');
        tabs.forEach((tab, index) => {
            if (tab.textContent.trim() === targetTab) {
                tab.click();
            }
        });
    }
});
</script>
""")

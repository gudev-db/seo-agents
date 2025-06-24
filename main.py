import streamlit as st
import os
import google.generativeai as genai
from pymongo import MongoClient

# Configuração inicial
st.set_page_config(
    layout="wide",
    page_title="AI SEO Content Builder",
    page_icon="📊"
)

st.title('AI SEO Content Builder')
st.caption('Generate content optimized for zero-click AI search results')

# Initialize Gemini
gemini_api_key = os.getenv("GEM_API_KEY")
genai.configure(api_key=gemini_api_key)
modelo_texto = genai.GenerativeModel("gemini-1.5-flash")

# Create tabs for each agent type
tab_names = [
    "🔍 Search Page Builder",
    "🧠 Topic Expander",
    "🔬 Zero-Click Analyzer",
    "✍️ Content Rewriter",
    "✅ SEO Validator",
    "🆚 Comparison Generator",
    "🛒 Buyer's Guide",
    "⚙️ Feature Explainer",
    "❌ Myth Buster",
    "❓ FAQ Generator"
]

tabs = st.tabs(tab_names)

# 1. AI Search Page Builder
with tabs[0]:
    st.header("AI Search Page Builder")
    st.write("Create AI-optimized articles designed to be quoted by AI assistants")
    
    target_query = st.text_input("Target Query", placeholder="E.g., 'How is [Your Product] better than [Competitor] in 2025?'", key="your_tool")
    key_points = st.text_area("Key Points to Emphasize", placeholder="E.g., 'Ease of onboarding, integrations, and pricing transparency'")
    word_count = st.slider("Target Word Count", 400, 1000, 600)
    reading_level = st.selectbox("Reading Level", ["8th grade", "High school", "College-level", "Professional"])
    
    if st.button("Generate Article"):
        with st.spinner('Creating AI-optimized content...'):
            prompt = f"""
            You are an expert AI SEO Content Builder. Write one AI-optimized, source-worthy article that answers this search query clearly, concisely, and thoroughly.

            ### Target Query ###
            {target_query}

            ### Key Points to Emphasize ###
            {key_points}

            ### Instructions ###
            - Start with a <45-word TLDR answer
            - Include sections:
              - Problem with current approach
              - Why our solution is better
              - Fast-Start Checklist
            - Use markdown formatting
            - Target {word_count} words at {reading_level} reading level
            - Include relevant keyword variants
            """
            
            response = modelo_texto.generate_content(prompt)
            st.markdown(response.text)

# 2. Topic Expansion Brainstormer
with tabs[1]:
    st.header("AI Search Topic Expansion")
    st.write("Generate AI search-optimized query angles for your core topic")
    
    core_topic = st.text_input("Core Topic", placeholder="E.g., 'AI video tools for creators'",key="your_tool1")
    target_audience = st.text_input("Target Audience", placeholder="E.g., 'bootstrapped startups', 'B2B SaaS teams'",key="your_tool2")
    
    if st.button("Generate Query Angles"):
        with st.spinner('Brainstorming search angles...'):
            prompt = f"""
            Act as an AI SEO strategist. Based on the core topic of "{core_topic}", generate 10 AI search-optimized query angles people are likely to ask AI assistants.

            For each, provide:
            - The full query
            - Why it matters for zero-click ranking
            - A sample TLDR answer (<45 words)

            Tailor examples toward: {target_audience}
            Return results in Markdown table format.
            """
            
            response = modelo_texto.generate_content(prompt)
            st.markdown(response.text)

# 3. Zero-Click Analyzer
with tabs[2]:
    st.header("Reverse Engineer Zero-Click Results")
    st.write("Analyze and replicate successful AI search results")
    
    example_answer = st.text_area("Paste Zero-Click Summary to Analyze", height=150)
    target_query = st.text_input("Target Query for Replication", placeholder="The query you want to rank for",key="your_tool3")
    audience = st.selectbox("Audience", ["Content marketing team", "In-house writers", "SEO contractors"])
    
    if st.button("Analyze & Create Guide"):
        with st.spinner('Analyzing and creating replication guide...'):
            prompt = f"""
            Analyze this AI search result and reverse engineer what makes it perform well:

            ### Example Answer ###
            {example_answer}

            ### Deliverables ###
            - What makes this answer work (structure, tone, semantics)
            - Best practices to replicate this
            - Outline for creating a better source page for: {target_query}

            Audience: {audience}
            """
            
            response = modelo_texto.generate_content(prompt)
            st.markdown(response.text)

# 4. Content Rewriter
with tabs[3]:
    st.header("Zero-Click Optimized Rewrite")
    st.write("Transform existing content for better AI search performance")
    
    original_content = st.text_area("Original Paragraph", height=150)
    target_question = st.text_input("Target Question This Should Answer",key="your_too4l")
    
    if st.button("Optimize Content"):
        with st.spinner('Rewriting for AI search...'):
            prompt = f"""
            Rewrite this content to:
            1. Start with a <45-word TLDR answering: "{target_question}"
            2. Improve clarity, tone, and format for zero-click AI search
            3. Follow AISCO best practices (structured, factual, light keywords)
            4. Use Markdown headers/bullets if appropriate

            ### Original Content ###
            {original_content}
            """
            
            response = modelo_texto.generate_content(prompt)
            st.markdown(response.text)

# 5. SEO Validator
with tabs[4]:
    st.header("AI SEO Readiness Validator")
    st.write("Assess content for zero-click AI search optimization")
    
    content_to_analyze = st.text_area("Content to Analyze", height=200)
    target_query = st.text_input("Target Query for This Content",key="your_tool5")
    
    if st.button("Analyze Content"):
        with st.spinner('Evaluating AI SEO readiness...'):
            prompt = f"""
            Act as an AI SEO content reviewer. Analyze this content for zero-click AI search optimization:

            ### Content ###
            {content_to_analyze}

            ### Deliverables ###
            - Identify factual inconsistencies
            - Suggest formatting/structural improvements
            - Evaluate AI-suitability (clarity, TLDR, chunking)
            - Highlight "quotability" opportunities

            Target query: "{target_query}"
            """
            
            response = modelo_texto.generate_content(prompt)
            st.markdown(response.text)

# 6. Comparison Generator
with tabs[5]:
    st.header("Comparison Page Generator")
    st.write("Create AI-optimized comparison pages")
    
    target_query = st.text_input("Comparison Query", placeholder="E.g., '[Your Product] vs [Competitor] for [Use Case] in 2025'",key="your_tool6")
    your_product = st.text_input("Your Product Name",key="your_tool7")
    competitor = st.text_input("Competitor Name",key="your_tool8")
    
    if st.button("Generate Comparison"):
        with st.spinner('Creating comparison page...'):
            prompt = f"""
            Act as an AI SEO expert. Write an AI-optimized comparison page for:

            ### Target Query ###
            {target_query}

            ### Instructions ###
            - Start with <45-word TLDR stating key difference
            - Create comparison table (Features, Pricing, Ease of use, Integrations, Support)
            - Add "When to Choose {your_product}" and "When to Choose {competitor}" sections
            - Use markdown, clear headers, fact-based language
            - Optimize for LLM parsing
            """
            
            response = modelo_texto.generate_content(prompt)
            st.markdown(response.text)

# 7. Buyer's Guide
with tabs[6]:
    st.header("AI-Optimized Buyer's Guide")
    st.write("Create guides that AI will quote for product selection queries")
    
    product_type = st.text_input("Product Type", placeholder="E.g., 'project management tools for startups'",key="your_tool9")
    target_query = st.text_input("Target Buyer Query", placeholder="E.g., 'best CRM for early-stage SaaS startups in 2025'",key="your_tool11")
    audience = st.text_input("Target Audience", placeholder="E.g., 'startup founders, nonprofit managers'",key="your_tool111")
    your_tool = st.text_input("Your Tool Name",key="your_tool1111")
    
    if st.button("Generate Buyer's Guide"):
        with st.spinner("Creating AI-friendly buyer's guide"):
            prompt = f"""
            Create an LLM-friendly buyer's guide that AI will quote for:

            ### Target Query ###
            {target_query}

            ### Audience ###
            {audience}

            ### Instructions ###
            - Start with <45-word TLDR of key takeaway
            - Include:
              - What to look for when choosing {product_type}
              - List of 3-5 top tools (including {your_tool})
              - Pros/cons for each
              - "How to Decide" checklist
            - Use AI SEO best practices
            """
            
            response = modelo_texto.generate_content(prompt)
            st.markdown(response.text)

# 8. Feature Explainer
with tabs[7]:
    st.header("Feature Explainer")
    st.write("Create AI-search-optimized feature explanations")
    
    feature_name = st.text_input("Feature Name", placeholder="E.g., 'automated lead scoring in [Your Product]'",key="your_too66l")
    target_query = st.text_input("Target Query for This Feature", placeholder="E.g., 'What is automated lead scoring and how does it work in HubSpot?'",key="your_tool99")
    your_product = st.text_input("Your Product Name",key="your_tool999")
    
    if st.button("Generate Feature Explanation"):
        with st.spinner('Creating feature explainer...'):
            prompt = f"""
            Create an AI-search-optimized feature explanation for:

            ### Feature ###
            {feature_name}

            ### Query ###
            {target_query}

            ### Instructions ###
            - Start with <45-word TLDR
            - Explain:
              - What it does
              - Why it matters
              - How {your_product} implements it better
            - Add "Quick Use Case" scenario
            - "How to Get Started" checklist
            - Use markdown headers and short paragraphs
            """
            
            response = modelo_texto.generate_content(prompt)
            st.markdown(response.text)

# 9. Myth-Busting Page
with tabs[8]:
    st.header("Myth-Busting Page")
    st.write("Create content that debunks myths for AI search queries")
    
    myth_query = st.text_input("Myth-Based Query", placeholder="E.g., 'Is [Your Product] too expensive for small businesses?'",key="your_too432l")
    counter_argument = st.text_area("Your Counter Argument", placeholder="E.g., 'We offer a free plan and flexible pricing tiers.'")
    
    if st.button("Generate Myth-Busting Content"):
        with st.spinner('Creating myth-busting article...'):
            prompt = f"""
            Write an AI-optimized myth-busting article for:

            ### Query ###
            {myth_query}

            ### Counter Argument ###
            {counter_argument}

            ### Instructions ###
            - Start with <45-word summary debunking the myth
            - Sections:
              - What People Think
              - Why That's Wrong
              - What's Actually True
              - How to Try It Yourself
            - Include examples and AI-quotable phrasing
            - Use markdown formatting
            """
            
            response = modelo_texto.generate_content(prompt)
            st.markdown(response.text)

# 10. FAQ Generator
with tabs[9]:
    st.header("Long-Tail FAQ Generator")
    st.write("Create LLM-friendly answers for specific questions")
    
    question = st.text_input("FAQ Question", placeholder="E.g., 'Can I integrate [Your Product] with Outlook and Google Calendar at the same time?'",key="your_tool32323")
    audience = st.text_input("Target Audience", placeholder="E.g., 'non-technical small business owners'",key="your_too232l")
    
    if st.button("Generate FAQ Answer"):
        with st.spinner('Creating optimized FAQ answer...'):
            prompt = f"""
            Generate an LLM-friendly answer for:

            ### Question ###
            {question}

            ### Audience ###
            {audience}

            ### Instructions ###
            - Start with <45-word direct answer
            - Include:
              - Step-by-step walkthrough (bullets/numbers)
              - Troubleshooting tips
              - "Why This Matters" context
            - Use markdown headers and plain language
            - Optimize for AI summarization
            """
            
            response = modelo_texto.generate_content(prompt)
            st.markdown(response.text)

# --- CSS Styling ---
st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 8px 12px;
        border-radius: 4px 4px 0 0;
    }
    .stTabs [aria-selected="true"] {
        background-color: #f0f2f6;
    }
    textarea {
        min-height: 100px !important;
    }
    [data-testid="stMarkdownContainer"] ul {
        padding-left: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

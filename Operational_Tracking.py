import streamlit as st
from datetime import date
import getpass

# Detecta tema (light/dark) via Streamlit (experimental)
def get_theme():
    theme = st.get_option("theme.base")
    return theme if theme else "light"

theme = get_theme()

# Cores
AZUL = "#1769aa"
CINZA_DARK = "#262730"  # cor padrão dos campos no tema dark do Streamlit
BRANCO = "#fff"

# Configuração da página
st.set_page_config(
    page_title="Operational Tracking",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "language" not in st.session_state:
    st.session_state.language = "PT"
if "status" not in st.session_state:
    st.session_state.status = "Ativo"

try:
    user_name = getpass.getuser()
except Exception:
    user_name = "Usuário"

TEXT = {
    "PT": {
        "system": "Operational Tracking",
        "description": "Ferramenta de acompanhamento operacional para monitoramento de status de pacotes, entregas e processos.",
        "welcome": "Bem-vindo",
        "instruction": "Selecione a DS e a data para iniciar",
        "date": "Data",
        "ds": "DS",
        "dispatch": "Gerar Dispatch",
        "language": "Idioma",
        "status": "Status"
    },
    "EN": {
        "system": "Operational Tracking",
        "description": "Operational tracking tool to monitor package, delivery, and process status.",
        "welcome": "Welcome",
        "instruction": "Select DS and date to start",
        "date": "Date",
        "ds": "DS",
        "dispatch": "Generate Dispatch",
        "language": "Language",
        "status": "Status"
    }
}
t = TEXT[st.session_state.language]

# CSS customizado
st.markdown(f"""
<style>
.header {{
    background-color: {AZUL};
    padding: 14px 30px;
    border-radius: 6px;
    display: flex;
    align-items: center;
    color: white;
    font-weight: 600;
    justify-content: space-between;
}}
.header-center {{
    flex: 1;
    text-align: center;
    font-size: 22px;
}}
.header-right {{
    display: flex;
    align-items: center;
    gap: 16px;
}}
/* Selectbox de idioma dentro da faixa azul */
div[data-baseweb="select"] {{
    background: transparent !important;
}}
/* Campo de instrução */
.sub-box {{
    background-color: {"#fff" if theme == 'dark' else AZUL};
    color: {"#222" if theme == 'dark' else "#fff"};
    padding: 14px;
    border-radius: 10px;
    text-align: center;
    margin-top: 30px;
    margin-bottom: 30px;
    font-weight: 600;
}}
/* Botão Gerar Dispatch */
.stButton>button {{
    background-color: {CINZA_DARK if theme == 'dark' else "#f3f4f6"} !important;
    color: #222 !important;
    border-radius: 8px !important;
    font-weight: 600;
    height: 48px;
    min-width: 120px;
    border: 1px solid #ccc !important;
}}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown(
    f"""
<div class="header">
  <div><b>Amazon Hub</b></div>
  <div class="header-center">{t['system']}</div>
  <div class="header-right">
      <span>{t['status']}: {st.session_state.status}</span>
      <div style="min-width:120px;">
          <form>
              <select onchange="window.location.search='?language='+this.value">
                  <option value="PT" {'selected' if st.session_state.language=='PT' else ''}>PT</option>
                  <option value="EN" {'selected' if st.session_state.language=='EN' else ''}>EN</option>
              </select>
          </form>
      </div>
  </div>
</div>
""", unsafe_allow_html=True
)

# Descrição e boas-vindas
st.markdown(f"<p style='text-align:center; margin-top:20px;'>{t['description']}</p>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align:center;'>{t['welcome']}, {user_name}</h3>", unsafe_allow_html=True)

# Campo instrução
st.markdown(f"<div class='sub-box'>{t['instruction']}</div>", unsafe_allow_html=True)

# Formulário para inputs + botão alinhado
with st.form(key="dispatch_form"):
    col_date, col_ds, col_btn = st.columns([3, 3, 2], gap="small")
    with col_date:
        selected_date = st.date_input(t["date"], date.today())
    with col_ds:
        selected_ds = st.selectbox(t["ds"], ["", "DSA1", "DSB2", "DSC3"])
    with col_btn:
        generate = st.form_submit_button(t["dispatch"])

# Resultado
if generate and selected_ds:
    st.success(f"Dispatch gerada para {selected_ds} em {selected_date}")

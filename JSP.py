import streamlit as st
import random
import time
from datetime import datetime
import base64
import os
from pathlib import Path

# --- FONCTION POUR CHARGER L'IMAGE ---
def load_image_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except:
        return None

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="★ Ton cadeau d'anniversaire ★",
    page_icon="🍂",
    layout="centered"
)

# --- INITIALISATION DE L'ÉTAT DU CADEAU ---
if 'ouvert' not in st.session_state:
    st.session_state.ouvert = False

# --- CHARGEMENT DU FOND ---
current_dir = os.path.dirname(__file__)
bg_img_path = os.path.join(current_dir, "fond.jpeg") 
bg_data = load_image_base64(bg_img_path)

# --- STYLE CSS GLOBAL ---
st.markdown("""
    <style>
    header, footer, .stDeployButton, #stDecoration {visibility: hidden;}

    /* Style général du texte */
    .stApp {
        color: #9D6B53; 
        font-family: 'Georgia', 'Times New Roman', serif;
    }

    /* Titres */
    h1, h2, h3 {
        color: #743014 !important;
        font-family: 'Georgia', serif;
        font-style: italic;
        letter-spacing: 1px;
    }

    /* --- STYLE DES ONGLETS (CORRIGÉ) --- */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        background-color: rgba(232, 209, 167, 0.8) !important; /* Fond beige/marron clair */
        border: 1px solid #84592B !important;
        padding: 10px;
        border-radius: 15px;
    }
    .stTabs [data-baseweb="tab"] {
        color: #743014 !important;
        font-family: 'Georgia', serif;
        font-weight: bold;
        background-color: transparent !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: #9D6B53 !important;
    }
    .stTabs [aria-selected="true"] {
        border-bottom: 2px solid #743014 !important;
    }

    /* --- BOUTONS --- */
    .stButton>button {
        width: 100%;
        background-color: #E8D1A7 !important; 
        color: #743014 !important;
        border-radius: 12px;
        font-family: 'Georgia', serif;
        font-weight: bold;
        border: 1px solid #84592B;           
        transition: 0.4s ease;
    }
    
    .stButton>button:hover {
        background-color: #9D9167 !important; 
        color: #E8D1A7 !important;
        transform: translateY(-2px);
    }

    /* Boîte de message */
    .message-box {
        padding: 30px;
        border: 1px solid #84592B;
        background-color: rgba(255, 252, 240, 0.95); 
        color: #743014;
        font-size: 1.2rem;
        font-style: italic;
        text-align: center;
        margin: 20px 0;
        border-radius: 5px;
        box-shadow: 8px 8px 0px rgba(157, 145, 103, 0.2); 
    }

    /* Animation du cadeau */
    .gift-container {
        text-align: center;
        margin-top: 100px;
    }
    .gift-box {
        font-size: 100px;
        animation: wiggle 2s infinite;
        cursor: pointer;
        margin-bottom: 20px;
    }

    @keyframes wiggle {
        0% { transform: rotate(0deg); }
        80% { transform: rotate(0deg); }
        85% { transform: rotate(7deg); }
        90% { transform: rotate(-7deg); }
        95% { transform: rotate(7deg); }
        100% { transform: rotate(0deg); }
    }

    /* Animation des feuilles */
    @keyframes fall {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    .leaf {
        position: fixed;
        top: -10%;
        user-select: none;
        pointer-events: none;
        z-index: 9999;
        animation: fall linear forwards;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE D'AFFICHAGE ---

if not st.session_state.ouvert:
    # --- ÉCRAN CADEAU FERMÉ ---
    st.markdown("""
        <div class="gift-container">
            <div class="gift-box">🎁</div>
            <h2 style="text-align:center;">Tu as reçu un paquet...</h2>
            <p style="text-align:center; font-style: italic;">Appuie sur le bouton pour l'ouvrir</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Déballer le cadeau !"):
        st.session_state.ouvert = True
        st.balloons()
        time.sleep(0.5)
        st.rerun()

else:
    # --- LE SITE UNE FOIS OUVERT ---
    
    if bg_data:
        st.markdown(f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpeg;base64,{bg_data}");
                background-size: 300px; 
                background-repeat: repeat;
                background-attachment: fixed;
            }}
            </style>
        """, unsafe_allow_html=True)

    def falling_leaves():
        leaf_icons = ["🍂", "🍁", "🍃"]
        html_leaves = ""
        for _ in range(15):
            left = random.randint(0, 95)
            duration = random.randint(5, 10)
            delay = random.uniform(0, 5)
            icon = random.choice(leaf_icons)
            size = random.randint(20, 40)
            html_leaves += f'<div class="leaf" style="left:{left}%; font-size:{size}px; animation-duration:{duration}s; animation-delay:{delay}s;">{icon}</div>'
        st.markdown(html_leaves, unsafe_allow_html=True)

    playlist = {
        "The Smiths - Back to the old house": {"audio": "backto.mp3", "image": "backto.jpeg"},
        "ABBA - Dancing Queen": {"audio": "queen.mp3", "image": "queen.jpg"},
        "She & Him - I thought I saw your face today": {"audio": "ithought.mp3", "image": "ithought.jpeg"},
        "TV Girl - Better in the dark": {"audio": "dark.mp3", "image": "dark.jpeg"},
        "girl in red - Better in the dark": {"audio": "october.mp3", "image": "october.png"},
        "The Police - Every breath you take": {"audio": "breath.mp3", "image": "breath.jpeg"},
    }

    st.markdown("<h2 style='text-align:center; color:#743014; text-shadow: 1px 1px 2px #E8D1A7;'>★ Ton cadeau d'anniversaire ★</h2>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["✨ Les réfs", "🎵 Les sons", "✉️ La lettre"])

    with tab1:
        st.markdown("<h3 style='text-align:center; color:#9D6B53;'>Appuie sur le bouton pour faire apparaître une réf...</h3>", unsafe_allow_html=True)
        if st.button('Les rèfs!!!'):
            falling_leaves()
            messages = ["On est pas au marché ici !"]
            st.markdown(f'<div class="message-box">"{random.choice(messages)}"</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown("### 🎧 Les Sons qui me font penser à toi")
        if "musique_index" not in st.session_state:
            st.session_state.musique_index = list(playlist.keys())[0]

        if st.button("🎲 Lecture Aléatoire"):
            st.session_state.musique_index = random.choice(list(playlist.keys()))

        choix = st.selectbox("Choisis ton morceau :", list(playlist.keys()), index=list(playlist.keys()).index(st.session_state.musique_index))
        st.divider()
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(playlist[choix]["image"], width=150)
        with col2:
            st.markdown(f"<h4 style='margin-top:0; color:#9D6B53;'>{choix}</h4>", unsafe_allow_html=True)
            st.audio(playlist[choix]["audio"])

    with tab3:
        st.markdown(f"""
        <div class="message-box" style="text-align: left; font-style: normal; line-height: 1.6;">
        Sana,<br><br>
        Joyeux Anniversaire ! J'ai créé ce site pour toi, pour ton anniversaire, mais tu pourras (j'espère) le garder toute ta vie. J'ai essayé de le créer à ton image. Il se peut que je le modifie dans le futur si je trouve le temps. Bref Bon anniversaire !!!!
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
        <div style='text-align: center; margin-top: 50px; opacity: 0.8;'>
            <span style='background-color: rgba(232, 209, 167, 0.7); padding: 10px 20px; border-radius: 5px; color: #9D6B53; font-size: 0.85rem; font-family: serif; border: 1px solid #84592B;'>
                Manuscrit avec ❤️ par Adam | {datetime.now().strftime('%d/%m/%Y')}
            </span>
        </div>
    """, unsafe_allow_html=True)

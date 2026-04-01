import streamlit as st
import random
import time
from datetime import datetime
import base64
import os
import json
from pathlib import Path

# --- FONCTIONS UTILITAIRES ---

def load_image_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except:
        return None

def charger_messages_permanents():
    """Charge les messages depuis le fichier texte s'il existe."""
    if not os.path.exists("messages.txt"):
        return []
    try:
        with open("messages.txt", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def sauvegarder_nouveau_message(nouveau_mot):
    """Ajoute un message au fichier texte."""
    messages = charger_messages_permanents()
    messages.insert(0, nouveau_mot)
    with open("messages.txt", "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="★ Ton cadeau d'anniversaire ★",
    page_icon="🍂",
    layout="centered"
)

# --- INITIALISATION DES VARIABLES ---
if 'ouvert' not in st.session_state:
    st.session_state.ouvert = False

# --- CHARGEMENT DU FOND ---
current_dir = os.path.dirname(__file__)
bg_img_path = os.path.join(current_dir, "Fond3.jpeg") 
bg_data = load_image_base64(bg_img_path)

# --- STYLE CSS GLOBAL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Beau+Rivage&display=swap');

    header, footer, .stDeployButton, #stDecoration {visibility: hidden;}

    .stApp {
        color: #9D6B53; 
        font-family: 'Georgia', serif;
    }

    h1, h2, h3 {
        color: #E4A65F !important;
        font-family: 'Palatino', serif;
        font-style: italic;
        letter-spacing: 1px;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        background-color: rgba(232, 209, 167, 0.9) !important; 
        border: 1px solid #84592B !important;
        padding: 10px;
        border-radius: 15px;
    }
    .stTabs [data-baseweb="tab"] {
        color: #743014 !important;
        font-family: 'Georgia', serif;
        font-weight: bold;
    }

    .message-box {
        padding: 25px;
        border: 1px solid #84592B;
        background-color: rgba(255, 252, 240, 0.98); 
        color: #743014;
        font-family: 'Beau Rivage', cursive !important;
        font-size: 2.2rem !important;
        line-height: 1.2;
        text-align: center;
        margin: 15px 0;
        border-radius: 10px;
        box-shadow: 4px 4px 15px rgba(0,0,0,0.05);
    }

    .signature {
        font-family: 'Georgia', serif;
        font-size: 0.8rem;
        color: #84592B;
        text-align: right;
        margin-top: -10px;
        font-style: italic;
        margin-bottom: 20px;
    }

    .stButton>button {
        width: 100%;
        background-color: #E8D1A7 !important; 
        color: #743014 !important;
        border-radius: 12px;
        font-weight: bold;
        border: 1px solid #84592B;           
    }

    .gift-box { font-size: 100px; animation: wiggle 2s infinite; text-align: center; margin-top: 50px; }
    @keyframes wiggle { 0%, 80% { transform: rotate(0deg); } 85% { transform: rotate(7deg); } 90% { transform: rotate(-7deg); } 95% { transform: rotate(7deg); } 100% { transform: rotate(0deg); } }
    
    @keyframes fall { 0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; } 100% { transform: translateY(100vh) rotate(360deg); opacity: 0; } }
    .leaf { position: fixed; top: -10%; z-index: 9999; animation: fall linear forwards; pointer-events: none; }
    </style>
    """, unsafe_allow_html=True)

def falling_leaves():
    leaf_icons = ["🍂", "🍁", "🍃"]
    html_leaves = ""
    for _ in range(15):
        left = random.randint(0, 95)
        duration = random.randint(5, 10)
        icon = random.choice(leaf_icons)
        size = random.randint(20, 40)
        html_leaves += f'<div class="leaf" style="left:{left}%; font-size:{size}px; animation-duration:{duration}s;">{icon}</div>'
    st.markdown(html_leaves, unsafe_allow_html=True)

# --- LOGIQUE ---

if not st.session_state.ouvert:
    st.markdown('<div class="gift-box">🎁</div>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#743014;'>Un petit quelque chose pour toi...</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Déballer le cadeau !"):
            st.session_state.ouvert = True
            st.balloons()
            time.sleep(0.5)
            st.rerun()
else:
    if bg_data:
        st.markdown(f'<style>.stApp {{ background-image: url("data:image/jpeg;base64,{bg_data}"); background-size: 300px; background-repeat: repeat; background-attachment: fixed; }}</style>', unsafe_allow_html=True)

    st.markdown("<h2 style='text-align:center; color:#743014; text-shadow: 1px 1px 2px #E8D1A7;'>★ Ton cadeau d'anniversaire ★</h2>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["✨ Les réfs", "🎵 Les sons", "📜 Livre d'Or"])

    with tab1:
        st.markdown("<h3 style='text-align:center; color:#9D6B53;'>Une petite réf ?</h3>", unsafe_allow_html=True)
        if st.button('Faire apparaître une réf'):
            falling_leaves()
            messages = ["On est pas au marché ici !",
                       "Oy boro vaya"]
            st.markdown(f'<div class="message-box">"{random.choice(messages)}"</div>', unsafe_allow_html=True)

    with tab2:
        playlist = {
            "The Smiths - Back to the old house": {"audio": os.path.join(current_dir, "backto.mp3"), "image": os.path.join(current_dir, "backto.jpeg")},
            "ABBA - Dancing Queen": {"audio": os.path.join(current_dir, "queen.mp3"), "image": os.path.join(current_dir, "queen.jpg")},
            "She & Him - I thought I saw your face today": {"audio": os.path.join(current_dir, "ithought.mp3"), "image": os.path.join(current_dir, "ithought.jpeg")},
            "TV Girl - Better in the dark": {"audio": os.path.join(current_dir, "dark.mp3"), "image": os.path.join(current_dir, "dark.jpeg")},
            "girl in red - we fell in love in october": {"audio": os.path.join(current_dir, "october.mp3"), "image": os.path.join(current_dir, "october.png")},
            "The Police - Every breath you take": {"audio": os.path.join(current_dir, "breath.mp3"), "image": os.path.join(current_dir, "breath.jpeg")},
        }
        if "musique_index" not in st.session_state: st.session_state.musique_index = list(playlist.keys())[0]
        if st.button("🎲 Aléatoire"): st.session_state.musique_index = random.choice(list(playlist.keys()))
        choix = st.selectbox("Choisis ton morceau :", list(playlist.keys()), index=list(playlist.keys()).index(st.session_state.musique_index))
        col1, col2 = st.columns([1, 2])
        with col1: st.image(playlist[choix]["image"], width=150)
        with col2:
            st.markdown(f"<h4 style='color:#9D6B53;'>{choix}</h4>", unsafe_allow_html=True)
            st.audio(playlist[choix]["audio"])

    with tab3:
        st.markdown("### 🖋️ Laisse un petit mot dans le Livre d'Or")
        
        # On utilise un formulaire pour que l'interface soit plus propre
        with st.form("form_livre", clear_on_submit=True):
            nom = st.text_input("Ton nom ou surnom :", "")
            message = st.text_area("écris ton message :")
            submit = st.form_submit_button("Poster dans le Livre d'Or")
            
            if submit:
                if message.strip():
                    nouveau_mot = {
                        "nom": nom if nom else "Anonyme",
                        "message": message,
                        "date": datetime.now().strftime("%d/%m/%Y à %H:%M")
                    }
                    sauvegarder_nouveau_message(nouveau_mot)
                    falling_leaves()
                    st.success("Message ajouté ! ✨")
                    time.sleep(1)
                    st.rerun()

        st.divider()
        
        # On charge les messages depuis le fichier permanent
        messages_permanents = charger_messages_permanents()
        
        if not messages_permanents:
            st.info("Le livre d'or est vide pour le moment. Sois la première à écrire !")
        else:
            for item in messages_permanents:
                st.markdown(f"""
                    <div class="message-box">
                        {item['message']}
                    </div>
                    <div class="signature">Par {item['nom']}, le {item['date']}</div>
                """, unsafe_allow_html=True)

    # PIED DE PAGE
    st.markdown(f"<div style='text-align: center; margin-top: 50px;'><span style='background-color: rgba(232, 209, 167, 0.7); padding: 10px 20px; border-radius: 5px; color: #9D6B53; font-size: 0.85rem; border: 1px solid #84592B;'>Manuscrit avec ❤️ par Adam | {datetime.now().strftime('%d/%m/%Y')}</span></div>", unsafe_allow_html=True)

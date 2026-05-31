import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Mix Assistant", layout="wide")
st.title("🎧 Asistente de Transiciones Inteligente")

# 1. Ingreso de la Playlist
st.markdown("### 1. Carga tu maleta de discos")
url_playlist = st.text_input("🔗 Pega el enlace de la Playlist pública de Spotify:")

if url_playlist:
    # Lógica de validación rápida de la URL
    if "open.spotify.com/playlist/" in url_playlist:
        st.success("¡Playlist detectada! Analizando BPMs y Tonalidades...")
        
        # ------------------------------------------------------------------
        # Aquí irá tu código Spotipy en el futuro. 
        # Extraerás el ID así: playlist_id = url_playlist.split("/")[-1].split("?")[0]
        # Y armarás un DataFrame real.
        # ------------------------------------------------------------------
        
        # Simulamos que el algoritmo ya analizó la playlist
        if "playlist_df" not in st.session_state:
            st.session_state.playlist_df = pd.DataFrame({
                "Track": ["Canción A", "Canción B", "Canción C", "Canción D"],
                "BPM": [95, 105, 106, 98],
                "Camelot": ["8A", "9A", "9B", "7A"]
            })
            
        st.dataframe(st.session_state.playlist_df, use_container_width=True)
        st.divider()
        
        # 2. Iniciar el Motor de Mezcla
        st.markdown("### 2. Inicia tu Set")
        track_inicial = st.selectbox("Selecciona la pista de inicio:", st.session_state.playlist_df["Track"].tolist())
        
        if st.button("Buscar Transiciones"):
            st.session_state.cancion_actual = track_inicial
            # Aquí se gatillaría la lógica iterativa que vimos en el mensaje anterior
            st.info(f"Calculando las mejores salidas para {track_inicial}...")
            
    else:
        st.error("Por favor, ingresa un enlace válido de una playlist de Spotify.")

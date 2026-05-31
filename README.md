# 🎧 ASSISMIX-SHOW

¡Bienvenido a **ASSISMIX-SHOW**! Un asistente algorítmico diseñado para DJs que buscan llevar sus transiciones al siguiente nivel. 

Esta aplicación web extrae los datos de cualquier playlist pública de Spotify, analiza el tempo (BPM) y la tonalidad de cada pista, y utiliza la lógica de la **Rueda de Camelot** para recomendar las mejores transiciones armónicas en tiempo real. 

Nacido de la fusión entre la Ingeniería Empresarial y de Sistemas y la pasión por mezclar en consola (desde la salsa más brava hasta la cumbia peruana), este proyecto busca automatizar el análisis musical para que el DJ solo se concentre en el arte de mezclar.

## ✨ Características Principales

- **Análisis de Playlists en Bloque:** Ingresa la URL de cualquier playlist pública de Spotify y obtén la metadata de todas las canciones en segundos.
- **Traducción Armónica (Camelot Wheel):** Convierte automáticamente el `Key` y `Mode` estándar de la API de Spotify al sistema Camelot (ej. 8A, 9B), el estándar de la industria DJ.
- **Motor de Recomendación Inteligente:** Al seleccionar la pista que está sonando, el algoritmo filtra y sugiere las siguientes canciones basándose en un rango de BPM compatible ($\pm$ 4%) y reglas de mezcla armónica.
- **Interfaz Interactiva:** Construido con Streamlit para una experiencia de usuario fluida y sin recargas en el navegador.

## 🛠️ Stack Tecnológico

- **Python 3.x**
- **Streamlit** (Frontend y lógica de interfaz)
- **Pandas** (Estructuración y manipulación del catálogo)
- **Spotipy** (Integración con la API de Spotify)

## 🚀 Instalación y Uso Local

Sigue estos pasos para correr ASSISMIX-SHOW en tu máquina:

**1. Clona el repositorio:**
```bash
git clone [https://github.com/TU_USUARIO/ASSISMIX-SHOW.git](https://github.com/TU_USUARIO/ASSISMIX-SHOW.git)
cd ASSISMIX-SHOW

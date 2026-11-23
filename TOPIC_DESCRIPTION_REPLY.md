Hi Dr. Humera,

Sorry about the text getting cut off in the application form. Here is the concise summary in 3 paragraphs:

**1. What We Will Do:**  
We are developing **SoundScope**, an AI-driven platform that jointly analyzes song audio and lyrics to provide automated, explainable feedback for music creators. While existing tools examine sound or lyrics in isolation, our platform bridges both worlds by evaluating audio mix balance, tempo, genre, emotional mood, and lyrical themes to show artists how well their music and message align. This will be conducted as a team project with Apoorv Pillai (Matr. 85099328).

**2. Which Data We Will Use:**  
For audio data, we will use the benchmark **Free Music Archive (FMA)** and **GTZAN** datasets, which provide thousands of labeled tracks across diverse genres. For lyrical data, we will use the **Genius / Spotify Lyrics dataset** along with **OpenAI Whisper** to automatically transcribe lyrics directly from user-uploaded audio files (MP3/WAV).

**3. What Analysis We Will Do:**  
We will perform dual-branch analysis using Digital Signal Processing (DSP) and Natural Language Processing (NLP). On the audio branch, we will extract tempo (BPM), frequency balance, and MFCCs using Librosa, and train classification models (XGBoost/CNN) to predict genre and mood alongside UMAP clustering. On the lyric branch, we will analyze emotional sentiment arcs, rhyme structure, and topics. Finally, an LLM agent will synthesize both branches into clear, actionable production suggestions for the artist.

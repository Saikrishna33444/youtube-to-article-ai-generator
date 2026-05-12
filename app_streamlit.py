import streamlit as st
from app import extract_video_id, get_transcript, generate_article

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="YouTube to Article AI Generator",
    page_icon="🎥",
    layout="centered"
)

# ==============================
# UI
# ==============================
st.title("🎥 YouTube to Article AI Generator")
st.write("Convert YouTube videos into structured articles using AI 🚀")

# ==============================
# INPUT
# ==============================
url = st.text_input("🔗 Enter YouTube URL")

# ==============================
# BUTTON
# ==============================
if st.button("Generate Article"):

    # Empty input
    if not url:
        st.warning("⚠️ Please enter a YouTube URL")

    else:
        video_id = extract_video_id(url)

        # Invalid URL
        if not video_id:
            st.error("❌ Invalid YouTube URL")
        else:
            # ==============================
            # FETCH TRANSCRIPT
            # ==============================
            with st.spinner("📥 Fetching transcript..."):
                transcript, lang = get_transcript(video_id)

            if transcript is None:
                st.error("❌ Failed to fetch transcript.\n\n👉 Try another video or change network.")
            else:
                st.success(f"✅ Transcript fetched (Language: {lang})")

                # Reduce size (avoid quota issues)
                transcript = transcript[:3000]

                # ==============================
                # GENERATE ARTICLE
                # ==============================
                with st.spinner("🤖 Generating article using AI..."):
                    article = generate_article(transcript, lang)

                if article is None:
                    st.error("❌ Failed to generate article")
                    st.warning("👉 Possible reasons:\n- API quota exceeded\n- Invalid API key")

                    # Fallback
                    st.info("⚠️ Showing sample output instead")
                    article = "Sample generated article (API quota issue). Please check your API key or billing."

                else:
                    st.success("🎉 Article Generated Successfully!")

                # ==============================
                # OUTPUT
                # ==============================
                st.subheader("📄 Generated Article")
                st.write(article)

                # ==============================
                # DOWNLOAD OPTIONS
                # ==============================
                col1, col2 = st.columns(2)

                # TXT download
                with col1:
                    st.download_button(
                        label="📥 Download as TXT",
                        data=article,
                        file_name="article.txt",
                        mime="text/plain"
                    )

                # HTML download (FIXED VERSION)
                with col2:
                    formatted_article = article.replace("\n", "<br>")

                    html_content = f"""
                    <html>
                    <head>
                        <title>Generated Article</title>
                        <style>
                            body {{
                                font-family: Arial;
                                margin: 40px auto;
                                max-width: 800px;
                                line-height: 1.6;
                                background-color: #0e1117;
                                color: white;
                            }}
                            h1, h2, h3 {{
                                color: #00ffcc;
                            }}
                        </style>
                    </head>
                    <body>
                        <h1>Generated Article</h1>
                        <p>{formatted_article}</p>
                    </body>
                    </html>
                    """

                    st.download_button(
                        label="🌐 Download as HTML Website",
                        data=html_content,
                        file_name="website.html",
                        mime="text/html"
                    )

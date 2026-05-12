# ============================================
# YouTube → Article → PDF → Website Generator
# FINAL CLEAN VERSION
# ============================================

import html
import os
from urllib.parse import parse_qs, urlparse

from google import genai
from fpdf import FPDF
from youtube_transcript_api import YouTubeTranscriptApi


# 🔐 API KEY (set in environment)
API_KEY = "AIzaSyAV8FkKOhv9PNt6MxkLEknxm27zULaw9UY"
GENAI_CLIENT = genai.Client(api_key=API_KEY)


# ============================================
# Extract Video ID
# ============================================
def extract_video_id(url):
    parsed = urlparse(url.strip())

    if parsed.netloc in {"youtu.be", "www.youtu.be"}:
        return parsed.path.strip("/") or None

    query_video_id = parse_qs(parsed.query).get("v", [None])[0]
    if query_video_id:
        return query_video_id

    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) >= 2 and parts[0] in {"shorts", "embed"}:
        return parts[1]

    return None


# ============================================
# Get Transcript (FIXED)
# ============================================
def get_transcript(video_id):
    try:
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)

        # Try English → Telugu → Any
        try:
            transcript = transcript_list.find_transcript(["en"])
        except:
            try:
                transcript = transcript_list.find_transcript(["te"])
            except:
                transcript = next(iter(transcript_list))

        # Translate if needed
        if transcript.language_code != "en" and transcript.is_translatable:
            try:
                transcript = transcript.translate("en")
            except:
                pass

        data = transcript.fetch()

        text = " ".join(item.text for item in data)

        print(f"Using transcript language: {transcript.language_code}")
        return text, transcript.language_code

    except Exception as e:
        print("❌ Error fetching transcript:", e)
        return None, None


# ============================================
# Generate Article (FIXED MODEL)
# ============================================
def generate_article(text, source_language):
    try:
        prompt = f"""
Convert the following YouTube transcript into a professional blog article in English.

Requirements:
- Translate if needed
- Add Title, Introduction, Sections, Bullet points, Conclusion
- Make it clean and readable

Transcript language: {source_language}

{text}
"""

        response = GENAI_CLIENT.models.generate_content(
            model="gemini-2.0-flash",   # ✅ correct model
            contents=prompt,
        )

        return response.text if hasattr(response, "text") else str(response)

    except Exception as e:
        print("❌ Error generating article:", e)
        return None


# ============================================
# Create PDF
# ============================================
def create_pdf(content):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)

        for line in content.split("\n"):
            safe_line = line.encode("latin-1", "replace").decode("latin-1")
            pdf.multi_cell(0, 10, safe_line)

        pdf.output("output.pdf")
        print("✅ PDF generated")

    except Exception as e:
        print("❌ PDF error:", e)


# ============================================
# Create HTML
# ============================================
def create_html(content):
    try:
        formatted = html.escape(content).replace("\n", "<br>")

        html_content = f"""
        <html>
        <head>
            <title>Generated Article</title>
            <style>
                body {{
                    font-family: Arial;
                    margin: 40px auto;
                    max-width: 900px;
                    line-height: 1.6;
                }}
            </style>
        </head>
        <body>
            {formatted}
        </body>
        </html>
        """

        with open("output.html", "w", encoding="utf-8") as f:
            f.write(html_content)

        print("✅ HTML generated")

    except Exception as e:
        print("❌ HTML error:", e)


# ============================================
# MAIN
# ============================================
if __name__ == "__main__":
    url = input("🔗 Enter YouTube URL: ")

    video_id = extract_video_id(url)

    if not video_id:
        print("❌ Invalid URL")
        exit()

    print("📥 Fetching transcript...")
    transcript, lang = get_transcript(video_id)

    if transcript is None:
        print("❌ Cannot proceed")
        exit()

    print("🤖 Generating article...")
    article = generate_article(transcript, lang)

    if article is None:
        print("❌ Failed to generate article")
        exit()

    print("📄 Creating PDF...")
    create_pdf(article)

    print("🌐 Creating HTML...")
    create_html(article)

    print("\n🎉 DONE!")
    print("➡ output.pdf")
    print("➡ output.html")

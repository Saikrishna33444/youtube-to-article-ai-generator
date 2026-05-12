# youtube-to-article-ai-generator
YouTube to Article AI Generator
📌 Overview
The YouTube to Article AI Generator is an end-to-end Generative AI application that transforms YouTube video content into structured, high-quality written articles through an interactive web interface.

This project demonstrates the practical use of Large Language Models (LLMs) for content transformation, combining transcript extraction, intelligent summarization, and user-friendly UI deployment.

🎯 Objective
The primary objective of this project is to:

Convert video-based content into readable blog-style articles
Build a deployable AI-powered web application
Demonstrate real-world usage of Generative AI with APIs
Handle real-world challenges like API limits and missing data
✨ Key Features
🔗 YouTube Transcript Extraction
Automatically fetches transcripts from YouTube videos using API-based extraction.

🧠 AI-Powered Article Generation
Transforms raw transcripts into structured, professional articles using Gemini AI.

🖥️ Interactive Web Application
Built using Streamlit for real-time user interaction.

📥 Export Options
Users can download generated content as:

Text file (.txt)
HTML webpage (.html)
⚠️ Error Handling & Fallback System
Handles:

Invalid YouTube URLs
Missing transcripts
API quota limitations
Provides fallback output to ensure smooth user experience.

🛠️ Tech Stack
Backend & AI
Python
Google Gemini API (google.genai)
YouTube Transcript API
Frontend
Streamlit
Utilities
FPDF (optional)
dotenv (environment variable management)
🏗️ Architecture Overview
The project follows a modular pipeline:

Input Layer
Accepts YouTube video URL from user

Data Extraction
Fetches transcript using YouTube Transcript API

Processing Layer
Preprocesses transcript and prepares input for AI

AI Generation
Gemini LLM converts transcript into structured article

Output Layer
Displays article in UI and allows download as TXT/HTML

⚙️ Installation & Setup
1. Install Dependencies
pip install -r requirements.txt
2. Configure Environment Variables
Create a .env file:

GEMINI_API_KEY=your_api_key_here
⚠️ Do NOT expose your API key publicly.

3. Run the Application
streamlit run app_streamlit.py
📄 Output
After execution, users can:

View generated article in browser

Download as:

article.txt
website.html
⚠️ Important Note on API Usage
This project uses Google Gemini API (Free Tier).

Free tier limitations may include:

Limited requests per day
Token usage restrictions
Temporary rate limits
Due to these constraints, the application includes fallback handling when API quota is exceeded.

🚀 Future Enhancements
PDF download support
Advanced UI/UX improvements
Multiple article styles (short / detailed)
Batch video processing
Cloud deployment enhancements
🧠 Learning Outcomes
This project demonstrates:

End-to-end Generative AI pipeline development
Prompt engineering for structured outputs
Integration of LLMs with real-world data
Building deployable AI applications
Handling API limitations in production
👨‍💻 Author
Lokesh Naidu Gen-AI Intern | Data Science Enthusiast

GitHub: https://github.com/lokesh985003
LinkedIn: https://www.linkedin.com/in/orugantilokeshnaidu/
⭐ Support
If you found this project useful, consider giving it a ⭐ on GitHub.

📬 Contact
Feel free to connect for collaboration, feedback, or discussions on AI and development.

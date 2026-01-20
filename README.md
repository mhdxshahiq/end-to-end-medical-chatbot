# 🏥 MediFlow AI: Medical HealthBot

MediFlow AI is an end-to-end RAG (Retrieval-Augmented Generation) medical assistant. It leverages Pinecone for high-performance vector search and Google Gemini for generative intelligence. The application features a bold, architectural UI design optimized for performance and professional medical branding.

---

## 🛠️ Tech Stack
* **Generative AI:** Google Gemini API (`gemini-1.5-flash`)
* **Orchestration:** LangChain (LCEL)
* **Vector Database:** Pinecone
* **Backend:** Flask (Python 3.10+)
* **Frontend:** HTML5, CSS3 (Flat/Bold Neo-Brutalist Design), jQuery
* **Deployment:** AWS (Elastic Beanstalk / EC2) via CI/CD pipelines

---

## 📦 Deployment Architecture

The project is structured to integrate seamlessly with **AWS CodePipeline** or **GitHub Actions**.



1.  **Source:** Developer pushes code to the `main` branch on GitHub.
2.  **Build:** AWS CodeBuild (or GitHub Actions) initializes the environment and installs dependencies from `requirements.txt`.
3.  **Deploy:** The application is deployed to an AWS environment with environment variables pre-configured.

---

## 🔑 Environment Variables

To run this project, you must add the following variables to your AWS Environment Properties or your local `.env` file:

env
GOOGLE_API_KEY=your_gemini_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_API_ENV=your_pinecone_environment

---

## 📂 Project Structure
Plaintext

├── .github/workflows/   # CI/CD pipeline definitions
├── src/
│   ├── templates/      # Refined index.html (UI)
│   ├── static/         # Custom style.css (Bold/Flat design)
│   ├── helper.py       # Embeddings and data processing
│   └── prompt.py       # Anti-hijacking system prompt
├── app.py              # Flask server & RAG chain logic
├── requirements.txt    # Project dependencies
└── README.md           # Documentation

---

## 🛡️ Security & Performance Optimization
Prompt Hijacking Protection: The system prompt includes a "Security Guard" layer to ignore malicious instructions (e.g., "ignore all previous instructions").

Rate Limit Handling: The backend is configured to catch 429 RESOURCE_EXHAUSTED errors gracefully, ensuring the app remains stable during traffic spikes.

Quota Management: The retriever is set to k=1 to minimize token consumption and stay within Gemini's Free Tier limits (Requests Per Minute).

---

## 🚀 Getting Started
Local Setup
Clone the repository:
---
Bash
git clone [https://github.com/yourusername/medical-chatbot.git](https://github.com/yourusername/medical-chatbot.git)
cd medical-chatbot
Install requirements:
---
Bash
pip install -r requirements.txt
Run the application:
---
Bash
python app.py

## AWS CI/CD Deployment
Connect your GitHub repository to AWS CodePipeline.
Configure AWS CodeBuild to use the requirements.txt for the build stage.
Set your API keys in the AWS Elastic Beanstalk Configuration > Software section.
Push code to main to trigger an automatic build and deployment.
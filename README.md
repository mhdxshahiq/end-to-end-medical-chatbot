# 🏥 MediFlow AI – Medical HealthBot

MediFlow AI is an end-to-end **Retrieval-Augmented Generation (RAG)** medical assistant designed to deliver accurate, context-aware medical information. It combines **high-performance vector search** using Pinecone with **Google Gemini** for generative intelligence, wrapped in a clean, bold, and professional medical-grade UI.

The system is built with scalability, security, and deployment readiness in mind, making it suitable for real-world production environments.

---

## 🧠 Key Features

* **RAG-powered Medical Assistant** – Retrieves relevant medical context before generating responses
* **Google Gemini Integration** – Uses `gemini-1.5-flash` for fast and cost-efficient inference
* **Pinecone Vector Search** – Low-latency, high-accuracy semantic retrieval
* **Prompt Injection Protection** – Built-in system-level security guard
* **Production-Ready Architecture** – CI/CD enabled with AWS deployment support
* **Professional Medical UI** – Flat, bold, neo-brutalist design optimized for performance

---

## 🛠️ Tech Stack

* **Generative AI:** Google Gemini API (`gemini-1.5-flash`)
* **Orchestration:** LangChain (LCEL)
* **Vector Database:** Pinecone
* **Backend:** Flask (Python 3.10+)
* **Frontend:** HTML5, CSS3 (Bold / Flat Neo-Brutalist UI), jQuery
* **Deployment:** AWS (Elastic Beanstalk / EC2) with CI/CD

---

## 🏗️ Deployment Architecture

MediFlow AI is structured to integrate seamlessly with **AWS CodePipeline** or **GitHub Actions**.

**Deployment Flow:**

1. **Source** – Developer pushes code to the `main` branch on GitHub
2. **Build** – AWS CodeBuild (or GitHub Actions) installs dependencies from `requirements.txt`
3. **Deploy** – Application is deployed to AWS with pre-configured environment variables

---

## 🔑 Environment Variables

Configure the following environment variables either in your local `.env` file or in **AWS Elastic Beanstalk → Configuration → Software**:

```
GOOGLE_API_KEY=your_gemini_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_API_ENV=your_pinecone_environment
```

---

## 📂 Project Structure

```
├── .github/workflows/     # CI/CD pipeline definitions
├── src/
│   ├── templates/        # Refined index.html (UI)
│   ├── static/           # Custom style.css (Bold / Flat design)
│   ├── helper.py         # Embeddings & data processing
│   └── prompt.py         # System prompt & anti-hijacking logic
├── app.py                # Flask server & RAG chain logic
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🛡️ Security & Performance Optimizations

* **Prompt Hijacking Protection**
  A dedicated system-level "Security Guard" prompt prevents instruction overrides such as *"ignore previous instructions"*.

* **Rate Limit Handling**
  Graceful handling of `429 RESOURCE_EXHAUSTED` errors ensures application stability during traffic spikes.

* **Quota Optimization**
  Retriever is configured with `k = 1` to minimize token usage and remain within Gemini Free Tier RPM limits.

---

## 🚀 Getting Started

### Local Setup

Clone the repository:

```bash
git clone https://github.com/yourusername/medical-chatbot.git
cd medical-chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

The application will be available at:

```
http://localhost:5000
```

---

## ☁️ AWS CI/CD Deployment

1. Connect your GitHub repository to **AWS CodePipeline**
2. Configure **AWS CodeBuild** to install dependencies from `requirements.txt`
3. Set environment variables in **Elastic Beanstalk → Configuration → Software**
4. Push code to the `main` branch to trigger automatic build and deployment

---

## 📌 Notes

* Designed to stay within **Gemini Free Tier** limits
* Optimized for **low latency and high reliability**
* Easily extensible for EHR integration, medical PDFs, or custom datasets

---

## 📄 License

This project is intended for educational and research purposes. Ensure compliance with medical data regulations before using in production healthcare

# 📄 PDF Summarizer

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Flask](https://img.shields.io/badge/Flask-Backend-red) ![React](https://img.shields.io/badge/React-Frontend-blue) ![GeminiAI](https://img.shields.io/badge/GeminiAI-Powered-green)

A simple **PDF summarization tool** that extracts and summarizes content using **Google's Gemini AI**. Designed to assist with **academic exam preparation** by providing concise and clear summaries of uploaded PDFs.

## 🚀 Features
- 📂 Upload and summarize PDFs
- 🤖 Uses **Google's Gemini AI** for intelligent summarization
- 📝 Provides **detailed and structured summaries**
- 📲 **Share summaries via WhatsApp**

## 📑 Table of Contents
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Endpoint](#-api-endpoint)
- [Demo](#-demo)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

## 🛠 Tech Stack
- **Frontend:** React
- **Backend:** Flask (Python)
- **AI Model:** Gemini AI via LangChain
- **PDF Processing:** PyPDFLoader

## ⚙️ Installation
### Prerequisites
- Node.js & npm
- Python 3
- Flask
- Google Gemini API Key

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your Google API key:
   ```bash
   export GOOGLE_API_KEY='your_google_api_key'
   ```
4. Run the Flask server:
   ```bash
   python app.py
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the React app:
   ```bash
   npm start
   ```

## 🎯 Usage
1. 📂 Upload a **PDF file**.
2. 🔍 Click **"Summarize PDF."**
3. 📝 View the **generated summary.**
4. 📲 **Share the summary via WhatsApp.**

## 🌐 API Endpoint
### PDF Summarization
```bash
POST /summarize
```
#### Example Usage
```bash
curl -X POST -F "file=@document.pdf" http://127.0.0.1:5000/summarize
```

## 📸 Demo
![PDF Summarizer UI](path_to_screenshot.png)

## 🤝 Contributing
Feel free to **open an issue** or **submit a pull request** if you’d like to improve this project!

## 📜 License
This project is open-source under the **MIT License**.

## 👤 Author
Created by Hari nath for **academic exam preparation**.

---
🔥 If you like this project, give it a ⭐ on GitHub! 🚀

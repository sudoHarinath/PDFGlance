# PDFGlance

A simple PDF summarization tool that extracts and summarizes content using Google's Gemini AI. Designed to help with academic exam preparation by providing concise and clear summaries of uploaded PDFs.

## Features
- Upload and summarize PDFs
- Uses Google's Gemini AI for intelligent summarization
- Provides a detailed and structured summary
- Share summaries via WhatsApp

## Tech Stack
- **Frontend:** React
- **Backend:** Flask (Python)
- **AI Model:** Gemini AI via LangChain
- **PDF Processing:** PyPDFLoader

## Installation
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

## Usage
1. Upload a PDF file.
2. Click "Summarize PDF."
3. View the generated summary.
4. Share the summary via WhatsApp.

## API Endpoint
- `POST /summarize`: Accepts a PDF file and returns a summary.

## Contributing
Feel free to open an issue or submit a pull request if you’d like to improve this project!

## License
This project is open-source under the MIT License.

## Author
Created by [Your Name] for academic exam preparation.


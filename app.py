# from flask import Flask, request, jsonify
# from flask_cors import CORS
# # from flask_ngrok import run_with_ngrok
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_community.document_loaders import PyPDFLoader
# from io import BytesIO
# import os
# import google.generativeai as genai

# os.environ['GOOGLE_API_KEY'] = "AIzaSyDDB78xZEeqQt6ymzUxFsqa0LAm4Hp7ybs"
# genai.configure(api_key = os.environ['GOOGLE_API_KEY'])
# app = Flask(__name__)
# # run_with_ngrok(app)
# CORS(app)
# # Initialize the langchain model
# model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.4)
# # model = genai.GenerativeModel('gemini-pro')
# # response = model.generate_content('Please summarise this document: ...')
# UPLOAD_FOLDER = 'uploaded_pdfs'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# @app.route('/summarize', methods=['POST'])
# def summarize_pdf():
#     try:
#         # Get the raw binary data of the PDF file
#         pdf_data = request.data
#         # print("hello",pdf_data)
#         # Save the PDF file to the upload folder
#         pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_pdf.pdf')
#         print("hello",pdf_path)
#         with open(pdf_path, 'wb') as pdf_file:
#             pdf_file.write(pdf_data)

#         # Load the entire PDF content using BytesIO
#         loader = PyPDFLoader(pdf_path)
#         data = loader.load()

#         # Create context from PDF content
#         context = "\n".join(str(p.page_content) for p in data)
#         # print(context)

#         # Generate a summary using langchain
#         prompt = "Generate a detailed and straightforward summary of the provided PDF content, ensuring each concept encountered is explained in a clear and understandable manner. Include examples to aid comprehension. Prioritize the inclusion of crucial details, methodologies, and concepts discussed in the content, covering all major topics comprehensively without omitting important points. Craft the summary with accessibility in mind, aiming for clarity and simplicity in explanations while ensuring completeness in coverage.\n" + context
#         summary = model.invoke(prompt)
#         # cleaned_summary = summary.content.replace('\n', '')

#         # Delete the uploaded PDF file
#         os.remove(pdf_path)

#         return jsonify({'summary': summary.content})

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from io import BytesIO
import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "AIzaSyDDB78xZEeqQt6ymzUxFsqa0LAm4Hp7ybs"
# os.environ['GOOGLE_API_KEY'] = "AIzaSyDNHMRbnD8xk6Jl3dIg7wkFRUluqS52StY"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

app = Flask(__name__)
CORS(app)

# Initialize the langchain model
model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.4,request_timeout=120)

UPLOAD_FOLDER = 'uploaded_pdfs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/summarize', methods=['POST'])
def summarize_pdf():
    try:
        # Get the raw binary data of the PDF file
        pdf_data = request.data
        
        # Save the PDF file to the upload folder
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_pdf.pdf')
        with open(pdf_path, 'wb') as pdf_file:
            pdf_file.write(pdf_data)

        # Load the entire PDF content using BytesIO
        loader = PyPDFLoader(pdf_path)
        data = loader.load()

        # Define the number of pages to process at a time
        page_batch_size = 15
        num_pages = len(data)
        print(num_pages)
        # Create context from PDF content, processing three pages at a time
        contexts = []
        for i in range(0, num_pages, page_batch_size):
            pages = data[i:i+page_batch_size]
            context = "\n".join(str(p.page_content) for p in pages)
            contexts.append(context)

        # Generate a summary for each batch of pages
        summaries = []
        for context in contexts:
            prompt = "Generate a detailed and straightforward summary of the provided PDF content, ensuring each concept encountered is explained in a clear and understandable manner. Include examples to aid comprehension. Prioritize the inclusion of crucial details, methodologies, and concepts discussed in the content, covering all major topics comprehensively without omitting important points. Craft the summary with accessibility in mind, aiming for clarity and simplicity in explanations while ensuring completeness in coverage.\n" + context
            summary = model.invoke(prompt)
            summaries.append(summary.content)

        # Concatenate the individual summaries into a single summary
        concatenated_summary = "\n".join(summaries)

        # Delete the uploaded PDF file
        os.remove(pdf_path)

        return jsonify({'summary': concatenated_summary})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

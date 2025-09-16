# **AI-Powered Resume Analyzer**

**Created & Developed by:** [Greeshmanth Basivi](https://www.linkedin.com/in/greeshmanth-basivi-44030a382/)

The AI Resume & Job Match Analyzer is a modern, full-stack web application designed to help job seekers evaluate their resume against a specific job description. By uploading a resume and pasting the job text, users receive an instant percentage-based match score and a highlighted list of keywords that are present and missing, providing a clear overview of lexical alignment.

## **✨ Features**

* **User-Friendly Interface**: A sleek, responsive, and modern UI with dynamic animations for a professional user experience.  
* **Versatile File Upload**: Seamlessly extracts text from both **PDF** and **DOCX** file formats.  
* **NLP-Powered Analysis**: Utilizes an advanced NLP engine with **spaCy** for text preprocessing, including lemmatization and stop-word removal.  
* **Accurate Match Score**: Calculates a precise, percentage-based similarity score using **scikit-learn's** TF-IDF and Cosine Similarity algorithms.  
* **Intelligent Skill Gap Analysis**: Moves beyond simple keyword counting by automatically categorizing key terms from the job description into:  
  * **Technical Skills** (e.g., Python, SQL, AWS)  
  * **Soft Skills** (e.g., Communication, Teamwork)  
  * **Action Verbs** (e.g., Developed, Managed, Analyzed)  
* **Actionable Feedback**: Clearly highlights which crucial skills are present in the resume and which are missing, empowering users to make targeted improvements.

## **📸 Application Screenshot**

![AI Resume Analyzer](assets/output.png)

## **🛠️ Tech Stack**

### **Backend & NLP**

* **Framework**: Flask (Python)  
* **NLP Library**: spaCy  
* **Machine Learning Library**: scikit-learn  
* **File Parsing**: PyMuPDF, python-docx

### **Frontend**

* **Languages**: HTML5, CSS3, JavaScript  
* **Styling**: Custom Modern UI with Animations  
* **Templating**: Jinja2

## **🚀 Getting Started**

Follow these instructions to set up and run the project on your local machine.

### **Prerequisites**

Make sure you have the following installed:

* [Python](https://www.python.org/downloads/) (v3.9 or later recommended)  
* pip and venv for Python package management

### **⚙️ Local Setup**

1. **Clone the Repository**  
   git clone \[https://github.com/your-username/AI-Resume-Analyzer.git\](https://github.com/your-username/AI-Resume-Analyzer.git)  
   cd AI-Resume-Analyzer

2. **Create a Python Virtual Environment**  
   python \-m venv venv

3. **Activate the Virtual Environment**  
   * On Windows:  
     .\\venv\\Scripts\\activate

   * On macOS/Linux:  
     source venv/bin/activate

4. **Install Dependencies**  
   pip install \-r requirements.txt

5. **Download the spaCy Language Model**  
   python \-m spacy download en\_core\_web\_sm

6. **Run the Flask Application**  
   python app.py

   The Flask server will start running. You can view the application in your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000). 

* This project leverages the powerful NLP capabilities of [spaCy](https://spacy.io/).  
* The core similarity scoring is made possible by the robust tools in [scikit-learn](https://scikit-learn.org/).
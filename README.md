# AI Resume Critique and Job Recommender
A Streamlit-based web application that analyzes your resume and recommends job listings tailored to your skills and experiences. It uses OpenAI's language model to extract key insights from your resume, identify skill gaps, generate a career roadmap, and suggest relevant job opportunities from LinkedIn.

---

## 🚀 Features
* **PDF Resume Upload**: Upload your resume in PDF format.
* **AI-Powered Resume Summary**: Automatically summarize your education, experience, and skills.
* **Skill Gap Analysis**: Get feedback on missing skills and certifications that could improve your job chances.
* **Career Roadmap**: Receive a personalized roadmap for future growth, including recommended skills, certifications, and industry exposure.
* **LinkedIn Job Recommendations**: Get real-time job listings based on extracted resume insights and keyword optimization.

## 🛠️ Tech Stack
|**Technology**|**Purpose**|
|--------------|-----------|
|Python|Core programming language|
|Streamlit	|Frontend framework for UI|
|OpenAI API	|Resume analysis, skill gap detection|
|APIFY TOKEN (or Scraper)	|To access job search and recommendation scraper|
|PDFMiner / PyMuPDF	|PDF text extraction|


## 📁 Project Structure
```python
    AI-RESUME-CRITIQUE/
        │
        ├── app.py                   # Main Streamlit app
        ├── src/
        │   ├── helper.py            # Contains PDF extraction and OpenAI API call logic
        │   └── job_api.py           # Job retrieval logic (LinkedIn scraping/API)
        │
        ├── requirements.txt         # Python dependencies
        └── README.md                # Project documentation
```

## 🧾 Setup Instructions
1. Clone the Repository
```bash
git clone https://github.com/kanon14/ai-resume-critique.git
cd ai-resume-critique
```
2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

# Using Anaconda
conda create -n ai-resume python=3.11 -y
conda activate ai-resume

# Using UV
uv venv --python 3.11
venv\Scripts\activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Configure API Keys
```bash
OPENAI_API_KEY = "your-openai-api-key"
APIFY_API_TOKEN = "your-apify-api-token"
```

5. Run the App
```bash
streamlit run app.py
open http://localhost:<port>
```

## 📝 Sample Usage
1. Upload a PDF version of your resume.
2. Let the app analyze your resume and extract:
    * A concise summary
    * Your skill gaps
    * A personalized roadmap
3. Click the "Get Job Recommendations" button.
4. Browse through the top job opportunities fetched from LinkedIn based on your profile.
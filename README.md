 💼 Job Skill Matching Chatbot

This project is an AI-powered **Job Skill Matching Chatbot** built using Python, Streamlit, Sentence Transformers, and OpenAI.

The system recommends suitable job roles based on user-provided skills and certificates by using semantic similarity search and an LLM-based response generator.

---

## 🚀 Features

- Semantic job matching using Sentence Transformers
- Skill + certificate-based recommendation system
- Cosine similarity for retrieving relevant job profiles
- AI-generated job suggestions using OpenAI GPT model
- Simple and interactive Streamlit interface

---

## 🧠 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Sentence Transformers
- Scikit-learn
- OpenAI API

---

## 📊 Dataset

The chatbot uses a CSV file:
it-jobs.csv
Dataset Columns:
It is worth mentioning that dataset was preprocessed and basing on the clusters of Skills and certifications 15 clusters were identified and two new groups naming 

category_group_name (Skills)
certificate_group_name (Certificates)
were formed

KMeans clustering was applied.

Job Title
category_group_name (Skills)
certificate_group_name (Certificates)
⚙️ Installation

Install required libraries:

pip install -r requirements.txt
🔑 API Key Setup

you directly run it on: https://decodelabs-skill-job-suggestion-chatbotproject3-jex3tmfpwawutc.streamlit.app/

**This below is only if u want to run it using your API key**
# Add your OpenAI API key here
# Example: api_key = "YOUR_OPENAI_API_KEY"
replace this:
api_key = st.secrets["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)

with this:

api_key = "YOUR_OPENAI_API_KEY"

client = OpenAI(api_key=api_key)

Add:

OPENAI_API_KEY = "your_api_key_here"
▶️ Run the Application
streamlit run app.py

you can also directly run it on: https://decodelabs-skill-job-suggestion-chatbotproject3-jex3tmfpwawutc.streamlit.app/

🧩 How It Works
User enters skills and certificates
Input is converted into embeddings
Cosine similarity finds the most relevant job matches
Top matching job profiles are retrieved
OpenAI generates a final recommendation with explanation
🤖 Model Used
Embedding Model:
all-MiniLM-L6-v2
LLM Model:
gpt-4o-mini
📁 Project Structure
project/
│
├── app.py
├── it-jobs.csv
├── requirements.txt
├── README.md
│
└── .streamlit/
    └── secrets.toml
📈 Future Improvements
Add resume upload (PDF parsing)
Improve ranking using weighted skill matching
Add job filtering (location, experience level)
Use FAISS for faster vector search
Deploy with Streamlit Cloud

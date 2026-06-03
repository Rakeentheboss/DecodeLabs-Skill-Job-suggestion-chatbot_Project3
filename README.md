 ## Job Skill Matching Chatbot

This project is an AI-powered **Job Skill Matching Chatbot** built using Python, Streamlit, Sentence Transformers, and OpenAI.

The system recommends suitable job roles based on user-provided skills and certificates by using semantic similarity search and an LLM-based response generator.

---

##  Features

- Semantic job matching using Sentence Transformers
- Skill + certificate-based recommendation system
- Cosine similarity for retrieving relevant job profiles
- AI-generated job suggestions using OpenAI GPT model
- Simple and interactive Streamlit interface

---
## DEVELOPMENT

In this project at first the gpt-4.0 mini model of Open AI was obtained as this will be used as LLM. Now we obtain the dataset, preprocess it later on we implement **KMEANS** clustering so that 15 unique clusters of skills can be figured out.
The final dataset became
Job Title	    Job Description	   category_group_name	    certificate_group_name

Now the category_group_name is basically the skill name. The category_group and certificate group are combined and their embeddings are generated using ALL-MINI-LM-V2-L6. When user gives input his/her input is also embedded in the same way. Then this is compared with the embeddings of the combined category_group and certificate_group using cosine similarity.  The title[i] retrieved has obtained the closest value to one. Finally, this title and combined category is fed to the LLM and a prompt is configured so that it can tell about the job and its description.



##  Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Sentence Transformers
- Scikit-learn
- OpenAI API

---

##  Dataset

The chatbot uses a CSV file:
it-jobs.csv
Dataset Columns:
It is worth mentioning that dataset was preprocessed and basing on the clusters of Skills and certifications 15 clusters were identified using KMEANS clustering and two new groups were formed naming:

category_group_name (Skills);
certificate_group_name (Certificates)



The it_jobs.csv had
Job Title;
Job Description;
category_group_name (Skills);
certificate_group_name (Certificates)

⚙️ Installation

Install required libraries:

pip install -r requirements.txt
 API Key Setup


Running the app:
you directly run it on: https://decodelabs-skill-job-suggestion-chatbotproject3-jex3tmfpwawutc.streamlit.app/


## System Architecture

User Input (Skills + Certificates)
        ↓
Sentence Transformer Embedding
        ↓
Cosine Similarity Search
        ↓
Top Matching Job Profiles
        ↓
GPT-4o-mini Recommendation Generator
        ↓
Final Career Suggestion


# This below is only if u want to run it using your API key

Add your OpenAI API key here
Example: api_key = "YOUR_OPENAI_API_KEY"
replace this:
api_key = st.secrets["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)

with this:

api_key = "YOUR_OPENAI_API_KEY"

client = OpenAI(api_key=api_key)

Add:

OPENAI_API_KEY = "your_api_key_here"
## Run the Application
streamlit run app.py

you can also directly run it on: https://decodelabs-skill-job-suggestion-chatbotproject3-jex3tmfpwawutc.streamlit.app/

## How It Works
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
## Project Structure
project/
│
├── app.py
├── it-jobs.csv
├── requirements.txt
├── README.md



📈 Future Improvements
Add resume upload (PDF parsing)
Improve ranking using weighted skill matching
Add job filtering (location, experience level)
Use FAISS for faster vector search
Deploy with Streamlit Cloud

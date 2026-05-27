# IT Support FAQ Chatbot

This project is a simple AI-powered IT Support FAQ chatbot built using Python, Streamlit, Sentence Transformers, and OpenAI.

The chatbot retrieves the most relevant IT support tickets from a dataset using semantic similarity and then generates a response using an OpenAI model.

---

## Features

- Semantic search using Sentence Transformers
- Similarity matching using cosine similarity
- AI-generated IT support responses
- Simple Streamlit web interface

---

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Sentence Transformers
- Scikit-learn
- OpenAI API

---

## Dataset

The chatbot uses a CSV file:

```text
tickets - tickets.csv
```

The dataset contains:
- Ticket Titles
- Ticket Resolutions

---

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## API Key Setup

OpenAI API key is used. You can directly run the app in my link.

https://decodelabs-skill-job-suggestion-chatbotproject3-jex3tmfpwawutc.streamlit.app/


## Run the Application
you can run the application using the command below but before that u need to adjust the API key settings.
Either store it in stream lit secrets and run or embed it directly on the code.
```bash
streamlit run app.py
```

---

## How It Works

1. The user enters an IT support question.
2. The application converts the query into embeddings.
3. Cosine similarity is used to retrieve the most relevant tickets.
4. The retrieved context is sent to the OpenAI model.
5. The chatbot generates an appropriate IT support response.

---

## Model Used

- Embedding Model:
  - all-MiniLM-L6-v2

- OpenAI Model:
  - gpt-4o-mini

---

## Project Structure

```text
project/
│
├── app.py
├── tickets - tickets.csv
├── requirements.txt
├── README.md
│
└── .streamlit/
    └── secrets.toml
```

---

## Future Improvements

- Add chat history
- Improve UI design
- Add ticket categories
- Use vector databases like FAISS
- Deploy online using Streamlit Cloud

---

## License

This project is for educational purposes only.
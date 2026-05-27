import streamlit as st
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI


api_key = st.secrets["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)

df = pd.read_csv("it-jobs.csv")



titles=df["Job Title"].astype(str).tolist()
skills=df["category_group_name"].astype(str).tolist()
certificates=df["certificate_group_name"].astype(str).tolist()

model="gpt-4o-mini"

combined_texts = [
    f"Skills: {s}. Certificates: {c}"
    for s, c in zip(skills, certificates)
]



embeddings_model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = embeddings_model.encode(combined_texts)


def retrieve(combined_input, top_k=5):
    query_embedding = embeddings_model.encode([combined_input])
    similarity = cosine_similarity(query_embedding, embeddings)[0]
    top_indices = np.argsort(similarity)[-top_k:][::-1]
    
    context = []

    for i in top_indices:
        context.append(( combined_texts[i], titles[i], similarity[i]))

    return context


def generate_response(combined_input, context):
    context_str = "\n\n".join([f"Combined Text: {combined_text}\nSimilarity: {similarity:.4f}" for combined_text, title, similarity in context])
    
    prompt = f"""You are a helpful assistant for Job support. Use the following context to answer the user's question. You will tell the appropriate job and its description to the user.

{context_str}



User: {combined_input}

Assistant: """
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

st.title("Job Support FAQ Chatbot")
skill = st.text_input("Enter your skills:")
certificates= st.text_input("Enter your certificates:")
if st.button("Get Answer"):
    if skill.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Finding relevant information..."):
            combined_input = f"Skills: {skill}. Certificates: {certificates}"
            context = retrieve(combined_input)
            answer = generate_response(combined_input, context)
            st.subheader("Answer:")
            st.write(answer)


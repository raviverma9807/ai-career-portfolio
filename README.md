# 🤖 AI-Powered Career Portfolio using Azure OpenAI

An AI-powered conversational portfolio built using **Azure OpenAI**, **Azure AI Search**, and **Retrieval-Augmented Generation (RAG)** that enables recruiters and hiring managers to interactively explore my professional experience, technical expertise, certifications, enterprise projects, and achievements through natural language conversations.

Instead of browsing a traditional resume, users can ask questions such as:

- Why should I hire Ravi?
- What Azure services has Ravi worked with?
- Tell me about Ravi's experience at Royal Mail.
- Explain Ravi's AI project.
- What Microsoft certifications does Ravi hold?

The application retrieves relevant information from an indexed knowledge base using **Hybrid Search (Keyword + Vector + Semantic Search)** and generates accurate, context-aware responses using **Azure OpenAI GPT**.

---

# 🚀 Live Demo

**Application:** https://ask-ravi.streamlit.app/

---

# ✨ Features

- AI-powered conversational portfolio
- Natural language question answering
- Retrieval-Augmented Generation (RAG)
- Hybrid Search for improved retrieval accuracy
- Semantic Search
- Vector Search
- Azure OpenAI GPT integration
- Azure OpenAI Embeddings
- Prompt Engineering
- Recruiter-focused responses
- Resume download
- LinkedIn & GitHub integration
- Conversation history
- Responsive Streamlit interface

---

# 🏗 Architecture

```
                User
                  │
                  ▼
          Streamlit Web App
                  │
                  ▼
      Azure OpenAI Embeddings
                  │
                  ▼
         Azure AI Search
     (Hybrid + Vector + Semantic)
                  │
                  ▼
       Relevant Document Chunks
                  │
                  ▼
        Azure OpenAI GPT Model
                  │
                  ▼
      Context-Aware AI Response
```

---

# ⚙ Technology Stack

## AI

- Azure OpenAI (GPT)
- Prompt Engineering
- Retrieval-Augmented Generation (RAG)

## Search

- Azure AI Search
- Hybrid Search
- Semantic Search
- Vector Search
- text-embedding-3-small

## Azure

- Azure OpenAI
- Azure AI Search
- Azure Blob Storage
- Azure AI Foundry

## Backend

- Python

## Frontend

- Streamlit

## Version Control

- Git
- GitHub

---

# 🔍 How It Works

### 1. Knowledge Base

Professional information including:

- Resume
- Work Experience
- Projects
- Skills
- Certifications
- Education

is stored in Azure Blob Storage.

---

### 2. Indexing

Documents are indexed into Azure AI Search.

During indexing:

- Documents are chunked
- Vector embeddings are generated using **text-embedding-3-small**
- Chunks are stored with embeddings for semantic retrieval

---

### 3. User Question

When a recruiter asks a question:

Example:

> "Why should I hire Ravi?"

---

### 4. Retrieval

The application performs Hybrid Search by combining:

- Keyword Search
- Vector Search
- Semantic Ranking

to retrieve the most relevant document chunks.

---

### 5. Response Generation

Retrieved context is passed to Azure OpenAI GPT along with a recruiter-focused system prompt.

The model generates a grounded response without hallucinating information outside the indexed documents.

---

# 📁 Project Structure

```
ask-ravi-bot/
│
├── app.py
├── prompts/
├── services/
│   ├── openai_service.py
│   └── search_service.py
├── utils/
├── resume/
├── requirements.txt
└── README.md
```

---


# 🎯 Future Enhancements

- Conversation memory
- Streaming AI responses
- Voice interaction
- Multi-user portfolio support
- Resume upload and dynamic indexing
- Recruiter analytics dashboard

---

# 👨‍💻 About

Developed by **Ravi Verma**

Azure .NET Developer | Azure OpenAI | Azure AI Search | Generative AI | Microservices | Cloud-native Applications

LinkedIn:
https://www.linkedin.com/in/ravi-verma-2b757817b/

GitHub:
https://github.com/raviverma9807/

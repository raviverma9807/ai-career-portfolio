FOLLOW_UPS = {
    "azure": [
        "Which Azure services has Ravi worked with?",
        "Explain Ravi's event-driven architecture experience.",
        "Tell me about Ravi's microservices experience.",
        "Describe Ravi's production support experience."
    ],

    "project": [
        "Tell me more about the Royal Mail project.",
        "Tell me about the Walmart ASDA project.",
        "Which project demonstrates Ravi's Azure expertise?",
        "Which project was the most technically challenging?"
    ],

    "ai": [
        "How was the RAG pipeline implemented?",
        "How does Azure AI Search work in this project?",
        "Why was Hybrid Search used?",
        "Which Azure AI services power this application?"
    ],

    "work": [
        "Tell me about Ravi's experience at Capgemini.",
        "What did Ravi do at TCS?",
        "Describe Ravi's role at Infosys.",
        "Which industries has Ravi worked in?"
    ],

    "certification": [
        "Which Microsoft certifications does Ravi hold?",
        "Does Ravi have Azure Developer certification?",
        "Does Ravi have Azure AI certification?",
        "How do Ravi's certifications complement his experience?"
    ],

    "education": [
        "Which college did Ravi graduate from?",
        "What is Ravi's educational background?",
        "What academic achievements does Ravi have?",
        "How does Ravi's education support his career?"
    ],

    "personal": [
        "Where is Ravi currently based?",
        "What are Ravi's hobbies and interests?",
        "Which languages does Ravi speak?",
        "Tell me about Ravi's educational background."
    ],

    "default": [
        "Tell me about Ravi's Azure experience.",
        "Describe Ravi's work experience.",
        "Tell me about Ravi's major projects.",
        "What certifications does Ravi hold?"
    ]
}


def get_followups(question: str):

    text = question.lower()

    # AI
    if any(keyword in text for keyword in [
        "artificial intelligence",
        "azure openai",
        "openai",
        "generative ai",
        "ai-powered projects",
        "rag",
        "retrieval-augmented generation",
        "hybrid search",
        "vector search",
        "semantic search"
    ]):
        return FOLLOW_UPS["ai"]

    # Projects
    if any(keyword in text for keyword in [
        "project",
        "projects",
        "royal mail",
        "walmart",
        "asda",
        "cvs",
        "welsh water"
    ]):
        return FOLLOW_UPS["project"]

    # Azure
    if "azure" in text:
        return FOLLOW_UPS["azure"]

    # Work Experience
    if any(keyword in text for keyword in [
        "experience",
        "work",
        "capgemini",
        "tcs",
        "infosys"
    ]):
        return FOLLOW_UPS["work"]

    # Certifications
    if "cert" in text:
        return FOLLOW_UPS["certification"]

    # Education
    if any(keyword in text for keyword in [
        "education",
        "college",
        "university"
    ]):
        return FOLLOW_UPS["education"]

    # Personal
    if any(keyword in text for keyword in [
        "who is",
        "about ravi",
        "personal",
        "personal details",
        "contact",
        "profile",
        "background",
        "location",
        "hobbies",
        "interests"
    ]):
        return FOLLOW_UPS["personal"]

    return FOLLOW_UPS["default"]
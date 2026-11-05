from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Configure CORS so your React frontend can access this API
origins = [
    "http://localhost:3000",  # Default Create-React-App port
    "http://localhost:5173",  # Default Vite + React port
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
    "https://portfolio-v3-phi-rust.vercel.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Define a structure for a Contact Form request
class ContactMessage(BaseModel):
    name: str
    email: str
    affiliation: str | None = None
    message: str


class Project(BaseModel):
    id: int
    num: str
    title: str
    description: str
    tech: list[str]
    year: str
    crest: str
    art: str
    github: str
    status: str = "Completed"


class SkillCategory(BaseModel):
    title: str
    description: str
    image: str
    reverse: bool = False
    skills: list[dict[str, str]]


class EducationItem(BaseModel):
    stage: str
    degree: str
    institution: str
    duration: str
    status: str
    gpa: str
    description: str
    modules: list[str]
    current: bool = False


PROJECTS = [
    Project(
        id=1,
        num="01",
        title="Local RAG Platform for Academic Data",
        description="Built an end-to-end RAG application with FastAPI, LangChain, and LLaMA 3 to query unstructured academic data.",
        tech=["Python", "FastAPI", "LangChain", "LLaMA 3", "Chroma DB", "Google Drive API"],
        year="2026",
        crest="/images/survey-logo.jpg",
        art="/images/shiganshina-wall.jpg",
        github="https://github.com/lahiruimesh",
    ),
    Project(
        id=2,
        num="02",
        title="Stateful AI Travel Orchestrator",
        description="Built an agentic AI travel system using LangGraph with memory, dynamic workflow routing, and real-time APIs.",
        tech=["Python", "LangGraph", "FastAPI", "Groq (Llama 3.1)", "n8n", "Next.js", "TypeScript"],
        year="2026",
        crest="/images/hero-wall.png",
        art="/images/hero-wall.png",
        github="https://github.com/lahiruimesh",
    ),
    Project(
        id=3,
        num="03",
        title="Brain Tumor Classification System",
        description="Developed an EfficientNetB3 deep learning model for MRI scan classification with an OpenCV preprocessing pipeline.",
        tech=["Python", "TensorFlow", "Keras", "EfficientNetB3", "OpenCV", "Scikit-learn", "NumPy"],
        year="2026",
        crest="/images/ArmoredTitan.png",
        art="/images/ArmoredTitan.png",
        github="https://github.com/lahiruimesh",
    ),
    Project(
        id=4,
        num="04",
        title="Healthcare Risk Prediction Platform",
        description="Built a machine learning web application to predict heart disease, diabetes, and high cholesterol risk with Streamlit dashboards.",
        tech=["Python", "Streamlit", "XGBoost", "Scikit-learn", "Pandas", "NumPy", "Matplotlib", "Seaborn"],
        year="2026",
        crest="/images/BeastTitan.png",
        art="/images/BeastTitan.png",
        github="https://github.com/lahiruimesh",
    ),
    Project(
        id=5,
        num="05",
        title="Sellaro Customizable E-Commerce Web Template System",
        description="Built a multi-tenant e-commerce platform for SMEs with secure Stripe integration, product management, and customizable UI templates.",
        tech=["Next.js", "NestJS", "MongoDB", "Stripe", "Cloudinary", "JWT", "Figma"],
        year="2024-25",
        crest="/images/col.png",
        art="/images/col.png",
        github="https://github.com/lahiruimesh",
    ),
    Project(
            id=6,
            num="06",
            title="Sellaro Customizable E-Commerce Web Template System",
            description="Built a multi-tenant e-commerce platform for SMEs with secure Stripe integration, product management, and customizable UI templates.",
            tech=["Next.js", "NestJS", "MongoDB", "Stripe", "Cloudinary", "JWT", "Figma"],
            year="2024-25",
            crest="/images/col.png",
            art="/images/col.png",
            github="https://github.com/lahiruimesh",
        ),
]

SKILL_CATEGORIES = [
    {
        "title": "Programming Languages",
        "description": "Core languages used across AI, automation, and product development.",
        "image": "/images/PL.png",
        "skills": [
            {"name": "Java", "level": "Strong", "style": "92%"},
            {"name": "Python", "level": "95%", "style": "95%"},
            {"name": "JavaScript", "level": "88%", "style": "88%"},
        ],
    },
    {
        "title": "Machine Learning & AI",
        "description": "Model development, preprocessing, evaluation, and agentic workflows.",
        "image": "/images/PL.png",
        "reverse": True,
        "skills": [
            {"name": "TensorFlow / Keras", "level": "90%", "style": "90%"},
            {"name": "Scikit-Learn / XGBoost", "level": "92%", "style": "92%"},
            {"name": "LangChain / LangGraph / n8n", "level": "87%", "style": "87%"},
        ],
    },
    {
        "title": "Web & Full-Stack",
        "description": "Frontend and backend application development for scalable products.",
        "image": "/images/PureTitan.png",
        "skills": [
            {"name": "ReactJS / NextJS", "level": "88%", "style": "88%"},
            {"name": "FastAPI / NestJS", "level": "90%", "style": "90%"},
            {"name": "Streamlit", "level": "84%", "style": "84%"},
        ],
    },
    {
        "title": "Data Science & Analytics",
        "description": "Analysis, visualization, and data preparation for decision making.",
        "image": "/images/BeastTitan.png",
        "reverse": True,
        "skills": [
            {"name": "Pandas / NumPy", "level": "92%", "style": "92%"},
            {"name": "Matplotlib / Seaborn", "level": "86%", "style": "86%"},
            {"name": "Feature Engineering", "level": "90%", "style": "90%"},
        ],
    },
    {
        "title": "Databases & Tools",
        "description": "Storage, collaboration, and delivery tools used in daily development.",
        "image": "/images/col.png",
        "skills": [
            {"name": "MySQL / PostgreSQL / MongoDB", "level": "88%", "style": "88%"},
            {"name": "Git / GitHub", "level": "95%", "style": "95%"},
            {"name": "Adobe / Canva / VS Code", "level": "86%", "style": "86%"},
        ],
    },
]

EDUCATION = [
    {
        "stage": "Current Degree",
        "degree": "B.Sc. (Hons) in Information Technology",
        "institution": "Faculty of Information Technology, University of Moratuwa",
        "duration": "2022 — Present",
        "status": "In Progress",
        "gpa": "3.39 / 4.00",
        "description": "Undergraduate study focused on information technology, software engineering, and applied AI/ML development.",
        "modules": ["AI / ML", "Web Development", "Databases", "Software Engineering"],
        "current": True,
    },
    {
        "stage": "Secondary Education",
        "degree": "GCE Advanced Level",
        "institution": "Bandarawela Central College",
        "duration": "2018 — 2020",
        "status": "Science Stream",
        "gpa": "Z-score 1.6220",
        "description": "Completed the science stream and built a strong foundation in analytical problem solving.",
        "modules": ["Physics", "Chemistry", "Combined Mathematics"],
        "current": False,
    },
]

CONTACT_MESSAGES: list[ContactMessage] = []

@app.get("/api/projects")
def get_projects() -> list[Project]:
    return PROJECTS


@app.get("/api/skills")
def get_skills() -> list[dict[str, object]]:
    return SKILL_CATEGORIES


@app.get("/api/education")
def get_education() -> list[dict[str, object]]:
    return EDUCATION

@app.post("/api/contact")
def receive_contact(data: ContactMessage):
    CONTACT_MESSAGES.append(data)
    print(f"Received message from {data.name} ({data.email}): {data.message}")
    return {
        "status": "success",
        "message": "Message received successfully!",
        "stored_messages": len(CONTACT_MESSAGES),
    }
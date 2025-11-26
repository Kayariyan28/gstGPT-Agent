# gstGPT: Enterprise-Grade AI GST Counsel & Automation Agent

![gstGPT Banner](apps/web/public/images/project_banner.jpg)

![Status](https://img.shields.io/badge/Status-Beta-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Tech Stack](https://img.shields.io/badge/Stack-Next.js%20%7C%20FastAPI%20%7C%20Postgres%20%7C%20Gemini-orange)

**gstGPT** is a next-generation **AI-powered Tax Automation Platform** designed specifically for the Indian market. It transcends traditional tax software by combining a **Retrieval-Augmented Generation (RAG)** expert system with an **Agentic Workflow Engine**. 

Unlike standard chatbots, gstGPT doesn't just answer questions—it **performs work**. It connects directly to your financial data to analyze sales, compute tax liabilities, and draft GSTR returns autonomously.

---

## 🚀 Key Features

### 1. 🧠 AI Counsel (RAG Engine)
- **Expert Knowledge Base**: Ingested with the latest GST Acts, Rules, and Notifications.
- **Context-Aware**: Understands complex tax scenarios and provides citations.
- **Powered by Gemini**: Utilizes Google's advanced LLM for high-accuracy reasoning.

### 2. 🤖 Agentic Automation
- **Data Analyst**: "What is my sales summary for October?" — The Agent queries your database and visualizes the results.
- **Action Taker**: "Draft my GSTR-1" — The Agent triggers workflows to create return drafts in the system.
- **Tool Use**: Seamlessly switches between answering questions and executing database tools.

### 3. ⚡ Modern Full-Stack Architecture
- **Frontend**: Next.js 14 with Tailwind CSS and Shadcn UI for a premium, responsive experience.
- **Backend**: FastAPI (Python) for high-performance async API handling.
- **Database**: PostgreSQL for transactional data (Invoices, Returns) and Qdrant for vector embeddings.
- **Infrastructure**: Dockerized microservices architecture for easy deployment.

---

## 🛠️ Technology Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | Next.js 14, React, TypeScript | Server-Side Rendering, Type Safety |
| **Styling** | Tailwind CSS, Shadcn UI | Modern, accessible component library |
| **Backend** | FastAPI, Python 3.10+ | Async API, Pydantic validation |
| **Database** | PostgreSQL | Relational data (Invoices, Users) |
| **Vector DB** | Qdrant | Semantic search for RAG |
| **LLM** | Google Gemini 1.5 Flash | Reasoning and Function Calling |
| **ORM** | SQLAlchemy | Database abstraction |
| **DevOps** | Docker, Poetry, TurboRepo | Containerization and Monorepo management |

---

## 🏁 Getting Started

### Prerequisites
- Docker & Docker Compose
- Node.js 18+
- Python 3.10+
- Google Gemini API Key

### Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/your-org/gstGPT.git
    cd gstGPT
    ```

2.  **Environment Setup**
    Create a `.env` file in `apps/api`:
    ```env
    DATABASE_URL=postgresql://postgres:postgres@localhost:5433/gstgpt
    GEMINI_API_KEY=your_api_key_here
    ```

3.  **Start Infrastructure**
    ```bash
    docker-compose up -d
    ```

4.  **Install Dependencies & Run**
    ```bash
    # Backend
    cd apps/api
    poetry install
    poetry run uvicorn app.main:app --reload --port 8000

    # Frontend
    cd apps/web
    npm install
    npm run dev
    ```

5.  **Access the Dashboard**
    Open [http://localhost:3000/dashboard/counsel](http://localhost:3000/dashboard/counsel)

---

## 📊 System Architecture

![System Architecture](apps/web/public/images/system_architecture.png)

For a detailed breakdown of the system design, data flow, and component interactions, please refer to the [Architecture Documentation](docs/ARCHITECTURE.md).

## 💼 Business Case

Interested in the market opportunity, problem statement, and strategic vision? Read our [Business Case & Market Analysis](docs/BUSINESS_CASE.md).

---

## 🔒 Security & Compliance
- **Data Privacy**: Financial data is stored locally/on-premise (in Docker).
- **Encryption**: All sensitive data is encrypted at rest and in transit.
- **Audit Logs**: Every Agent action is logged for compliance and review.

---

## 👨‍💻 Creator Credits

**Karan Chandra Dey** — *AI Expert, Product Strategist, AI Product & Innovation Expert*
<br>
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/karan-chandra-dey-23392b1b9)

---

## 🤝 Contributing
We welcome contributions! Please see `CONTRIBUTING.md` for guidelines.

---

**gstGPT** — *Simplifying GST for India, one prompt at a time.*

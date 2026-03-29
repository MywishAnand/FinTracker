# 💸 FinTracker: Agentic Financial Intelligence & Anomaly Detection

***Detect. Analyze. Flag.*** <br>
FinTracker is a high-performance, agentic pipeline designed to solve the "Expense Visibility Gap" for modern businesses. It automates the ingestion of unstructured financial documents, enforces strict PII data privacy, categorizes expenditures via semantic intelligence, and identifies capital leakage through hybrid anomaly detection.

🌐 **Live Demo:** https://fintracker-agent.streamlit.app/  
📂 **Repository:** https://github.com/MywishAnand/FinTracker  

---

## 🧠 AI Intelligence

**FinTracker** is an AI-powered modular agentic pipeline that uses different layers of intelligence, like Statistical Intelligence, to simulate the reasoning of a Financial Forensic Engineer:

### 1. **Semantic Intelligence (Categorization)**
The engine doesn't just look at names; it performs **Semantic Tagging**. It maps unstructured merchant strings (like "AWS 12345 SEATTLE") into high-level business categories (*Essential Operations, Variable Growth, Redundant/Shadow IT*) using a knowledge-lexicon. This moves the app beyond raw calculation into **contextual business reasoning**.

### 2. **Heuristic-Based Multi-Modal Ingestion**
Reading unstructured PDFs is a classic AI challenge. FinTracker uses a **Document Parsing Agent** that acts as a structural proxy for Vision-Language Models. It interprets the visual coordinates of PDF tables to reconstruct meaningful financial ledgers from fragmented data sources.

### 3. **Hybrid Anomaly Analytics**
The platform features an **Anomaly Detection Agent** that uses a dual-engine approach:
*   **Statistical Intelligence (Z-Scores)**: It calculates the "velocity" of your spending and flags items that fall **2.5 standard deviations** from the category mean.
*   **Logical Reasoning**: It detects "contextual anomalies"—like a subscription for a Saturday or Sunday, duplicate vendor billing, or "price creep"—which are often missed by traditional software.

### 4. **Reasoning-Based Optimization**
The final layer is the **Optimizer Intelligence**. Instead of just showing values, it generates an **Agentic Roadmap** with a "Leakage Score." This score is a weighted algorithmic grade of your capital efficiency, identifying exactly where you have high-impact, low-effort saving opportunities.

---

## 🚀 Key Features
- **Multimodal Ingestion**: Seamlessly ingest `.pdf`, `.csv`, and `.xlsx` financial records.
- **PII Sanitization**: Automatic redaction of sensitive data (SSNs, Credit Cards, Emails) before analysis.
- **Semantic Categorization**: Intelligent grouping of spend into Essential, Growth, and Redundant buckets.
- **Anomaly Detection**: Dual-layer detection using statistical Z-scores and contextual business logic.
- **Executive Dashboard**: A reactive Streamlit interface for real-time visualization and cost-reduction roadmaps.
- **CFO Export**: Generate redacted, professional CSV summaries for financial reporting.

---

### 🏗️ **FinTracker Project Structure**

The project is organized using a **Modular Agentic Architecture**, separating the logic for data, security, analytics, and presentation.

```text
FinTracker/
├── app.py                      # 🚀 Executive Dashboard (Streamlit Entrypoint)
├── README.md                   # 📖 Project Overview & Setup (GitHub Ready)
├── model_architecture.md       # 🏗️ Technical Deep-Dive & Design Logic
├── requirements.txt            # 📦 Python Dependencies
├── .gitignore                  # 🔒 Sensitive Data Exclusions
│
├── engine/                     # 🧠 Agentic Core Modules
│   ├── parser.py               # 📂 Multimodal Ingestion (PDF/CSV/XLSX)
│   ├── categorizer.py          # 🏷️ Semantic Taxonomy & Classification
│   ├── anomaly_detector.py     # 🚨 Statistical (Z-Score) & Logic Analysis
│   └── optimizer.py            # 📉 Strategic Cost-Reduction Intelligence
│
├── utils/                      # 🛠️ Utility Layer
│   └── security.py             # 🛡️ PII Redaction Agent (Regex-based)
│
└── venv/                       # 🐍 Local Virtual Environment
```

---

## 🛠️ Project Setup & Installation

### Prerequisites
- Python 3.10 or higher
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/MywishAnand/FinTracker.git
cd FinTracker
```

### 2. Configure Environment
Create and activate a virtual environment to isolate dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the Application
Start the interactive dashboard:
```bash
streamlit run app.py
```

---

## 📋 How to Use
1. **Initialize**: Launch the app and view the "Data Gateway" on the main dashboard.
2. **Upload**: Drag and drop your 📄 bank statements, 💳 PDF receipts, or 📊 transaction ledgers.
3. **Analyze**: The agentic pipeline automatically sanities, categorizes, and flags your data.
4. **Optimize**: Review the "Cost Reduction Roadmap" and specific anomalies flagged by the AI.
5. **Export**: Use the "Download CFO Summary Report" button to save your sanitized and processed ledger.

---

## 🔒 Security & Privacy
Data security is built into the core of FinTracker. All processing occurs locally within the execution environment. The **Security Engine** uses regex-based patterns to identify and redact personal identifiers immediately after ingestion, ensuring that neither the categorization logic nor the final dashboard ever handles exposed PII.


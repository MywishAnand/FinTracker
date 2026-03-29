# 💸 FinTracker: Agentic Financial Intelligence & Anomaly Detection

Detect. Analyze. Flag.
FinTracker is a high-performance, agentic pipeline designed to solve the "Expense Visibility Gap" for modern businesses. It automates the ingestion of unstructured financial documents, enforces strict PII data privacy, categorizes expenditures via semantic intelligence, and identifies capital leakage through hybrid anomaly detection.

🌐 **Live Demo:** https://fintracker-agent.streamlit.app/  
📂 **Repository:** https://github.com/MywishAnand/FinTracker  

## 🚀 Key Features
- **Multimodal Ingestion**: Seamlessly ingest `.pdf`, `.csv`, and `.xlsx` financial records.
- **PII Sanitization**: Automatic redaction of sensitive data (SSNs, Credit Cards, Emails) before analysis.
- **Semantic Categorization**: Intelligent grouping of spend into Essential, Growth, and Redundant buckets.
- **Anomaly Detection**: Dual-layer detection using statistical Z-scores and contextual business logic.
- **Executive Dashboard**: A reactive Streamlit interface for real-time visualization and cost-reduction roadmaps.
- **CFO Export**: Generate redacted, professional CSV summaries for financial reporting.

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


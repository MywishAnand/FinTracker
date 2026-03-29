# 🏗️ FinTracker Architecture & Engineering

This document outlines the technical design, architectural patterns, and functional logic of the FinTracker agentic pipeline.

## 1. System Architecture
FinTracker operates as a modular, one-way pipeline. Each stage is decoupled, allowing for individual modules to be updated or replaced without impacting the overall system integrity.

### Data Flow Diagram
`Document Upload` → `Ingestion Engine` → `PII Redactor` → `Semantic Categorizer` → `Anomaly Detector` → `Optimizer` → `Streamlit UI`

---

## 2. Core Modules & Logic

### 📂 Ingestion Engine (`engine/parser.py`)
- **Responsibility**: Normalization of unstructured data sources.
- **Mechanism**: Extracts textual and tabular data from PDFs using coordinate-based table reconstruction.
- **Normalization**: Cleanses column headers (lowercase/strip/synonym mapping) and enforces a unified schema across all transaction types.

### 🛡️ Security Engine (`utils/security.py`)
- **Responsibility**: Privacy enforcement.
- **Logic**: Uses a Regular Expression (Regex) parser to identify and scrub:
  - **SSN**: Pattern `\b\d{3}-\d{2}-\d{4}\b`.
  - **Credit Cards**: Luhn-adjacent digit string patterns.
  - **Emails**: Standard RFC-compliant address patterns.

### 🏷️ Semantic Categorizer (`engine/categorizer.py`)
- **Responsibility**: Expenditure taxonomy.
- **Classification**: Groups transactions into three primary buckets:
  - **Essential Operations**: Infrastructure and mandatory toolsets.
  - **Variable Growth**: Sales, marketing, and expansionary costs.
  - **Redundant/Shadow IT**: Lifestyle services and unoptimized software.

### 🚨 Anomaly Detector (`engine/anomaly_detector.py`)
- **Responsibility**: Fraud and waste identification.
- **Hybrid Methods**:
  - **Statistical Analysis**: Implements a rolling **Z-Score** calculation. Transactions exceeding 2.5 standard deviations from the category mean are flagged.
  - **Contextual Heuristics**: Identifies billing duplicates, vendor "price creep," and abnormal weekend billing spikes (> $500).

### 📈 Optimizer Intelligence (`engine/optimizer.py`)
- **Responsibility**: Strategic cost-reduction.
- **Metrics**: Calculates the **Platform Leakage Score**, a weighted metric representing the ratio of capital waste to total gross expenditure.

---

## 3. Use Cases
- **Corporate Audit**: Rapidly sanitizing ledgers and identifying duplicate vendor billing.
- **Operational Optimization**: Finding and eliminating "Shadow IT" (redundant software seats).
- **Personal Finance**: High-fidelity categorization and unusual spend detection for power users.

## 4. Technology Stack
- **Frontend**: Streamlit
- **Data Engineering**: Pandas, NumPy, Scipy
- **Document Processing**: PDFPlumber
- **Visualization**: Plotly Express

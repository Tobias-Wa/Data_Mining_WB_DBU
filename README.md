# Anomaly Detection in Synthetic Biological Data Using Python

This repository contains a Data Mining project developed as part of the **DMI01 Data Mining** module in the *AI Empowered Data Analyst* training program at DBU (Digital Business University of Applied Sciences). The objective was to apply anomaly detection methods to synthetically generated biological data using Python, supported by generative AI, and structured according to the CRISP-DM methodology.

## Project Objectives

- Design a reproducible data mining process for identifying anomalies
- Generate realistic synthetic biological data using generative AI (ChatGPT)
- Apply and compare two different anomaly detection techniques:
  - Statistical 3-Sigma Rule
  - Machine Learning–based Isolation Forest
- Implement and document the full workflow in Python using Jupyter Notebook

## Repository Contents

- `Anomaleerkennung.ipynb` – Full workflow
- `Anomalieerkennung_Notebook.ipynb` – Full analysis workflow with step-by-step explanations
- `anomalies.json` – JSON export of detected anomalies
- `README.md` – Project documentation
- `synthetische_daten.csv` – Synthetic data file (not included in the repository)

## Technologies Used

- **Programming Language:** Python 3.x
- **Libraries:** `pandas`, `numpy`, `matplotlib`, `scikit-learn`
- **Models:** 3-Sigma Rule, Isolation Forest
- **Generative AI:** ChatGPT (GPT-4o) for synthetic data generation and documentation support
- **Framework:** CRISP-DM (Cross-Industry Standard Process for Data Mining)

## Results

- The 3-Sigma Rule effectively identified clear outliers in individual features.
- The Isolation Forest enabled detection of anomalies in multivariate feature spaces but showed limited interpretability in this specific dataset.
- The code is modular, transparent, and easily adaptable to real-world biological datasets.

## Usage Notes

- The file `synthetische_daten.csv` is **included** in the repository.
- When using your own dataset, make sure to update file paths in the notebook accordingly.
- If deploying this pipeline with real data or integrating LLMs, consider applicable data privacy regulations and the **EU AI Act**.

## Author

**Tobias Wachtel**  
Final project submitted for the DMI01 Data Mining module  
AI Empowered Data Analyst Program – March 2025

## License

This project is provided without a specific license and is intended for educational and demonstrational purposes only.

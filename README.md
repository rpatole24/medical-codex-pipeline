Medical Codex Pipeline

This repository contains Python scripts to process different medical codex datasets (SNOMED CT, ICD-10-CM, ICD-10-WHO, HCPCS, LOINC, RxNorm, and NPI) into standardized CSV files.

Setup

1. Clone the Repository
git clone ⁦https://github.com/<your-username>/medical-codex-pipeline.git⁩
cd medical-codex-pipeline

2. Create a Virtual Environment

python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

3. Install Dependencies

pip install -r requirements.txt

Usage

Each script in the `scripts/` folder processes one codex:

	•	Raw input files should be placed in the `input/` folder
	•	Cleaned outputs will be written to the `output/` folder

Example: Run ICD-10-CM Processor

python scripts/icd10cm_processor.py

Example: Run RxNorm Processor

python scripts/rxnorm_processor.py

Output Format

Each processed CSV has the following columns:

	•	**code** – Primary identifier
	•	**description** – Human-readable description
	•	**last_updated** – Processing timestamp


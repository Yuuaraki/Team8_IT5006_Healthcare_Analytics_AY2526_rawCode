#IT5006 Healthcare Readmission Analytics _ Team 8

#Overview
This capstone project requires student teams to conduct a comprehensive analytics workflow using real-world healthcare data. Teams will analyze the
Diabetes 130-US Hospitals (1999–2008)
dataset topredict hospital readmissions and understand key factors influencing patient outcomes.

## 1) Environment setup
1. create and activiate a virtual environment
   ```bash
   python -m venv .venv
   .\.venv\Scripts|activiate
    ```

2. install dependencies
   ```bash
   pip install -r requirements.txt
   pip install -U pip
   ```

## 2) Project layout
```

.
│   .gitignore
│   README.md
│   requirements.txt
│
├───dashboard # streamlit app
├───data      # keep large/raw data out of git (see .gitignore)
│   ├───interim
│   ├───processed
│   └───raw
├───docs      # data ploicy, references, diagrams
├───notebooks #Jupyter notebooks for EDA and experiments   
├───reports   # PDF for drafts for each phase
└───src       # reusable code (data loading, features, models, metrics)
    ├───data
    ├───eda
    ├───models
    └───utils
```
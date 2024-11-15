# Group XXX 2024 NISR Submission:

## Group Members:
- Denis Karani
- Christian Okeke
- Charite Uwatwembi.


## Running the code:
- Clone the repository
```bash
git clone 
```

- Change directory to the repository
```bash
cd NISR-2024
```

- Create a virtual environment
```bash
python3 -m venv venv
```

- Install the required packages
```bash
pip install -r requirements.txt
```

- navigate to src
```bash
cd src
```

- Run the app
```bash
cd src
streamlit run app.py
```

>[!NOTE]
>The chatbot is under development and works perfect on the langflow visualization. However, currently, it is run seperately but will be part of the main app in the next submission. 

## Run the chatbot
- navigate to langflow
```bash
cd langflow
```

- start Ollama and langflow
```bash
python -m langflow run
```
```bash
ollama run llama3
```

- run the app
```bash
python3 output_from_file.py
```

>[!NOTE]
>Users can create a similar flow on langflow and test using different files and questions. 
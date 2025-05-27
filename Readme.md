# 🧠 Travel Assistant Chatbot using CrewAI & Qdrant

## 📌 Project Description
This project is a travel assistant chatbot that leverages *CrewAI, **LangChain, **OpenAI embeddings, and **Qdrant* to:
- Ingest and chunk travel-related text data.
- Index the data using vector embeddings.
- Retrieve relevant information using semantic search.
- Generate human-like responses using a team of specialized agents.
- Provide a simple chatbot interface via *Streamlit*.

---

## 🚀 Usage & How to Run
### 2️⃣ Install the required dependencies:
bash
pip install -r requirements.txt


### 3️⃣ Set your OpenAI API Key:
You can either:
- Export it as an environment variable:
  bash
  export OPENAI_API_KEY="your_key_here"  # for Linux/macOS
  
 Windows PowerShell:
  powershell
  $env:OPENAI_API_KEY="your_key_here"
  

  python
  openai.api_key = "your_key_here"
  

### 4️⃣ Run the project step by step:

#### ✅ Step 1: Preprocess & Chunk Data
Run data_ingest.ipynb to load and process raw data into chunks.

#### ✅ Step 2: Index Chunks into Qdrant
Run:
bash
python index_and_retrieve.py


#### ✅ Step 3: Define the AI Crew
Run:
bash
python crew_config.py
### ✅ Step 4: Compose Response Logic
Run:
bash
python compose_response.py


#### ✅ Step 5: Launch the Chatbot UI
Run:
bash
streamlit run app.py


---

## 🧾 Requirements

List of Python packages needed (already in requirements.txt):

- openai
- crewai
- langchain
- qdrant-client
- tqdm
- streamlit
- pydantic
- python-dotenv
- jupyter

Install with:
bash
pip install -r requirements.txt

## 🗂 Project Structure


.
├── app.py                     # Streamlit chatbot interface
├── compose_response.py       # Summarizer and response composer
├── crew_config.py            # CrewAI agents setup
├── data_ingest.py        # Data preprocessing and chunking
├── index_and_retrieve.py     # Embedding + storing in Qdrant
├── processed_chunks.json     # Output from chunking step
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation


---

## 🧠 Crew Members (Agents)

- *Retriever Agent* – Finds relevant text chunks.
- *Summarizer Agent* – Compresses and summarizes context.
- *Responder Agent* – Crafts final answers in natural language.

---

## 📬 Contact
If you have any questions or need help, feel free to contact the maintainer or open an issue.



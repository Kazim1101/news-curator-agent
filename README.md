# 📰 News Curator Agent

**News Curator Agent** is an intelligent system that fetches articles from various news aggregators, filters them for relevance, and summarizes each article into a concise, readable digest. It is designed to provide a clean, streamlined news-reading experience.

The system is composed of two main components:

- **MCP Server** – The backend service responsible for article fetching, filtering, and summarization.
- **Strands Agent** – A frontend agent that interacts with the MCP server and provides a user-friendly interface.

---

## 📁 Project Structure

```plaintext
news-curator-agent/
├── mcp/              # Core server and processing logic
│   ├── server/       # API endpoints and server logic
│   └── ...
├── agent/            # Streamlit frontend agent
│   └── ...
├── README.md         # Project documentation
└── ...
```


## 🚀 Getting Started
### 🧰 Prerequisites
### Make sure the following are installed:
- **Python 3.8+**
- **uv**
- **Git**


### 🖥️ Running the Project Locally

Run the **MCP Server** and the **Agent Interface** in separate terminals.

---

#### 1️⃣ Start the MCP Server

In the first terminal:

```bash
cd mcp
uv pip install .
python server/server.py
```

#### 2️⃣ Start the Agent Interface
In the second terminal:

```bash
cd agent
uv pip install .
python run_streamlit.py
```





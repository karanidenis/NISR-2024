from langflow.load import run_flow_from_json
TWEAKS = {
  "File-qQAPE": {
    "path": "q2_data.csv",
    "concurrency_multithreading": 4,
    "silent_errors": False,
    "use_multithreading": False
  },
  "ParseData-VsMNm": {
    "sep": "\n",
    "template": "{text}"
  },
  "Prompt-rnEjU": {
    "template": "{document}\n\n{text}",
    "document": "",
    "text": ""
  },
  "ChatInput-qw1LG": {
    "files": "",
    "background_color": "",
    "chat_icon": "",
    "input_value": "is education a key factor in employment rates?",
    "sender": "User",
    "sender_name": "User",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "ChatOutput-GDQD2": {
    "background_color": "",
    "chat_icon": "",
    "data_template": "{text}",
    "input_value": "",
    "sender": "Machine",
    "sender_name": "AI",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "OllamaModel-SrhMw": {
    "base_url": "http://localhost:11434",
    "format": "",
    "input_value": "",
    "metadata": {},
    "mirostat": "Disabled",
    "mirostat_eta": None,
    "mirostat_tau": None,
    "model_name": "llama3:latest",
    "num_ctx": None,
    "num_gpu": None,
    "num_thread": None,
    "repeat_last_n": None,
    "repeat_penalty": None,
    "stop_tokens": "",
    "stream": False,
    "system": "",
    "system_message": "",
    "tags": "",
    "temperature": 0.2,
    "template": "",
    "tfs_z": None,
    "timeout": None,
    "top_k": None,
    "top_p": None,
    "verbose": False
  }
}

result = run_flow_from_json(flow="nisr_flow.json",
                            session_id="", # provide a session id if you want to use session state
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)
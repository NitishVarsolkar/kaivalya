from langflow.load import run_flow_from_json
TWEAKS = {
  "ChatInput-BSosG": {},
  "ParseData-6DmrF": {},
  "Prompt-FNc44": {},
  "SplitText-D9iG0": {},
  "ChatOutput-AETGh": {},
  "AstraDB-W6ZwW": {},
  "AstraDB-jAmS3": {},
  "File-vjBMU": {},
  "Google Generative AI Embeddings-fCs7j": {},
  "Google Generative AI Embeddings-BvXnX": {},
  "GoogleGenerativeAIModel-bWKX2": {}
}

result = run_flow_from_json(flow="Vector Store RAG.json",
                            input_value="message",
                            session_id="", # provide a session id if you want to use session state
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)
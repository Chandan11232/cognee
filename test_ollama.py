import os
import logging

# 1. Force Python to show warnings on the console
logging.basicConfig(level=logging.WARNING)

# 2. Simulate setting an unvalidated model AND the required dummy credentials
os.environ["LLM_PROVIDER"] = "ollama"
os.environ["LLM_MODEL"] = "qwen2.5"
os.environ["LLM_ENDPOINT"] = "http://localhost:11434"
os.environ["LLM_API_KEY"] = "fake_key_for_testing"

# Also pass dummy embedding credentials just in case the secondary validator checks them
os.environ["EMBEDDING_PROVIDER"] = "ollama"
os.environ["EMBEDDING_MODEL"] = "nomic-embed-text"
os.environ["EMBEDDING_DIMENSIONS"] = "768"

from cognee.infrastructure.llm.config import get_llm_config

# 3. Trigger initialization/validation
print("--- Triggering Cognee Config Validation ---")
config = get_llm_config()
print("--- Check finished ---")

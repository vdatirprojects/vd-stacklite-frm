from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")





from ai_modules.llm_interfaces.openai_interface import LangChainOpenAIInterface


llm = LangChainOpenAIInterface().get_llm_chat_client()
print("LLM Client:", llm.invoke("Hello, how are you?"))

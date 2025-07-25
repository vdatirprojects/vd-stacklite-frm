from ai_modules.llm_interfaces.openai_interface import LangChainOpenAIInterface



llm = LangChainOpenAIInterface().get_llm_chat_client()
print("LLM Client:", llm.invoke("Hello, how are you?"))
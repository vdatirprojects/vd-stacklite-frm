from utils.logger import get_logger
import os
from langchain_openai import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings

logger = get_logger(__name__)


class LangChainOpenAIInterface:
    def __init__(self, openai_api_key: str = None):
        if "OPENAI_API_KEY" in os.environ:
            logger.warning("OPENAI_API_KEY is set in environment variables, using it instead of the provided key.")
            openai_api_key = os.environ["OPENAI_API_KEY"]   
            self.openai_api_key = openai_api_key
        else:
            self.openai_api_key = openai_api_key

    def get_llm_chat_client(self, model_name="gpt-4o-mini", temperature=0.0, **kwargs) -> ChatOpenAI:
        try:
            llm_client = ChatOpenAI(
                model=model_name,
                api_key= self.openai_api_key,
                temperature=temperature,
                **kwargs
            )

            logger.info(f"LangChainOpenAIInterface initialized with model: {model_name}")
            return llm_client
    
        except Exception as e:
            logger.exception(f"Failed to initialize LangChainOpenAIInterface: {e}")
            raise

    def get_embeddings_client(self, model_name="text-embedding-ada-002", **kwargs) -> OpenAIEmbeddings:
        try:
            embeddings_client = OpenAIEmbeddings(
                model=model_name,
                api_key=self.openai_api_key,
                **kwargs
            )

            logger.info(f"OpenAI Embeddings client initialized with model: {model_name}")
            return embeddings_client

        except Exception as e:
            logger.exception(f"Failed to initialize OpenAI Embeddings client: {e}")
            raise
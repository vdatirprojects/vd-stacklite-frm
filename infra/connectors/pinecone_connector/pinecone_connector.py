
from utils.logger import get_logger

logger = get_logger(__name__)


class PineconeConnector:
    def __init__(self, api_key: str):
        """
        Initializes the Pinecone connector with API key and environment.
        """
        self.api_key = api_key
        logger.debug(f"PineconeConnector initialized with environment")



if __name__ == "__main__":
    pass
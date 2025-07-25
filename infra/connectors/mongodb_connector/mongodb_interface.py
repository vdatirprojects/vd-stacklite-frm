from pymongo import MongoClient
from utils.logger import get_logger

logger = get_logger(__name__)


class MongoDbConnector:
    def __init__(self, mongo_uri: str, mongo_config: dict):
        self.uri = mongo_uri
        self.database_name = mongo_config["database"]

    def __enter__(self):
        """
        Open the connection to MongoDB.
        """
        logger.info("Mongodb Connector Opened...!!")
        self.client = MongoClient(self.uri)
        self.db_handle = self.client[self.database_name]
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Close the connection to MongoDB.
        """
        if self.client:
            self.client.close()
            logger.info("Mongodb Connector Closed...!!")

    def create_collection(self, collection_name):
        try:
            collecton = self.db_handle[collection_name]
            logger.info(f"{collection_name} Collection created")
            return collecton

        except Exception as e:
            logger.exception(f"Error in create_collection operation : {e}")

    def create_view(self, view_name: str, base_collection: str, pipeline: list):
        try:
            view = self.db_handle.create_collection(
                view_name, viewOn=base_collection, pipeline=pipeline
            )
            logger.info(f"{view_name} View created")
            return view

        except Exception as e:
            logger.exception(f"Error in create_view operation : {e}")

    def select(self, collection_name: str, query: dict):
        try:
            query = query or {}
            return list(self.db_handle[collection_name].find(query))

        except Exception as e:
            logger.exception(f"Error in select operation : {e}")

    def insert(self, collection_name: str, documents):
        """
        Insert a single document or multiple documents into a collection.
        """
        try:
            if isinstance(documents, list):
                result = self.db_handle[collection_name].insert_many(documents)
                logger.info(
                    f"{len(result.inserted_ids)} documents inserted successfully."
                )
                return result.inserted_ids
            else:
                result = self.db_handle[collection_name].insert_one(documents)
                logger.info("1 document inserted successfully.")
                return result.inserted_id
        except Exception as e:
            logger.exception(f"Error in insert operation: {e}")

    def delete(self, collection_name: str, query: dict):
        """
        Delete documents from a collection matching the query.
        """
        try:
            result = self.db_handle[collection_name].delete_many(query)
            logger.info(f"{result.deleted_count} documents deleted successfully.")
            return result.deleted_count
        except Exception as e:
            logger.exception(f"Error in delete operation: {e}")

    def update(
        self,
        collection_name: str,
        query: dict,
        update_values: dict,
        upsert: bool = False,
    ):
        """
        Update documents in a collection matching the query with the specified values.
        """
        try:
            result = self.db_handle[collection_name].update_many(
                query, {"$set": update_values}, upsert=upsert
            )
            logger.info(f"{result.modified_count} documents updated successfully.")
            return result.modified_count
        except Exception as e:
            logger.exception(f"Error in update operation: {e}")

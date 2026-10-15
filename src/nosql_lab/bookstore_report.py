#!/usr/bin/env python3

import logging
import os

from pymongo import MongoClient


MONGODB_ATLAS_URL = os.getenv("MONGODB_ATLAS_URL")
MONGODB_ATLAS_USER = os.getenv("MONGODB_ATLAS_USER")
MONGODB_ATLAS_PWD = os.getenv("MONGODB_ATLAS_PWD")

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


AUTHOR_IDS = ["author_002", "author_003", "author_004"]


def main():
    """Connect to Atlas and print every book for each author in AUTHOR_IDS."""
    try:
        client = MongoClient(
            MONGODB_ATLAS_URL,
            username=MONGODB_ATLAS_USER,
            password=MONGODB_ATLAS_PWD,
        )
        client.admin.command("ping")  # it fails here if the connection is bad

        logging.info("Connected to MongoDB Atlas")

        db = client["bookstore"]

        authors = db["authors"]

        books = db["books"]
        
        count = authors.count_documents({"_id": {"$in": AUTHOR_IDS}})

        print(f"Authors: {count}\n")

    
        for author in authors.find({"_id": {"$in": AUTHOR_IDS}}):
            print(author["name"])
            for book in books.find({"author_ids": author["_id"]}):
                print(f"  {book['title']} ({book['published_year']})")
            print()

        client.close()
        logging.info("Connection closed")
    except Exception as e:
        logging.error("MongoDB error: %s", e)


if __name__ == "__main__":
    main()
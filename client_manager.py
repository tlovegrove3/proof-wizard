"""
Author: Terry Lovegrove
File: client_manager.py
Date written: 10/13/2024
Purpose: This module allows for loading, adding and removing clients from a json list
of clients.

"""

import json
import os


class ClientManager:
    """This class allows for adding or removing clients from a list of clients."""

    def __init__(self, json_file="clients.json"):
        self.json_file = json_file
        self.clients = self.load_clients()

    def load_clients(self):
        """Loads the list of clients from the JSON file."""
        if not os.path.exists(self.json_file):
            return []
        try:
            with open(self.json_file, "r", encoding="utf-8") as file:
                clients = json.load(file)
                return clients
        except json.JSONDecodeError:
            print(
                f"Error: Could not decode JSON from {self.json_file}. Starting with an empty list."
            )
            return []

    def save_clients(self):
        """Saves the list of clients to the JSON file."""
        with open(self.json_file, "w", encoding="utf-8") as file:
            json.dump(self.clients, file, indent=4)

    def add_client(self, client_name):
        """Adds a new client to the list if it doesn't already exist."""
        if client_name not in self.clients:
            self.clients.append(client_name)
            self.clients.sort()  # Keep the list sorted
            self.save_clients()
            return f"Client '{client_name}' added."
        return f"Client '{client_name}' already exists."

    def remove_client(self, client_name):
        """Removes a client from the list if it exists."""
        if client_name in self.clients:
            self.clients.remove(client_name)
            self.save_clients()
            return f"Client '{client_name}' removed."
        return f"Client '{client_name}' not found."

    def get_clients(self):
        """Returns the list of clients."""
        return self.clients

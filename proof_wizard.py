"""
Author: Terry Lovegrove
File: Proof_Wizard.py
Date written: 9/29/2024
Assignment: Final Project (tkinter gui)
Purpose: GUI program that allows a user to select from a list of clients to generate
a proof. It will allow for selection of a few different proof types. It will also
allow to complete pending proofs.It uses ttkbootstrap for styling, so ttkbootstrap
will need to be pip installed if that is ok.

"""

import os
import tkinter as tk
from tkinter import ttk

# pip install ttkbootstrap for the below module to work
from ttkbootstrap import Style


class ProofWizard(tk.Tk):
    """This is a tkinter module for generating proofs."""

    def __init__(self):
        super().__init__()
        self.style = Style(theme="solar")
        self.title("Proof Wizard")
        self.geometry("600x300")

        # not sure if I want this turned on or not but leaving off for now.
        # self.grid_rowconfigure(0, weight=1)  # Allow the first row to expand
        # self.grid_columnconfigure(0, weight=1)  # Allow the first column to expand

        # Create a ttk Notebook for setting up multiple tabs
        self.nb = ttk.Notebook(self)
        self.nb.grid(row=0, column=0, sticky="nsew")

        # Create main frame for the "Main Proofs" tab
        self.frm_main = ttk.Frame(self.nb)
        self.nb.add(self.frm_main, text="Proof Setup")

        # Create completed frame for the "Completed Proofs" tab
        self.frm_completed = ttk.Frame(self.nb)
        self.nb.add(self.frm_completed, text="Completed Proofs")

        # Get username from OS
        self.current_user = self.get_current_user()
        self.clients = self.load_clients()  # Placeholder for client data
        self.proofs = self.load_proofs()  # Placeholder for proofs

        # Setting up the tabs
        self.setup_main_widgets()
        self.setup_completed_widgets()

    def setup_main_widgets(self):
        """Creating widgets for the main tab."""

        # Username label
        self.lbl_user = ttk.Label(self.frm_main, text="User: " + self.current_user)
        self.lbl_user.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Client label
        self.lbl_client = ttk.Label(self.frm_main, text="Select Client:")
        self.lbl_client.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        # Dropdown of client list
        self.combo_client = ttk.Combobox(self.frm_main, values=self.clients)
        self.combo_client.grid(row=3, column=1, padx=10, pady=10)

        # Proof type label
        self.lbl_proof_type = ttk.Label(self.frm_main, text="Select Proof Type:")
        self.lbl_proof_type.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        # Proof type dropdown
        self.proof_type_field = ttk.Combobox(
            self.frm_main, values=["Generic", "Approval"]
        )
        self.box_proof_type.grid(row=4, column=1, padx=10, pady=10)

        # Button to generate proofs
        self.btn_make_proof = ttk.Button(
            self.frm_main, text="Make Proof", command=self.make_proof
        )
        self.btn_make_proof.grid(
            row=5, column=1, columnspan=1, padx=10, pady=10, sticky="e"
        )

        # Exit button to close application
        self.btn_exit = ttk.Button(self.frm_main, text="Exit", command=self.quit)
        self.btn_exit.grid(row=6, column=1, columnspan=1, padx=10, pady=10, sticky="e")

        # Create a dropdown to select themes
        self.lbl_theme = ttk.Label(self.frm_main, text="Select Theme:")
        self.lbl_theme.grid(row=0, column=5, padx=10, pady=10)

        # Get the current theme
        self.theme_var = tk.StringVar(value=self.style.theme_use())

        # Setup theme dropdown and set the values
        self.combo_theme = ttk.Combobox(self.frm_main, textvariable=self.theme_var)
        self.combo_theme["values"] = self.style.theme_names()
        self.combo_theme.grid(row=0, column=6, padx=10, pady=10)

        # Bind the combo selection event to the change_theme method
        self.combo_theme.bind("<<ComboboxSelected>>", self.change_theme)

    def setup_completed_widgets(self):
        """Sets up widgets for the completed proofs tab"""
        lbl = ttk.Label(self.frm_completed, text="Completed Proofs")
        lbl.grid(row=0, column=0, columnspan=1, pady=10)
        for proof in self.proofs:
            if proof["status"] == "Complete":
                ttk.Label(
                    self.frm_completed,
                    text=f"{proof['client']}: {proof['proof_type']}",
                ).grid()

    def change_theme(self, event):
        """Changes the theme of the application based on the dropdown selection."""
        selected_theme = (
            self.theme_var.get()  # Get the selected theme from the dropdown
        )
        self.style.theme_use(selected_theme)  # Apply the selected theme

    def make_proof(self):
        """Proof function"""
        client = self.combo_client.get()
        proof_type = self.proof_type_field.get()
        # Code to generate proof goes here
        print(f"Generated proof for {client} ({proof_type})")

    def load_clients(self):
        """Loads the list of clients."""
        return ["Acme Corporation", "Global Tech"]

    def load_proofs(self):
        """Loads the list of proofs"""
        return [
            {
                "client": "Acme Corporation",
                "proof_type": "Approval",
                "status": "Complete",
            }
        ]

    def get_current_user(self):
        """Gets the current username running the program."""
        user = os.getlogin()
        return user


if __name__ == "__main__":
    app = ProofWizard()
    app.mainloop()

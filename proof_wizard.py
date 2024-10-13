"""
Author: Terry Lovegrove
File: Proof_Wizard.py
Date written: 10/13/2024
Assignment: Final Project (tkinter gui)
Purpose: GUI program that allows a user to select from a list of clients to generate
a proof. It will allow for selection of a few different proof types. It will also
allow to complete pending proofs.It uses ttkbootstrap for styling, so ttkbootstrap
will need to be pip installed if that is ok.

"""

import datetime
import json
import os
import tkinter as tk
from tkinter import PhotoImage, ttk

from ttkbootstrap import Style


class ProofWizard(tk.Tk):
    """This is a tkinter module for generating proofs."""

    def __init__(self):
        super().__init__()
        self.style = Style(theme="solar")
        self.title("Proof Wizard")
        self.geometry("1025x450")
        self.minsize(1025, 450)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.icon_image = PhotoImage(file="images/icon.png")
        self.iconphoto(False, self.icon_image)

        # Create a ttk Notebook for setting up multiple tabs
        self.nb = ttk.Notebook(self)
        self.nb.grid(row=0, column=0, sticky="nsew")

        # Create main frame for the "Main Proofs" tab
        self.frm_main = ttk.Frame(self.nb)
        self.nb.add(self.frm_main, text="Proof Setup")

        # Create completed frame for the "Completed Proofs" tab
        self.frm_completed = ttk.Frame(self.nb)
        self.nb.add(self.frm_completed, text="Completed Proofs")

        # Add the Instructions frame
        self.frm_instructions = ttk.Frame(self.nb)
        self.nb.add(self.frm_instructions, text="Instructions")

        # Create a custom style for the Treeview
        self.style.configure("Treeview", borderwidth=1)
        # self.style.map("Treeview", background=[("selected", "darkblue")])

        # Get username from OS
        self.current_user = self.get_current_user()
        self.clients = self.load_clients()
        self.pending_proofs = self.load_json("pending.json")
        self.completed_proofs = self.load_json("completed.json")

        # Sort state tracking
        self.pending_sort_order = {
            "date_created": False,
            "created_by": False,
            "client": False,
        }
        self.completed_sort_order = {
            "date_created": False,
            "created_by": False,
            "client": False,
            "date_completed": False,
            "completed_by": False,
        }

        # Setting up the tabs
        self.setup_frm_instructions()
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
        self.box_proof_type = ttk.Combobox(
            self.frm_main, values=["Generic", "Approval"]
        )
        self.box_proof_type.grid(row=4, column=1, padx=10, pady=10)

        # Button to generate proofs
        self.btn_make_proof = ttk.Button(
            self.frm_main, text="Generate Proof", command=self.make_proof
        )
        self.btn_make_proof.grid(
            row=5, column=1, columnspan=1, padx=10, pady=10, sticky="e"
        )

        # Get the current theme
        self.theme_var = tk.StringVar(value=self.style.theme_use())

        # Setup theme dropdown and set the values
        self.combo_theme = ttk.Combobox(self.frm_main, textvariable=self.theme_var)
        self.combo_theme["values"] = self.style.theme_names()
        self.combo_theme.grid(row=0, column=3, padx=10, pady=10, sticky="e")

        # Exit button to close application
        self.btn_exit = ttk.Button(self.frm_main, text="Exit", command=self.quit)
        self.btn_exit.grid(row=6, column=1, columnspan=1, padx=10, pady=10)

        # Treeview for pending approvals
        self.pending_tree = ttk.Treeview(
            self.frm_main,
            columns=("Date Created", "Created By", "Client"),
            show="headings",
            # style="Treeview",
        )
        self.pending_tree.grid(
            row=3, column=3, rowspan=3, padx=10, pady=10, sticky="nsew"
        )
        self.pending_tree.heading(
            "Date Created",
            text="Date Created",
            command=lambda: self.sort_pending("date_created"),
        )
        self.pending_tree.heading(
            "Created By",
            text="Created By",
            command=lambda: self.sort_pending("created_by"),
        )
        self.pending_tree.heading(
            "Client", text="Client", command=lambda: self.sort_pending("client")
        )
        # Bind the combo selection event to the change_theme method
        self.combo_theme.bind("<<ComboboxSelected>>", self.change_theme)

        # Load pending proofs into the treeview
        self.load_pending_proofs()

        # Mark Complete button
        self.btn_mark_complete = ttk.Button(
            self.frm_main, text="Mark Complete", command=self.mark_proof_complete
        )
        self.btn_mark_complete.grid(row=6, column=3, padx=10, pady=10, sticky="e")

    def setup_frm_instructions(self):
        """Create a label for the instructions heading"""
        # Load the logo image (adjust path to your logo)
        self.logo_image = PhotoImage(file="images/logo.png")

        # Create a label to display the logo
        logo_label = tk.Label(self.frm_instructions, image=self.logo_image)
        logo_label.pack(pady=10)

        instructions_heading = tk.Label(
            self.frm_instructions,
            text="How to Use Proof Wizard",
            font=("Arial", 14, "bold"),
        )
        instructions_heading.pack(pady=10)

        # Create a text widget to hold the instructions
        instructions_text = tk.Text(
            self.frm_instructions, wrap="word", height=20, width=75
        )
        instructions_text.pack(padx=10, pady=10)

        instructions_content = (
            "Welcome to the Proof Wizard! Here are the instructions for using the application:\n\n"
            "1. Pending Proofs Tab: View and manage all proofs that are still in progress. "
            "You can select a proof and update its status or view more details.\n\n"
            "2. Completed Proofs Tab: This tab displays proofs that have been completed. "
            "You can review completed proofs here.\n\n"
            "3. Archiving Proofs: Select one or more completed proofs to archive them if the list becomes too long. "
            "Archived proofs are saved to a separate file for future reference.\n\n"
            "4. Exit: Use the 'Exit' button to close the application safely.\n\n"
            "5. Theme: Use the 'Theme' option to change the appearance of the application.\n\n"
            "For any further assistance, please refer to the user manual or contact support."
        )

        # Insert the instructions content into the text widget and disable editing
        instructions_text.insert("1.0", instructions_content)
        instructions_text.config(state="disabled")

    def setup_completed_widgets(self):
        """Sets up widgets for the completed proofs tab"""
        lbl = ttk.Label(self.frm_completed, text="Completed Proofs")
        lbl.grid(row=0, column=0, columnspan=1, pady=10)
        # Treeview for completed proofs
        self.completed_tree = ttk.Treeview(
            self.frm_completed,
            columns=(
                "Date Created",
                "Created By",
                "Client",
                "Date Completed",
                "Completed By",
            ),
            show="headings",
            style="Treeview",
        )
        # Vertical scrollbar for completed tree
        self.completed_scrollbar = ttk.Scrollbar(
            self.frm_completed, orient="vertical", command=self.completed_tree.yview
        )
        self.completed_tree.configure(yscrollcommand=self.completed_scrollbar.set)

        # Place the treeview and scrollbar using grid
        self.completed_tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.completed_scrollbar.grid(row=1, column=2, sticky="ns")

        self.completed_tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.completed_tree.heading(
            "Date Created",
            text="Date Created",
            command=lambda: self.sort_completed("date_created"),
        )
        self.completed_tree.heading(
            "Created By",
            text="Created By",
            command=lambda: self.sort_completed("created_by"),
        )
        self.completed_tree.heading(
            "Client",
            text="Client",
            command=lambda: self.sort_completed("client"),
        )
        self.completed_tree.heading(
            "Date Completed",
            text="Date Completed",
            command=lambda: self.sort_completed("date_completed"),
        )
        self.completed_tree.heading(
            "Completed By",
            text="Completed By",
            command=lambda: self.sort_completed("completed_by"),
        )

        self.load_completed_proofs()

    def load_json(self, filename):
        """Load JSON data from a file."""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_json(self, data, filename):
        """Save JSON data to a file."""
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def make_proof(self):
        """Generates a proof and adds it to pending or completed JSON files."""
        client = self.combo_client.get()
        proof_type = self.box_proof_type.get()

        # Get current datetime
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_proof = {
            "client": client,
            "proof_type": proof_type,
            "created_by": self.current_user,
            "date_created": current_datetime,
        }

        if proof_type == "Approval":
            self.pending_proofs.append(new_proof)
            self.save_json(self.pending_proofs, "pending.json")
            self.load_pending_proofs()
        else:
            new_proof["date_completed"] = current_datetime
            new_proof["completed_by"] = self.current_user
            self.completed_proofs.append(new_proof)
            self.save_json(self.completed_proofs, "completed.json")
            self.load_completed_proofs()

    def change_theme(self, selected_theme):
        """Changes the theme of the application based on the dropdown selection."""
        selected_theme = self.theme_var.get()
        self.style.theme_use(selected_theme)

    def load_pending_proofs(self):
        """Load pending proofs into the treeview."""
        for item in self.pending_tree.get_children():
            self.pending_tree.delete(item)
        for proof in sorted(
            self.pending_proofs,
            key=lambda x: x["date_created"],
            reverse=self.pending_sort_order["date_created"],
        ):
            self.pending_tree.insert(
                "",
                "end",
                values=(proof["date_created"], proof["created_by"], proof["client"]),
            )

    def load_completed_proofs(self):
        """Load completed proofs into the treeview."""
        for item in self.completed_tree.get_children():
            self.completed_tree.delete(item)
        for proof in self.completed_proofs:
            self.completed_tree.insert(
                "",
                "end",
                values=(
                    proof["date_created"],
                    proof["created_by"],
                    proof["client"],
                    proof["date_completed"],
                    proof["completed_by"],
                ),
            )

    def mark_proof_complete(self):
        """Marks selected pending proofs as complete."""
        selected_items = self.pending_tree.selection()

        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for item in selected_items:
            proof_values = self.pending_tree.item(item, "values")
            for proof in self.pending_proofs:
                if (
                    proof["date_created"],
                    proof["created_by"],
                    proof["client"],
                ) == proof_values:
                    proof["date_completed"] = current_datetime
                    proof["completed_by"] = self.current_user
                    self.completed_proofs.append(proof)
                    self.pending_proofs.remove(proof)
                    break
        self.save_json(self.pending_proofs, "pending.json")
        self.save_json(self.completed_proofs, "completed.json")
        self.load_pending_proofs()
        self.load_completed_proofs()

    def get_current_user(self):
        """Get the current user name."""
        return os.getlogin()

    def load_clients(self):
        """Loads client list from the clients.json file."""
        try:
            with open("clients.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def sort_pending(self, column):
        """Sorts pending proofs based on the selected column."""
        self.pending_sort_order[column] = not self.pending_sort_order[column]
        self.pending_proofs.sort(
            key=lambda x: x[column], reverse=self.pending_sort_order[column]
        )
        self.load_pending_proofs()

    def sort_completed(self, column):
        """Sorts completed proofs based on the selected column."""
        self.completed_sort_order[column] = not self.completed_sort_order[column]
        self.completed_proofs.sort(
            key=lambda x: x[column], reverse=self.completed_sort_order[column]
        )
        self.load_completed_proofs()


if __name__ == "__main__":
    app = ProofWizard()
    app.mainloop()

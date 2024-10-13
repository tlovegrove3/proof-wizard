# Welcome to Proof Wizard

## You Must Install ttkbootstrap Before Running

ttkbootstrap is used for the modern styling themes.

## What Can This GUI Do?

Proof Wizard is a Python-based GUI project using `tkinter`. It is currently a project for school, but I am hoping to use it as a tool at work for generating and tracking proofs.
To get started, start the app and go to the Instructions tab for details on how to operate.
Features included:

- Choose a theme from a theme dropdown.
- Generates and manages proofs for a client-based system.
- Username shows on the main page.
  - Username is also shown on created and completed proof items.
- Dropdown list for selecting clients.
- Dropdown list for proof selecting proof types.
- A `Generate Proof` button.
- A `Mark Complete` button.
- A working `Exit` button.
- Utilizes JSON files for storing the list pending proofs, and completed proofs.
- Selecting from the `Pending Proofs` list and marking as complete will remove them from
that list and add them to the `Completed Proofs` list.
  - Both pending and completed lists can be sorted by any of the columns in descending
  or ascending order by clicking on the column headers.
- Management of clients is handled by a separate a "client_manager.py" module with a "ClientManager" class for loading, creating, and removing clients.
- The "Clients" tab allows you to see the list of clients
  - The "Add Client" button in the clients tab calls the "add_client" method from
  "ClientManager" to handle the details of adding a client. If no data is entered
  in the input box, a message box will pop up to handle the empty input.
  - The "Remove Client" button calls the "remove_client" method from the
  "ClientManager" module. A message box will pop up to confirm the action.
  - Buttons include error handling and message box confirmations of actions.

## Problems and Next Steps

- Improve error handling and input validation for a smoother user experience.
- Add an archive feature. The user will be able to select from the completed list
which files to archive. They will be removed from the completed list and added to the
archive list.
- Add ability to cancel a pending proof.
- Next steps are to add integration with production system to allow for triggering
proof generation.

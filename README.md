# Welcome to Proof Wizard

Proof Wizard is a Python-based GUI project using `tkinter`. It is currently a project for school, but I am hoping to use it as a tool at work for generating and tracking proofs for various clients.

## What I’ve Completed

- A working GUI with 3 tabs, each with configured widgets.
- Modern default styling, with a dropdown for users to select other styles.
- Dropdown list for clients.
- Dropdown list for proof types.
- A `Generate Proof` button.
- A working `Exit` button.
- Utilizing JSON files for storing the list of clients, pending proofs, and completed proofs.
- Selecting from the pending list and marking as complete will remove them from that list
and add them to the completed list.
- Active username displays in the window.
- Username is shown on created and completed proofs.
- Added icon in the upper left of the main window.
- Added logo image to the instructions tab.
- Both pending and completed lists can be sorted by any of the columns in descending
or ascending order by clicking on the column headers.

## Problems and Next Steps

- Improve error handling and input validation for a smoother user experience.
- Add an archive feature. The user will be able to select from the completed list
which files to archive. They will be removed from the completed list and added to the
archive list.

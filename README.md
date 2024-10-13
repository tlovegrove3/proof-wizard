# Welcome to Proof Wizard

Proof Wizard is a Python-based GUI project using `tkinter`. It is currently a project for school, but I am hoping to use it as a tool at work for generating and tracking proofs for various clients.

## What I’ve Completed

- A working GUI with 2 tabs, each with configured widgets.
- Modern default styling, with a dropdown for users to select other styles.
- Dropdown list for clients.
- Dropdown list for proof types.
- A `Generate Proof` button.
- A working `Exit` button.

## Problems and Next Steps

- Utilize JSON files for storing the list of clients, proof types, and completed proofs. Currently, the data is hardcoded.
- Update the `generate proof` function to add the result to the JSON list instead of just using `print()`. The Completed Proofs tab will display this updated list.
- Consider adding a third tab for Pending Proofs or include a Pending Proofs list on the main tab to reduce tab switching.
- Add error handling and input validation for a smoother user experience.
- Implement functionality to select a pending proof from the list and mark it as complete, moving it from the Pending list to the Completed list.
- Add “Created By” and “Last Modified By” attributes to each proof, including optional creation and completion date/time.
- Explore how to incorporate images into the application.

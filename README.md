<h2>Welcome to Proof Wizard</h2>
<p>This is a python based GUI project using tkinter.</p>
<p>It is currently a project for school, but I am hoping to use it as a tool at work for generating and tracking proofs for various clients.</p>
<H3>What I’ve Completed</H3>
<ul>
  <li>I have a working GUI with 2 tabs, each with widgets configured.</li>
  <li>The styling has a more modern default style, but the user has a dropdown to select from to choose from other styles.</li>
  <li>I have a dropdown list of clients.</li>
  <li>I have another dropdown list for proof types.</li>
  <li>I have a Generate Proof button.</li>
  <li>I have working Exit button.</li>
</ul>
<h3>Problems and Next Steps</h3>
<ul>
  <li>I want to utilize json files for the list of clients, the proof types, and the completed proofs. Currently, the data is being hardcoded in the program.</li>
  <li>Currently the generate proof function is just doing a print() of the result. I will add that to the json list instead and the Completed Proofs tab will display the updated list.</li>
  <li>I think it makes sense to either create a third tab for Pending Proofs or add a Pending Proofs list to the main tab. I’m currently thinking about adding it to the main tab so there is less clicking between tabs.</li>
  <li>I need to add some error handling and input validation to help ensure a smooth experience.</li>
  <li>For the Pending Proofs, I need to add the functionality to select a pending proof from the list and mark as complete, which will cause it to be removed from the Pending list and into the Complete list.</li>
  <li>I want to add a “Created By” and “Last Modified By” attribute to each proof so that we know who initialized and who completed the proof. Possibly add a creation date/time and completion date/time too.</li>
  <li>I need to figure out how to incorporate images.</li>
</ul>

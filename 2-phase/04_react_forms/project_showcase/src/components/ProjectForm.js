import { useState } from "react"

/* 
  * => Vanilla js
  ! => REACT
  - submit event
    * document.getElementById("form-name").addEventListener("submit")
    ! onSubmit on the form element
  - preventDefault
    * e.preventDefault()
    ! e.preventDefault()
  - take the value of the input(s)
    * form.querySelector("find-input").value for all inputs
    ! inputs need to be in STATE
    ! React BUILDS the formdata as we fill it out
	- create DOM elements and attach to the page
		* docu.createElement OR innerHTML thing
		! modify state of the projects to include the new thing!
			- Push(Append) => setState([...prevState, newObj])
			- Unshift(Prepend) => setState([newObj, ...prevState])
			- Remove => setState(prevState.filter(x => x !=== something))
			- Update => setState(prevState.map(x => when x is the element to update, update))
  - to persist: 
    * Send a POST request to our server
    * With the BODY as all the input values

*/
const ProjectForm = ({ setProjectState }) => {
	const [nameInput, setName] = useState("")
	const [aboutInput, setAbout] = useState("")
	const [phaseInput, setPhase] = useState("0")
	const [linkInput, setLink] = useState("")
	const [screenShootInput, setScreenShot] = useState("")

	const handleNameChange = (e) => {
		// IF YOU NEED TO DO MORE THAN ONE SIMPLE THING
		setName(e.target.value)
	}

	const handleAboutChange = (e) => setAbout(e.target.value)

	const handleDropDown = (e) => {
		// console.log(e.target.value.split(" ")[1])
		// console.log(e.target.value)
		setPhase(e.target.value)
	}

	const handleSubmit = (e) => {
		e.preventDefault()

		// Match our formData from state into the format of our backend data
		const newProjData = {
			name: nameInput,
			about: aboutInput,
			phase: Number(phaseInput),
			link: linkInput,
			image: screenShootInput,
		}
		console.log(newProjData)
		// console.log(projectState)
		// ! Can't push (or do array modification methods) on state to trigger a re-render!
		// projectState.push(newProjData)
		setProjectState((prevProjects) => {
			return [...prevProjects, newProjData]
		})
		// debugger
		// Put this obj on the page!
		// <ProjectListItem project={newProjectData} />
	}

	return (
		<section>
			<form className="form" autoComplete="off" onSubmit={handleSubmit}>
				<h3>Add New Project</h3>

				<label htmlFor="name">Name</label>
				<input
					type="text"
					id="name"
					name="name"
					value={nameInput}
					onChange={handleNameChange}
				/>

				<label htmlFor="about">About</label>
				<textarea
					id="about"
					name="about"
					// value={aboutInput}
					onChange={handleAboutChange}
				/>

				<label htmlFor="phase">Phase</label>
				<select name="phase" id="phase" onChange={handleDropDown}>
					<option value="0">Select One</option>
					<option value="1">Phase 1 - JS</option>
					<option value="2">Phase 2 - React</option>
					<option value="3">Phase 3 - Python</option>
					<option value="4">Phase 4 - Flask</option>
					<option value="5">Phase 5 - Capstone</option>
				</select>

				<label htmlFor="link">Project Homepage</label>
				<input
					type="text"
					id="link"
					name="link"
					onChange={(e) => setLink(e.target.value)}
				/>

				<label htmlFor="image">Screenshot</label>
				<input
					type="text"
					id="image"
					name="image"
					onChange={(e) => setScreenShot(e.target.value)}
				/>

				<button type="submit">Add Project</button>
			</form>
		</section>
	)
}

export default ProjectForm

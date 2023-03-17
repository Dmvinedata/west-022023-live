import { useState } from "react"

const ProjectFormState = ({ setProjectState }) => {
	// const [nameInput, setName] = useState("")
	// const [aboutInput, setAbout] = useState("")
	// const [phaseInput, setPhase] = useState("0")
	// const [linkInput, setLink] = useState("")
	// const [screenShootInput, setScreenShot] = useState("")

	const [formState, setFormState] = useState({
		name: "",
		about: "",
		phase: 0,
		link: "",
		image: "",
	})

	// Can destructure to clean up dot notation if you want
	const { name, about, phase, link, image } = formState

	const handleNameChange = (e) => {
		// setName(e.target.value)
		// Now we need to update the FORMSTATE, but only the name key
		setFormState((prevFormState) => {
			// in Vanilla JS
			// * prevFormState.name = e.target.value
			return { ...prevFormState, name: e.target.value }
		})
		// setFormState({ ...formState, name: e.target.value })
	}

	const handleAboutChange = (e) => {
		setFormState({ ...formState, about: e.target.value })
	}

	const handleAnyChange = (e) => {
		// set the 'name' (or an attribute of your choosing, but choose name) html attribute to the KEYS of the formState
		setFormState({ ...formState, [e.target.name]: e.target.value })
	}

	const handleSubmit = (e) => {
		e.preventDefault()

		// Match our formData from state into the format of our backend data

		const newProjData = { ...formState, phase: Number(phase) }
		setProjectState((prevProjects) => {
			return [...prevProjects, newProjData]
			// return [...prevProjects, formState]
		})
	}

	return (
		<section>
			<form className="form" autoComplete="off" onSubmit={handleSubmit}>
				<h3>Add New Project</h3>

				<label htmlFor="name">Name</label>
				<input
					type="text"
					id="name"
					// name="names"
					name="name"
					value={formState.name}
					onChange={handleAnyChange}
				/>

				<label htmlFor="about">About</label>
				<textarea
					id="about"
					name="about"
					value={about}
					onChange={handleAnyChange}
				/>

				<label htmlFor="phase">Phase</label>
				<select name="phase" id="phase" onChange={handleAnyChange}>
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
					value={link}
					name="link"
					onChange={handleAnyChange}
				/>

				<label htmlFor="image">Screenshot</label>
				<input
					type="text"
					id="image"
					name="image"
					value={image}
					onChange={handleAnyChange}
				/>

				<button type="submit">Add Project</button>
			</form>
		</section>
	)
}

export default ProjectFormState

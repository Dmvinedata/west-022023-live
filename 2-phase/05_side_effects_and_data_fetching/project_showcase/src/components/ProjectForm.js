import { useState } from "react"

const ProjectForm = ({ setProjects, projects }) => {
	const [formState, setState] = useState({
		name: "",
		about: "",
		phase: "0",
		link: "",
		image: "",
		// image_url: "",
	})
	const { name, about, phase, link, image } = formState

	const handleChange = (e) => {
		setState({ ...formState, [e.target.name]: e.target.value })
	}

	const handleSubmit = (e) => {
		e.preventDefault()
		console.log(formState)
		// ! POST REQUEST

		const postReqobj = {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({ ...formState, phase: Number(phase) }),
			// body: JSON.stringify(formState),
		}
		console.log(postReqobj)

		// ! Optimism...
		// setProjects((prevStateProjects) => [...prevStateProjects, formState])

		fetch("http://localhost:4000/projects", postReqobj)
			.then((res) => res.json())
			.then((newProject) => {
				console.log(newProject)
				// Set the state of the projects here!
				// How do we PUSH into state
				// setProjects([...projects, newProject])
				setProjects((prevStateProjects) => [...prevStateProjects, newProject])
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
					name="name"
					onChange={handleChange}
					value={name}
				/>

				<label htmlFor="about">About</label>
				<textarea
					id="about"
					name="about"
					onChange={handleChange}
					value={about}
				/>

				<label htmlFor="phase">Phase</label>
				<select
					name="phase"
					id="phase"
					onChange={handleChange}
					value={formState.phase}
				>
					<option value="0">Select One</option>
					<option value="1">Phase 1</option>
					<option value="2">Phase 2</option>
					<option value="3">Phase 3</option>
					<option value="4">Phase 4</option>
					<option value="5">Phase 5</option>
				</select>

				<label htmlFor="link">Project Homepage</label>
				<input
					type="text"
					id="link"
					name="link"
					onChange={handleChange}
					value={link}
				/>

				<label htmlFor="image">Screenshot</label>
				<input
					type="text"
					id="image"
					name="image"
					onChange={handleChange}
					value={image}
				/>

				<button type="submit">Add Project</button>
			</form>
		</section>
	)
}

export default ProjectForm

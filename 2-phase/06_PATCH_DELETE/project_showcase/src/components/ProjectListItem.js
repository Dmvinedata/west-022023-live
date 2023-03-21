import { useState } from "react"
import { FaPencilAlt, FaTrash } from "react-icons/fa"

const ProjectListItem = ({
	project,
	enterProjectEditModeFor,
	setProjectId,
	setProjects,
}) => {
	const { id, image, about, name, link, phase, claps } = project

	// const [clapCount, setClapCount] = useState(0)

	const handleClap = () => {
		fetch(`http://localhost:4000/projects/${id}`, {
			method: "PATCH",
			headers: {
				"Content-Type": "application/json",
			},
			// PUT needs the whole object
			// body: JSON.stringify({ ...project, claps: clapCount + 1 }),
			body: JSON.stringify({ claps: !!claps ? claps + 1 : 1 }),
		})
			.then((res) => res.json())
			.then((updatedWithClaps) => {
				console.log(updatedWithClaps)
				// setClapCount(clapCount + 1)
				// setClapCount(updatedWithClaps.claps)
				setProjects((prevProj) =>
					prevProj.map((proj) =>
						proj.id === updatedWithClaps.id ? updatedWithClaps : proj
					)
				)
        // * Probably should pass down the updating function
        // onUpdatedProject(updatedWithClaps)
			})
	}

	const handleEditClick = () => {
		setProjectId(id)
	}

	const handleDeleteClick = () => {
		fetch(`http://localhost:4000/projects/${id}`, {
			method: "DELETE",
		})
    // .then(res => res.json()) // Unneed on DELETE unless, you are getting data back from the server, which can't happen in json-server
    .then((data) => {
			console.log(data)
			// IF req is a success then what?...
			// Remove the current id proj from state ALLLL THE WAY IN APP....
			setProjects((prevProj) => {
				return prevProj.filter((proj) => proj.id !== id)
			})
      // onDeletedProject(id)
		})
	}

	return (
		<li className="card">
			<figure className="image">
				<img src={image} alt={name} />
				<button onClick={handleClap} className="claps">
					👏{!!claps ? claps : 0}
				</button>
			</figure>

			<section className="details">
				<h4>{name}</h4>
				<p>{about}</p>
				{link ? (
					<p>
						<a href={link}>Link</a>
					</p>
				) : null}
			</section>

			<footer className="extra">
				<span className="badge blue">Phase {phase}</span>
				<div className="manage">
					<button onClick={() => setProjectId(id)}>
						<FaPencilAlt />
					</button>
					<button onClick={handleDeleteClick}>
						<FaTrash />
					</button>
				</div>
			</footer>
		</li>
	)
}

export default ProjectListItem

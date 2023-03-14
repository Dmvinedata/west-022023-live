import { useState } from "react"

import ProjectCard from "./ProjectCard"
import projects from "../projects"

function ProjectList() {
	const [searchQuery, setSearchQuery] = useState("")
	const [other, setOther] = useState("here")

	const renderedProjects = () => {
		return filteredProjects().map((project) => {
			return (
				<ProjectCard key={project.id} project={project} otherFunc={otherFunc} />
			)
		})
	}

	// const otherFunc = () => {
	function otherFunc() {
		console.log(this)
	}

	const filteredProjects = () => {
		return projects.filter((project) => {
			return project.name.toLowerCase().includes(searchQuery.toLowerCase())
		})
	}

	const handleSearchChange = (event) => {
		// console.log(event.target.value)
		// console.log(searchQuery)
		setSearchQuery(event.target.value)
		// console.log(searchQuery)
	}

	return (
		<section>
			<h2 onMouseOver={() => console.log(this)}>Projects</h2>

			<div className="filter">
				<button>All</button>
				<button>Phase 5</button>
				<button>Phase 4</button>
				<button>Phase 3</button>
				<button>Phase 2</button>
				<button>Phase 1</button>
			</div>
			<input
				type="text"
				placeholder="Search..."
				value={searchQuery} // Pessimistic inputs
				onChange={handleSearchChange}
			/>

			<ul className="cards">{renderedProjects()}</ul>
		</section>
	)
}

export default ProjectList

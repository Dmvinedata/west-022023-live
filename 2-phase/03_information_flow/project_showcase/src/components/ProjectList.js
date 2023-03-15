import ProjectListItem from "./ProjectListItem"
import { useState } from "react"

// import projects from '../projects.js'

const ProjectList = ({ projects, searchQuery, setSearchQuery }) => {
	// const [searchQuery, setSearchQuery] = useState("")
	// const [projects, setProjects] = useState([])

	// const searchResults = () => {
	// 	return projects.filter((project) => {
	// 		return project.name.toLowerCase().includes(searchQuery.toLowerCase())
	// 	})
	// }

	const projectListItems = () => {
		return projects.map((project) => (
			<ProjectListItem key={project.id} {...project} />
		))
	}

	// const handleOnChange = (e) => {
	// 	setSearchQuery(e.target.value)
	// }

	return (
		<>
			{/* SearchInput */}
			<ul className="cards">{projectListItems()}</ul>
		</>
	)
}

/* 
	Project H2
	Project Filters
	SearchInput

*/

export default ProjectList

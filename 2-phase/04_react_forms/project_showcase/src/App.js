import { useState } from "react"

import Header from "./components/Header"
import ProjectForm from "./components/ProjectForm"
import ProjectList from "./components/ProjectList"
import SearchInput from "./components/SearchInput"
import PhaseFilters from "./components/PhaseFilters"

const App = () => {
	const [projectState, setProjectState] = useState([])
	const [isDarkMode, setIsDarkMode] = useState(true)
	const [searchQuery, setSearchQuery] = useState("")
	const [phase, setPhase] = useState(0)

	const handleLoadProjects = (e) => {
		fetch("http://localhost:4000/projects")
			.then((res) => res.json())
			.then(setProjectState)
	}

	const searchResults = () => {
		return filterPhase().filter((project) => {
			return project.name.toLowerCase().includes(searchQuery.toLowerCase())
		})
	}

	const filterPhase = () => {
		return phase === 0
			? projectState
			: projectState.filter((project) => project.phase === phase)
	}

	return (
		<div className="App">
			<Header
				isDarkMode={isDarkMode}
				setIsDarkMode={setIsDarkMode}
				firstProject={projectState[0]}
				searchQuery={searchQuery}
			/>
			<ProjectForm />
			<button onClick={handleLoadProjects}>Load Projects</button>

			<section>
				<h2>Projects</h2>
				<PhaseFilters setPhase={setPhase} />
				<SearchInput
					searchQuery={searchQuery}
					setSearchQuery={setSearchQuery}
				/>
				<ProjectList
					// projects={projectState} // Just pass ALL of the projects
					// projects={searchResults()} // pass the FILTERED projects
					projects={searchResults()} // pass FILTERED projects by PHASE
					// isDarkMode={isDarkMode}
					// searchQuery={searchQuery}
					// setSearchQuery={setSearchQuery}
				/>
			</section>
		</div>
	)
}

export default App

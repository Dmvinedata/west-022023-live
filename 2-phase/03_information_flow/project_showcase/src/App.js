import { useState } from "react"

import Header from "./components/Header"
import ProjectForm from "./components/ProjectForm"
import ProjectList from "./components/ProjectList"
import SearchInput from "./components/SearchInput"
import PhaseFilters from "./components/PhaseFilters"
/* 
  Warm up Questions!

  1. What is State?
    - useState is the hook
    - Dynamic attributes of a component, can be updated
    - When state is changed, triggers a re-render of the component AND the component tree (all of the children)

  2. What type of data is props?
    - Object, which means we can pass down any datatype as a key/value pair

  3. How is State updated/mutated?
    - setter function
    - const [stateVar, setterFunction] = useState(initalValue)
    if our state is a string, set the inital datatype to a string
  - const [someNumber, setSomeNumber] = useState(null)
  - const [someArray, setsomeArray] = useState(null)
    -two components down we use someArray.forEach
      - with the null, we will get an error
        - can use error handling tho..
      - empty array will just return nothing
  - PLEASE MATCH DATATYPES

*/
const App = () => {
	const [projectState, setProjectState] = useState([])
	const [isDarkMode, setIsDarkMode] = useState(true)
	const [searchQuery, setSearchQuery] = useState("")
	const [phase, setPhase] = useState(0)
	// const [phase, setPhase] = useState("all")

	const handleLoadProjects = (e) => {
		fetch("http://localhost:4000/projects")
			.then((res) => res.json())
			.then((allProjects) => {
				console.log(allProjects)
				setProjectState(allProjects)
			})
	}

	const searchResults = () => {
		return filterPhase().filter((project) => {
			return project.name.toLowerCase().includes(searchQuery.toLowerCase())
		})
	}

	const filterPhase = () => {
		// filter the projects by phase
		const phaseProjects = projectState.filter((project) => {
			if (phase === 0) return true
			return project.phase === phase
		})
		console.log({ phaseProjects })
		return phaseProjects
	}

	return (
		<div className="App">
			<Header
				isDarkMode={isDarkMode}
				setIsDarkMode={setIsDarkMode}
				firstProject={projectState[0]}
				searchQuery={searchQuery}
			/>
			{/* <ProjectForm /> */}
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

import { useEffect, useState } from "react"

import Header from "./components/Header"
import ProjectForm from "./components/ProjectForm"
import ProjectList from "./components/ProjectList"
import ProjectEditForm from "./components/ProjectEditForm"

/* 

  Warmup Questions

  1. What are the 3 phase fo the component lifecycle?
    - Mount / Update / Unmount
  
  2. Mounting useEffect?
    - Empty Dep array
  
  3. Unmounting useEffect?
    - Cleanup function
      - Timers, server connections, end of componenet data functionality

  useEffect(cbfunc, depArray)
  cbfunc = () => {
     return cleanup func() {}
  }

  4. How do we add to an array (.push) through state?
    - Push    =>  setState(prevState => [...prevState, newThing])
    - Unshift =>  setState(prevState => [newThing, ...prevState])
    - Pop     =>  setState(prevState => prevState.filter(conditionThatRemovesTheLast))
    - Update  =>  setState(prevState => prevState.map(changingThings))
    - Insert? => prevState.forEach(insert at location)

*/

const App = () => {
	const [isDarkMode, setIsDarkMode] = useState(true)
	const [projects, setProjects] = useState([])
	// * For the edit comp, will need the id of the project to update
	const [projectId, setProjectId] = useState(null)

	useEffect(() => {
		console.log("App Mounted")
		fetch("http://localhost:4000/projects")
			.then((resp) => resp.json())
			.then((projects) => setProjects(projects))
	}, [])

	const onToggleDarkMode = () => {
		setIsDarkMode((isDarkMode) => !isDarkMode)
	}

	const onAddProject = (newProj) => {
		setProjects((projects) => [...projects, newProj])
	}

	const onUpdatedProject = (updatedProj) => {
		setProjects((prevProj) => {
			return prevProj.map((proj) => {
				if (proj.id === updatedProj.id) {
					return updatedProj
				} else {
					return proj
				}
			})
		})

		// setProjects((prevProj) =>
		// 	prevProj.map((proj) => (proj.id === updatedProj.id ? updatedProj : proj))
		// )
	}

	const onDeletedProject = (id) => {
		setProjects((prevProj) => {
			return prevProj.filter((proj) => proj.id !== id)
		})
	}

	const completeEditing = () => {
		setProjectId(null)
	}

	const enterProjectEditModeFor = (projectId) => {
		setProjectId(projectId)
	}

	const renderForm = () => {
		if (projectId) {
			return (
				<ProjectEditForm
					projectId={projectId}
					completeEditing={completeEditing}
					onUpdatedProject={onUpdatedProject}
				/>
			)
		} else {
			return <ProjectForm onAddProject={onAddProject} />
		}
	}

	return (
		<div className={isDarkMode ? "App" : "App light"}>
			<Header isDarkMode={isDarkMode} onToggleDarkMode={onToggleDarkMode} />
			{renderForm()}
			<ProjectList
				projects={projects}
				// enterProjectEditModeFor={enterProjectEditModeFor}
				setProjectId={setProjectId}
				setProjects={setProjects}
			/>
		</div>
	)
}

export default App

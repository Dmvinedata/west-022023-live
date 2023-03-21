import React, { useState, useEffect } from "react"
import Header from "./components/Header"
import ProjectForm from "./components/ProjectForm"
import ProjectList from "./components/ProjectList"

/* 

  Warm Up Questions!

  1. What is RESTful Routing?
    - Convention for organizing urls, routes, 
      - INDEX   GET  /somethings
      - SHOW    GET ONE THING /somethings/:id
      - CREATE  POST      /somethings
      - UPDATE  PATCH     /somethings/:id
      - DELETE  DELETE    /somethings/:id

  2. How do we lift state?
    - Move state to the parent and pass down as props

  3. What is a Controlled Form?
    - Every input on the form is in State 
    - AND the value of the inputs is taken PESSIMISTICALLY from our state
      - as simple as adding the value={valueFromState} on the <input />
    - Helps with making sure that the state is 100% accurate 

*/

/* 

  ! The Component LifeCycle

  - What happens before, during, and after the comp renders

  3 phases of a comp lifecycle
    1. Mounting
      - Everything that happens when the comp is put on the page
    2. Updating
      - while the comp is rendered, any changes to the comp
    3. Unmounting
      - What happens once the comp unrenders
      - Cleanup

    USEEFFECT HOOK

*/

const App = () => {
	const [projects, setProjects] = useState([])
	const [isDarkMode, setIsDarkMode] = useState(true)

	// useEffect(cbFunc, dependecies)
	// * Without a dependency array, this useEffect will run whenever there is ANY change to state on this component
	useEffect(() => {
		// This is where we define what this effect does
		console.log("hi, I will trigger on EVERY SINGLE STATE CHANGE")
		// ! DO NOT PUT CONTINUOUS LOOPS, FETCH REQUESTS
		// * DO PUT DEBUGGING CONSOLELOGS
	})

	// ! DON'T have this AMIBOUS Console.log, instead put it in an  useEffect Hook
	// // console.log(projects)

	// * EMPTY DEP ARRAY
	// ! COMPONENTDIDMOUNT
	// Check the dependecy array to trigger the hook
	// By the dep array being empty, that means that it will only run once on the mount
	useEffect(() => {
		console.log("Component Did Mount...")
		// * For initial fetches
		// * For any outside additional data
		fetchAllProjects()

		return function cleanup() {
			// ! Will only run is the entire APP unmounts
			console.log("ATTEMPT TO UNMOUNT")
		}
	}, [])

	useEffect(() => {
		// Only run when the state of the darkMode changes
		console.log({ isDarkMode })
		return () => {
			console.log("CLEANING UP DARKMODE")
		}
	}, [isDarkMode])

	// ! DO NOT CHANGE SET STATE INSIDE OF UNCONTROLLED USEEFFECT
	// useEffect(() => {
	// 	setIsDarkMode(!isDarkMode)
	// })

	const fetchAllProjects = () => {
		fetch("http://localhost:4000/projects")
			.then((res) => res.json())
			.then((projects) => setProjects(projects))
	}

	const onToggleDarkMode = () => setIsDarkMode(!isDarkMode)

	// * RENDERING FUNCTION
	return (
		<div className={isDarkMode ? "App" : "App light"}>
			<Header isDarkMode={isDarkMode} onToggleDarkMode={onToggleDarkMode} />
			<ProjectForm setProjects={setProjects} projects={projects} />
			{/* <button onClick={handleClick}>Load Projects</button> */}
			<ProjectList projects={projects} />
		</div>
	)
}

export default App

import { useState, useEffect } from "react"

import Header from "./components/Header"
import ProjectForm from "./components/ProjectForm"
import ProjectList from "./components/ProjectList"
import ProjectEditForm from "./components/ProjectEditForm"
import ProjectPage from "./components/ProjectPage"
import Home from "./components/Home"

import { Switch, Route } from "react-router-dom"

/* 

  Warmup Questions!

  1. what are the 2 arguments of the useEffect hook?
    - callback function that returns a cleanup function, dep Array

  2. What's the return of the useState hook?
    - returns an array of [stateVariable, setterFunc]
    - const [state, setState] = useState(initialState)
*/

/*  
  Server Side vs client side routing..
    Server Side 
      => RESTful routing (highly highly encouraged)
      => json-server (emulating a database)
      => database APIs, flask, python
    Client Side 
      => RESTful could be nice.
      => URLs that the user will probably see on the front end!
      => Based on the given URL, will render the correct html (vanilla) or components(react)
      => With Client Side Routing in react, are we still dealing with a Single Page App? YES!
        => Why? Still just ONE html file
      Benefits
        => Could help with performance
        => Can Navigate directly to the frontend endpoints

*/

const App = () => {
	const [isDarkMode, setIsDarkMode] = useState(true)
	const [projects, setProjects] = useState([])

	useEffect(() => {
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

	const onUpdateProject = (updatedProj) => {
		const updatedProjects = projects.map((ogProject) => {
			if (ogProject.id === updatedProj.id) {
				return updatedProj
			} else {
				return ogProject
			}
		})
		setProjects(updatedProjects)
	}

	const onDeleteProject = (deletedProj) => {
		const updatedProjects = projects.filter(
			(project) => project.id !== deletedProj.id
		)
		setProjects(updatedProjects)
	}

	/* 
    In V5 Route Component Declartion?
    routeProps => {location, history, match}
    1. Wrap the comp around the 2 sided Route
      <Route path=''>
        <MyComponent compProps={compProps}/>
      </Route>
        => Will just pass the compProps, will NOT pass the routeProps
    2. If you have NO compProps
      <Route path='' component={MyComp} />
        => Will pass all the RouteProps to the comp
    3. If you have compProps AND need the RouteProps
      <Route path='' render={(routeProps) => <MyComponent compProps={compProps} {...routeProps} />} />
  */

	/* 
    In V6 Route Comp Declaration
    1. <Route path='' element={<MyComp compProps={compProps} />}
      => Will automatically pass down all the routeProps
  */

	/* 
    v5                => v6
    Switch            => Routes
    Route render={cb} => Route element={<MyComp />}
    useHistory()      => useNavigate()
    nestingRoutes...  => <Outlet />
      
  */

	return (
		<div className={isDarkMode ? "App" : "App light"}>
			{/* NAVBR COMPONENT */}
			<Header isDarkMode={isDarkMode} onToggleDarkMode={onToggleDarkMode} />
			<Switch>
				{/* The Switch (Routesv6) will look through these routes until it finds the FIRST to satisfy the path contdition */}
				{/* "/projects".includes('/') */}
				{/* Either use 'exact' OR move the routes in Specific -> non-specific order */}

				<Route path="/projects/edit">
					<ProjectEditForm onUpdateProject={onUpdateProject} />
				</Route>
				<Route path="/projects/new">
					<ProjectForm onAddProject={onAddProject} />
				</Route>
				{/* IN V6 */}
				{/* <Route path="projects" element={<ProjectList projects={projects} />}  */}
				<Route
					path="/projects"
					render={(routeProps) => {
						return (
							<ProjectList
								projects={projects}
								onDeleteProject={onDeleteProject}
								{...routeProps}
							/>
						)
					}}
				/>
				{/* <Route path="/projects">
					<ProjectList projects={projects} onDeleteProject={onDeleteProject} />
				</Route> */}
				<Route path="/" component={Home} />
				{/* <Route path="/">
					<Home />
				</Route> */}
			</Switch>
		</div>
	)
}

export default App

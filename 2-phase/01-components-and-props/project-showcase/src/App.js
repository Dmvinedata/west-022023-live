import logo from "./logo.svg"
import "./App.css"
import Header from "./Header.js"
import Form from "./Form.js"
import ProjectList from "./ProjectList"
import projects from "./projects.js"
// import otherLogo from "../../../../../../public/logo192.png"

console.log("OUTSIDE")
const App = () => {
	console.log("INSIDE")
	return (
		<div>
			{/* <header>PROJECTS</header> */}
			{/* Create a HEADER component */}
			<Header />
			{/* ANY JAVASCRIPT INSIDE OF THE RETURN MUST BE IN CURLY BRACKETS */}
			{/* {1 + 1} */}
			{/* {projects[0].name} */}
			{/* "projects[0].name" */}
			{/* <form>
				<input type="text" placeholder="name" />
				<input type="submit" value="SUBMIT" />
			</form> */}
			<Form />
			{/* a list of all the projects from the projects.js file */}
			{/* <div id="project-list">
				<div>
					<h1>Great Outdoors Guide</h1>
					<p>Plan your next adventure to in the U.S. National Parks!</p>
				</div>
			</div> */}
			<ProjectList projectsArray={projects} />
		</div>
	)
}

export default App

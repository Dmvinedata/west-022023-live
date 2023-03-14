import React from "react"
import ProjectListItem from "./ProjectListItem"

const ProjectList = (props) => {
	const defFuncHere = () => {
		alert("WAOW")
	}
	const mappedProjects = () => {
		return props.projectsArray.map((project) => {
			return (
				<ProjectListItem
					// Pass down just the FIRST element in the projects array?
					wholeProjObj={project}
					name={project.name}
					about={project.about}
					imageUrl={project.image}
				/>
			)
		})
	}

	return (
		<div id="project-list">
			{/* a list of all the projects from the projects.js file */}
			{/* PASSING DOWN Props is just a KEY and VALUE pair */}
			{/* <ProjectListItem
				coolProp="hi"
				jsProp={1 + 1}
				funcProps={() => console.log("WAOW")}
				otherfuncProps={defFuncHere}
			/> */}

			{/*  */}
			{/* <ProjectListItem
				// Pass down just the FIRST element in the projects array?
				wholeProjObj={props.projectsArray[0]}
				name={props.projectsArray[0].name}
				about={props.projectsArray[0].about}
				imageUrl={props.projectsArray[0].image}
			/> */}
			{/* {props.projectsArray.forEach((project) => { */}
			{props.projectsArray.map((project) => {
				return (
					<ProjectListItem
						// Pass down just the FIRST element in the projects array?
						wholeProjObj={project}
						key={project.id}
						name={project.name}
						about={project.about}
						imageUrl={project.image}
					/>
				)
			})}

			{/* {mappedProjects()} */}
		</div>
	)
}
export default ProjectList

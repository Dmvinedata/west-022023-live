import React from "react"

import Header from "./components/Header"
import ProjectForm from "./components/ProjectForm"
import ProjectList from "./components/ProjectList"

/* 
  Warm Up Questions!

  1. What is a prop(s)?
    - Properties
    - Object that is passed from parent component to children components

  2. How are props passed?
    - <Header name={"some name"}/>

  3. How are props caught/collected in the child component?
    - Arguments in the component function
    - const Header = (props) => {}
    - props.name

*/

/* 
  1. What is state?
    - Attributes that can change assigned to a component
    - can still pass State as props, but as a prop, it won't change

  2. What happen if we Change State?
    - Triggers a Re-Render of all the components that are connected to that

*/

/* 
  Destructuring is JS

  ARRAYS:
  arr = [1,2,3]
  x = arr[0], y = arr[1], z = arr[2]
  IS THE SAME AS 
  const [x, y, z] = arr

  OBJECTS
  props = {name: "bill", job: "SE"}
  const name = props.name
  const job = props.job
  OR
  const {name, job} = props
  * WHEN DESTRUCTING AN OBJ, THE KEYS HAVE TO MATCH EXACTLY

*/

function App() {
	return (
		<div className="App">
			<Header />
			{/* <ProjectForm /> */}
			<ProjectList />
		</div>
	)
}

export default App

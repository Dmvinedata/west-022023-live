// import React, { useState } from "react"
// Import ALLLL of React
import { useState } from "react"
// Here we just grab the useState hook

function Header() {
	// const [stateVariable, setterFunction] = useState(initialState)
	// setterFunction(newState)
	// setterFunction(prevState => returns newState)
	const [isDarkMode, setIsDarkMode] = useState(true)
	// const [isLightMode, setIsLightMode] = useState(false)

	const toggleMode = (event) => {
		// isDarkMode = false
		console.log(isDarkMode)
		console.log(setIsDarkMode)
		// in order to Change the state, it has to run through the SETTER function
		setIsDarkMode(!isDarkMode)
		// set with the NEW value to overwrite
		// OR
		// a Callback function with the Previous State
		// setIsDarkMode((previousState) => {
		// 	console.log({ previousState })
		// 	return false
		// })
	}

	const buttonValue = () => {
		if (isDarkMode) {
			return "Dark Mode is func"
		} else {
			return "Light Mode in func"
		}
	}

	return (
		<header>
			<h1>
				<span className="logo">{"//"}</span>
				Project Showcase
			</h1>
			<nav>
				{/* <button onClick={() => setIsDarkMode(!isDarkMode)}> */}
				<button onClick={toggleMode}>
					{/* {isDarkMode ? "Dark Mode" : "Light Mode"} */}
					{buttonValue()}
				</button>
			</nav>
		</header>
	)
}

export default Header

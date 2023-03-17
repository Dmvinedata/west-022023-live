import React from "react"

const Header = (props) => {
	const handleClick = () => {
		props.setIsDarkMode(!props.isDarkMode)
	}

	const buttonTextContent = props.isDarkMode ? "Light Mode" : "Dark Mode"

	return (
		<header>
			<h1>
				<span className="logo">{"//"}</span>
				Project Showcase
			</h1>
			<p>{!!props.firstProject ? props.firstProject.name : null}</p>
			<h3>What ya searching??? {props.searchQuery}</h3>
			<button onClick={handleClick}>{buttonTextContent}</button>
		</header>
	)
}

export default Header

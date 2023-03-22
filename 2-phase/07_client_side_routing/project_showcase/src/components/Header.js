import React from "react"
import { Link, NavLink } from "react-router-dom"

const Header = ({ isDarkMode, onToggleDarkMode }) => {
	const buttonTextContent = isDarkMode ? "Light Mode" : "Dark Mode"

	return (
		<header>
			<nav>
				<Link to="/">
					<h1 className="branding">
						<span className="logo">{"//"}</span>
						Project Showcase
					</h1>
				</Link>

				<div className="navigation">
					<NavLink to="/projects" className="button">
						All Projects
					</NavLink>
					<NavLink to="/projects/new" className="button">
						Add Project
					</NavLink>
					<button onClick={onToggleDarkMode}>{buttonTextContent}</button>
				</div>
			</nav>
		</header>
	)
}

export default Header

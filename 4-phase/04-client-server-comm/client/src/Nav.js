import React from "react"
import { NavLink } from "react-router-dom"

const Nav = () => {
	return (
		<div>
			<NavLink to="/">Home</NavLink>
			<NavLink to="/songs">All Songs</NavLink>
			<NavLink to="/songs/new">Create a Song</NavLink>
		</div>
	)
}

export default Nav

import React from "react"

const Song = ({ song: { title, genre, length, plays, id } }) => {
	return (
		<div>
			<h2>
				{title} : {length}
			</h2>
			<h2>{genre}</h2>
			<p>{plays}</p>
		</div>
	)
}

export default Song

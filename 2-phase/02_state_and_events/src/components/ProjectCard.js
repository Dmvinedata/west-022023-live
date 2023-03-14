import { useState } from "react"

// function ProjectCard(props) {
// const {project} = props
function ProjectCard({ project, otherFunc }) {
	const { image, name, about, link, phase } = project

	const [clapCount, setClapCount] = useState(0)

	const handleClaps = (event) => {
		// when we click on the claps, increase the state by 1
		console.log("first: ", clapCount)
		const newClaps = clapCount + 1
		setClapCount(newClaps)
		// setClapCount(clapCount + 1)
		// ! SETTER FUNCTIONS ARE ASYNCHRONOUS
		// BECAUSE:
		// React will batch setState calls inside of React based event handlers to reduce component re-renders
		console.log("second: ", clapCount)
		console.log("third: ", newClaps)
	}

	const handleMouseOver = (e) => {
		otherFunc()
	}
	return (
		<li className="card">
			<figure className="image">
				{/* <img src={props.project.image} alt={props.project.name} /> */}
				<img
					src={image}
					alt={name}
					onMouseOver={handleMouseOver}
					onClick={(e) => console.log(e.target)}
				/>
				<button className="claps" onClick={handleClaps}>
					👏{clapCount}
				</button>
			</figure>

			<section className="details">
				<h4>{name}</h4>
				<p>{about}</p>
				{link ? (
					<p>
						<a href={link}>Link</a>
					</p>
				) : null}
			</section>

			<footer className="extra">
				<span className="badge blue">Phase {phase}</span>
			</footer>
		</li>
	)
}

export default ProjectCard

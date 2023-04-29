import { useEffect, useState } from "react"
import { useParams } from "react-router-dom"

const SongShow = () => {
	const { id } = useParams()
	const [displaySong, setSong] = useState({})

	useEffect(() => {
		fetch(`/songs/${id}`)
			.then((res) => res.json())
			.then((songData) => {
				console.log({ songData })
				setSong(songData)
			})
	}, [])
	return (
		<div>
			<h1>{displaySong.title}</h1>
			<h1>{displaySong.genre}</h1>
			<h1>{displaySong.length}</h1>
			<h1>{displaySong.plays}</h1>
		</div>
	)
}

export default SongShow

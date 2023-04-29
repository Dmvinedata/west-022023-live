import "./App.css"
import { useEffect, useState } from "react"
import { Routes, Route } from "react-router-dom"
import SongContainer from "./SongContainer"
import Nav from "./Nav"
import SongShow from "./SongShow"
import NewSongForm from "./NewSongForm"

function App() {
	const [songs, setSongs] = useState([])

	useEffect(() => {
		fetch("/songs")
			.then((res) => res.json())
			.then((songData) => {
				console.log(songData)
				setSongs(songData)
			})
	}, [])

	const addSong = (songData) => {
		const postReqObj = {
			method: "POST",
			headers: {
				"content-type": "application/json",
			},
			body: JSON.stringify(songData),
		}
		fetch("/songs", postReqObj)
			.then((res) => res.json())
			.then((newSong) => {
				if (newSong["message"]) {
					alert(newSong["message"])
				} else {
					setSongs((prevSongs) => [newSong, ...prevSongs])
				}
			})
			.catch((err) => console.log(err))
	}

	return (
		<div className="App">
			<h1>Cool Song App</h1>
			<Nav />
			<Routes>
				<Route path="/songs" element={<SongContainer songs={songs} />} />
				<Route path="/songs/:id" element={<SongShow />} />
				<Route path="/songs/new" element={<NewSongForm addSong={addSong} />} />
			</Routes>
		</div>
	)
}

export default App

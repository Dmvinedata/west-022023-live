import React from "react"
import Song from "./Song"

const SongContainer = ({ songs }) => {
	const mappedSongs = () =>
		songs.map((song) => <Song song={song} key={song.id} />)
	return <div>{mappedSongs()}</div>
}

export default SongContainer

import { useState } from "react"

const NewSongForm = ({addSong}) => {
	const [formData, setFormData] = useState({
		title: "",
		genre: "",
		length: 0,
	})

	const handleChange = (e) => {
		setFormData((prevState) => {
			return {
				...prevState,
				[e.target.name]: e.target.value,
			}
		})
	}

	const handleSubmit = (e) => {
		e.preventDefault()
		console.log(formData)
    addSong(formData)
	}
	return (
		<div>
			<h1>CREATE YOUR SONG</h1>
			<form onSubmit={handleSubmit}>
				<input
					placeholder="title"
					name="title"
					value={formData.title}
					onChange={handleChange}
				/>
				<input
					placeholder="genre"
					name="genre"
					value={formData.genre}
					onChange={handleChange}
				/>
				<br />
				<label>
					Length:
					<input
						placeholder="length"
						name="length"
						type="number"
						value={formData.length}
						onChange={handleChange}
					/>
				</label>
				<br />
				<input type="submit" value="Add your Song!" />
			</form>
		</div>
	)
}

export default NewSongForm

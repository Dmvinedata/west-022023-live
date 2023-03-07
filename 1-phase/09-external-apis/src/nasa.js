const NASA_URL = "https://api.nasa.gov"
const nasaContainer = document.getElementById("nasa-container")



const apod = () => {
	fetch(`${NASA_URL}/planetary/apod?api_key=${api_key}`)
		.then((res) => res.json())
		.then((apodData) => {
			console.log(apodData.service_version)
			renderApod(apodData)
		})
}

const renderApod = (apodData) => {
	const div = document.createElement("div")
	const img = document.createElement("img")
	const p = document.createElement("p")
	const title = document.createElement("h2")

	title.textContent = apodData.title
	img.src = apodData.hdurl
	img.alt = apodData.title
	p.textContent = apodData.explanation

	div.append(title, img, p)
	nasaContainer.append(div)
}

const mars = () => {
	fetch(
		`${NASA_URL}/mars-photos/api/v1/rovers/curiosity/photos?api_key=${api_key}&sol=2`
	)
		.then((res) => res.json())
		.then((marsData) => {
			console.log(marsData)
			marsData.photos.forEach((photo) => {
				renderOneMarsPhoto(photo)
			})
		})
}

const renderOneMarsPhoto = (photoData) => {
	// img_src / earth_date / camera.full_name
	const container = document.createElement("div")
	const img = document.createElement("img")
	const h2 = document.createElement("h2")
	const pCamera = document.createElement("p")

	img.src = photoData.img_src
	img.alt = photoData.earth_date
	h2.textContent = photoData.earth_date
	pCamera.textContent = photoData.camera.full_name

	container.append(h2, img, pCamera)
	nasaContainer.append(container)
}

document.getElementById("apod-btn").addEventListener("click", apod)
document.getElementById("mars-btn").addEventListener("click", mars)

console.log(otherSecret)


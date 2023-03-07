const LOTR_URL = "https://the-one-api.dev/v2/"

const getAllLOTRCharacters = () => {
	const getAuthObj = {
		method: "GET",
		headers: {
			"Content-type": "application/json",
			Authorization: `Bearer ${lotr_api_key}`,
		},
	}

	fetch(LOTR_URL + "books", getAuthObj)
		.then((res) => res.json())
		.then((lotrData) => {
			console.log(lotrData)
		})
}


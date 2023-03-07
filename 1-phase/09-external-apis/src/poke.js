// Code Here 👀

/* 
	Warm Up Questions

	1. What is an API?
		- Application Programming Interface?
		- What does it mean?
			- How we interact with a database


	2. What is the difference between a local API and an external API?
		- Local/Owned/Internal
			- An API that YOU have FULL CONTROL OF THE DATA
		- External
			- Limited Control of the data, not owned by you
			- Can potentially have WRITE access (POST / PATCH / DELETE)


*/

const BASE_URL = "https://pokeapi.co/api/v2/"
const ENDPOINTS = {
	pokemon: "pokemon",
	ability: "ability",
	berry: "berry",
}

const getPokemonByName = (pokeName) => {
	fetch(`${BASE_URL}${ENDPOINTS.pokemon}/${pokeName}`)
		.then((res) => res.json())
		.then((pokeObj) => {
			console.log(pokeObj)
			// do something with sprites/id/name/types
			renderPokeCard(pokeObj)
		})
		.catch((err) => console.log(err))
}

const renderPokeCard = (pokeObj) => {
	let pokeCard = `
		<div>
			<h1>${pokeObj.name}</h1>
			<h3>${pokeObj.id}</h3>
			<img src=${pokeObj.sprites.front_shiny} alt=${pokeObj.name}>
		</div>
	`
	document.getElementById("poke-container").innerHTML += pokeCard
}

const searchForPokemonByName = (event) => {
	event.preventDefault()
	console.log(event.target.search.value)
	getPokemonByName(event.target.search.value)
}

const getAbilityByName = (abilityName) => {
	fetch(`${BASE_URL}ability/${addDashes(abilityName)}`)
		.then((res) => res.json())
		.then((abilityObj) => {
			console.log(abilityObj)
			// renderPokeCard(abilityObj)
		})
		.catch((err) => console.log(err))
}

const addDashes = (str) => {
	return str.split(" ").join("-")
}

const searchForAbilityByName = (event) => {
	event.preventDefault()
	getAbilityByName(event.target["ability-search"].value)
}

const init = () => {
	document
		.getElementById("poke-search")
		.addEventListener("submit", searchForPokemonByName)
	document
		.getElementById("ability-search")
		.addEventListener("submit", searchForAbilityByName)
}

init()

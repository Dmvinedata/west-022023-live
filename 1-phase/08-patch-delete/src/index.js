/* 
    ! PATCH and DELETE Requests!

    Review Questions!

    1. What is the difference between PUT and PATCH?\
			ex in the db{
				id: 1, name: "james", job: "dev"
			}
			request body: {name: "derrick"}
			- PUT? 			Updates ALL the elements
			- PATCH? 		Update only the requested elements
		
		2. What is the route/url/path for patch and deletes?
			index => /books
			patch => /books/:id
			delete => /books/:id

*/

// ! GLOBAL VARIABLES
const BASE_URL = "http://localhost:3000/books/"

// ! IMPORTANT GLOBAL DOM ELEMENTS
const bookList = document.getElementById("book-list")
const bookForm = document.getElementById("book-form")

const fetchAllBooks = () => {
	fetch(BASE_URL)
		.then((response) => response.json())
		.then((books) => {
			clearList()
			books.forEach((book) => {
				renderOneBook(book)
			})
		})
}

const clearList = () => {
	bookList.innerHTML = ""
}

const renderOneBook = (book) => {
	const li = document.createElement("li")
	const h3 = document.createElement("h3")
	const pAuthor = document.createElement("p")
	const pPrice = document.createElement("p")
	const img = document.createElement("img")
	// create an INPUT field
	const inventoryInput = document.createElement("input")
	inventoryInput.type = "number"
	// inventoryInput.placeholder = "Please Enter your input"
	inventoryInput.value = book.inventory
	const pInventory = document.createElement("p")
	pInventory.textContent = book.inventory

	h3.textContent = book.title
	pAuthor.textContent = `Author: ${book.author}`
	pPrice.textContent = `$${book.price}`

	img.src = book.imageUrl
	li.className = "list-li"
	li.id = `book-${book.id}`

	const deleteBtn = document.createElement("button")
	deleteBtn.textContent = "DELETE"

	inventoryInput.addEventListener("change", (e) => {
		// updateBook(newInvValue, bookID)
		// pInventory.textContent = e.target.value
		updateBook(e.target.value, book.id, pInventory)
	})

	deleteBtn.addEventListener("click", (e) => {
		// * OPTIMISTIC REMOVAL
		// li.remove()
		// ! For PESSIMISTIC, we need to pass in something that can point us to the liContainer
		// can be the EVENT, LI, etc...
		// deleteBook(book.id, li)
		deleteBook(book.id, e)
	})

	li.append(deleteBtn, h3, pAuthor, pPrice, pInventory, inventoryInput, img)
	bookList.append(li)
}

const handleForm = (event) => {
	event.preventDefault()
	const newBookObj = {
		title: event.target.title.value,
		author: event.target.author.value,
		price: Number(event.target.price.value),
		imageUrl: event.target.imageUrl.value,
		inventory: parseInt(event.target.inventory.value),
		reviews: [],
	}
	createBook(newBookObj)
}

const hideForm = (e) => {
	if (e.target.textContent === "Hide Form") {
		bookForm.parent.hidden = true
		e.target.textContent = "Show Form"
	} else {
		bookForm.hidden = false
		e.target.textContent = "Hide Form"
	}
}

const createBook = (bookObjToAdd) => {
	const postReqObj = {
		method: "POST",
		headers: {
			"Content-type": "application/json",
		},
		body: JSON.stringify(bookObjToAdd),
	}
	fetch(BASE_URL, postReqObj)
		.then((response) => response.json())
		.then((newBook) => {
			renderOneBook(newBook)
		})
		.catch((err) => console.log(err))
}

// ! NEW STUFFF

const updateBook = (newInventoryValue, bookID, inventoryElement) => {
	console.log(newInventoryValue, bookID)

	const patchReqObj = {
		method: "PATCH",
		headers: {
			"Content-Type": "application/json",
			Accept: "application/json",
		},
		body: JSON.stringify({
			inventory: newInventoryValue,
		}),
	}

	fetch(BASE_URL + bookID, patchReqObj)
		.then((res) => res.json())
		.then((updatedBookObj) => {
			// console.log(updatedBookObj)
			// console.log(inventoryElement)
			inventoryElement.textContent = updatedBookObj.inventory
		})
}

const deleteBook = (bookID) => {
	console.log("DELETING!", bookID)
	// debugger
	fetch(BASE_URL + bookID, {
		method: "DELETE",
	})
		// we don't always need to parse to json because the delete response from the json-server is always an empty object
		// // .then((res) => res.json())
		.then((uselessLocalVariable) => {
			// remove the li node from the list
			// event.target.parentElement.remove()
			// liContainer.remove()
			document.getElementById(`book-${bookID}`).remove()
			// console.log(bookID, liContainer)
			// debugger
		})
		.catch((err) => console.log(err))

	// ! the reponses for a delete request are up to the dev
	// HEAD NO CONTENT
	// CANNOT USE res.json() because there will be no response
	// Is empty object/array/datatype (json-server)
	// Send the object that was deleted from the database
	// if YOU have more control
}

const init = () => {
	fetchAllBooks()
	bookForm.addEventListener("submit", handleForm)
	// document.getElementById("hide").addEventListener("click", hideForm)
}

init()

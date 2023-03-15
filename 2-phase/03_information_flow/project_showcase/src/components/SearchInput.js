const SearchInput = ({ searchQuery, setSearchQuery }) => {
	const handleOnChange = (e) => {
		setSearchQuery(e.target.value)
	}
	return (
		<input
			type="text"
			placeholder="Search..."
			value={searchQuery}
			onChange={handleOnChange}
		/>
	)
}

export default SearchInput

const PhaseFilters = ({ setPhase }) => {

	const handleFilterChange = (e) => {
		setPhase(Number(e.target.name))
	}
	return (
		<div className="filter">
			<button name={0} onClick={(e) => setPhase(Number(e.target.name))}>All</button>
			<button name={5} onClick={handleFilterChange}>Phase 5</button>
			<button name={4} onClick={handleFilterChange}>Phase 4</button>
			<button name={3} onClick={handleFilterChange}>Phase 3</button>
			<button name={2} onClick={handleFilterChange}>Phase 2</button>
			<button name={1} onClick={handleFilterChange}>Phase 1</button>

		</div>
	)
}

export default PhaseFilters

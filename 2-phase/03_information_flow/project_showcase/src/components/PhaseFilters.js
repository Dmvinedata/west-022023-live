const PhaseFilters = ({ setPhase }) => {

	const handleFilterChange = (e) => {
		setPhase(Number(e.target.name))
	}
	return (
		<div className="filter">
			{/* <button onClick={(e) => setPhase(0)}>All</button>
			<button onClick={() => setPhase(5)}>Phase 5</button>
			<button onClick={() => setPhase(4)}>Phase 4</button>
			<button onClick={() => setPhase(3)}>Phase 3</button>
			<button onClick={() => setPhase(2)}>Phase 2</button>
			<button onClick={() => setPhase(1)}>Phase 1</button> */}
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

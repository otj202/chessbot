#for now, return the min. then later worry about the rest.
def traveling_salesman(vertices,cities):
	if len(cities) == 0:
		return 0	
	mn=float("inf")
	for v in vertices:
		wasInCities=False
		if v in cities:
			wasInCities=True
			cities.remove(v)
		vertices.remove(v)
		res=_traveling_salesman(graph,cities,v)
		if res is not None and res < mn:
			mn=res
		if wasInCities:
			cities.add(v)
	return mn 
def _travelling_salesman(vertices,cities,v):
	if len(cities) == 0:
		return 0
	mn=float("inf")
	for e in v.edges:
		wasInCities=False
		if e.to in vertices:
			if e.to in cities:
				wasInCities=True
				cities.remove(e.to)
			vertices.remove(e.to)
			mn = min(mn,e.weight + _travelling_salesman(vertices,cities,e.to))
		if wasInCities:
			cities.add(v)
	return mn





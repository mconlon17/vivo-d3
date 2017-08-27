import json, vivotools

query = """
SELECT ?p ?o
WHERE {
  <http://vivo.ufl.edu/individual/n25562> ?p ?o
}
ORDER BY ?p
"""

data=vivotools.vivo_sparql_query(query,debug=True) # show the encoded query                                # issue the query, return the data
print "Retrieved data:\n" + json.dumps(data, sort_keys=True, indent=4)
print "Items found = ",len(data["results"]["bindings"])             

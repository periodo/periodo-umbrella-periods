def filter_sparql(expression):
    """Returns a SPARQL FILTER statement, as a string, for the given expression."""
    return "FILTER {exp}".format(exp=expression)


def max_sparql(group_var, result_var='max'):
    """Returns a SPARQL MAX aggregator statement, as a string, using the given variables."""
    return "(MAX(?{g}) AS ?{r})".format(g=group_var, r=result_var)


def min_sparql(group_var, result_var='min'):
    """Returns a SPARQL MIN aggregator statement, as a string, using the given variables."""
    return "(MIN(?{g}) AS ?{r})".format(g=group_var, r=result_var)


def set_sparql(items):

    return "({0})".format(', '.join(map(lambda x: x.n3(), items)))


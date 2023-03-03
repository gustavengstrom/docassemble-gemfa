def create_df(table):
    #! Pandas cannot be pickled in DA so it need a python function to be established in a DA code block.
    """Input is a DA table that is converted to a pandas df. Note it need to be initated with the table varibles (eg. Thing)."""
    str(table)
    df = table.as_df()
    return df
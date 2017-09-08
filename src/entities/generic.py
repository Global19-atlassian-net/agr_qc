from .transaction import Transaction

class GenericTransactions(object):
	def __init__(self, graph):
		Transaction.__init__(self, graph)

	def generic_tx(self):

		#Removes skeleton nodes
		query = """
			MATCH (n)
            WHERE size(keys(n))=1
            DETACH DELETE (n)
		"""
		Transaction.deleteTransaction(self, query)

        # remove all nodes that do not have any edges
        query2 = """
			MATCH (n)
			WHERE size((n)--())=0
			DELETE (n)
		"""
		Transaction.deleteTransaction(self, query2)

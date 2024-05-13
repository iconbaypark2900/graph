# query_graph.py
import networkx as nx

def get_transactions_by_user(G, user_id):
    """
    Returns all transaction nodes connected to a given user.
    """
    if user_id in G:
        transactions = [n for n in G.successors(user_id) if G.nodes[n]['type'] == 'Transaction']
        return transactions
    else:
        return []

def get_products_by_transaction(G, transaction_id):
    """
    Returns all product nodes connected to a given transaction.
    """
    if transaction_id in G:
        products = [n for n in G.successors(transaction_id) if G.nodes[n]['type'] == 'Product']
        return products
    else:
        return []

if __name__ == "__main__":
    # Example usage with a hypothetical graph instance
    G = nx.DiGraph()  # This would normally be loaded or built elsewhere in your application
    # Populate G with example data for demonstration
    G.add_node(1, type='User', name='John Doe')
    G.add_node(100, type='Transaction', transaction_type='Deposit', amount=200)
    G.add_node(101, type='Product', product_name='Savings Account')
    G.add_edge(1, 100, relationship='performed')
    G.add_edge(100, 101, relationship='involves')
    
    user_transactions = get_transactions_by_user(G, 1)
    print("Transactions for User 1:", user_transactions)
    transaction_products = get_products_by_transaction(G, 100)
    print("Products for Transaction 100:", transaction_products)

from neo4j import GraphDatabase

def create_relation(tx, node1_name, node2_name, relation_type):
    tx.run("MATCH (a:Node),(b:Node) WHERE a.name = $node1_name AND b.name = $node2_name "
           "CREATE (a)-[r:`{}`]->(b) RETURN r".format(relation_type),
           node1_name=node1_name, node2_name=node2_name)

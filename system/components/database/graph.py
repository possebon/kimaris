# Python Standard Libraries
import sqlite3

def get_standard_graph():
    try:
        conn = sqlite3.connect("./db/results.db")
        cursor = conn.cursor()

        cursor.execute(f"""
                SELECT id, name, depth, cited_by FROM nodes;
                """)

        nodes_ = cursor.fetchall()
        
        cursor.execute(f"""
                SELECT source, target FROM links;
                """)
        
        links_ = cursor.fetchall()
    except Exception as e:
        print(e)
        
    nodes = []
    sizes = []
    for node in nodes_:
        data = {"name": node[1], "group": node[2]}
        nodes.append(data)
        sizes.append(node[2])
        
    links = []
    for link in links_:
        data = {"source": link[0]-1, "target": link[1]-1}
        links.append(data)
        
    return nodes, links, sizes

def get_selected_graph(name):
    nodes = []
    links = []
    sizes = []
    IDX = 0
    
    create_select_graph_db()
    
    conn = sqlite3.connect("./db/results.db")
    new_conn = sqlite3.connect("./db/graph.db")

    new_cursor = new_conn.cursor()
    cursor = conn.cursor()

    cursor.execute(f"""
            SELECT id, name, depth, cited_by FROM nodes
            WHERE name = "{name}";
            """)

    node = cursor.fetchone()
    idx = node[0]
    try:
        
        new_cursor.execute(f"""
        INSERT INTO nodes (name)
        VALUES ("{name}")              
        """)
        nodes.append({"name": node[1], "group": node[2]})
        sizes.append(node[3])
        IDX +=1
    except Exception as e:
        print("article 0")

    cursor.execute(f"""
            SELECT source, target FROM links
            WHERE source = "{idx}"
            OR target = "{idx}";
            """)

    links_ = cursor.fetchall()
    for link in links_:
        #links.append({"source": link[0], "target": link[1]})
        if link[0] != idx:
            cursor.execute(f"""
            SELECT id, name, depth, cited_by FROM nodes
            WHERE id = "{link[0]}";
            """)
            node = cursor.fetchone()
            try:
                new_cursor.execute(f"""
                INSERT INTO nodes (name)
                VALUES ("{node[1]}")              
                """)
                nodes.append({"name": node[1], "group": node[2]})
                sizes.append(node[3])
                links.append({"source": IDX, "target": 0})
                if len(links_) == 1:
                    links.append({"source": 0, "target": IDX})
                IDX +=1
                
            except Exception as e:
                print(e)
                try:
                    new_cursor.execute(f"""
                    SELECT id, name FROM nodes
                    WHERE name = "{node[1]}";
                    """)
                    node_id = cursor.fetchone()
                    node_id = node_id[0]
                    nodes.append({"name": node[1], "group": node[2]})
                    sizes.append(node[3])

                    links.append({"source": node_id, "target": 0})
                    if len(links_) == 1:
                        links.append({"source": 0, "target": node_id})
                except:
                    pass
                
        elif link[1] != idx:
            cursor.execute(f"""
            SELECT id, name, depth, cited_by FROM nodes
            WHERE id = "{link[1]}";
            """)
            node = cursor.fetchone()
            try:
                new_cursor.execute(f"""
                INSERT INTO nodes (name)
                VALUES ("{node[1]}");              
                """)
                nodes.append({"name": node[1], "group": node[2]})
                sizes.append(node[3])
                links.append({"source": 0, "target": IDX})
                if len(links_) == 1:
                    links.append({"source": IDX, "target": 0})
                IDX +=1
                
            except Exception as e:
                print(e)
                try:
                    new_cursor.execute(f"""
                    SELECT id, name FROM nodes
                    WHERE name = "{node[1]}";
                    """)
                    node_id = cursor.fetchone()
                    
                    node_id = node_id[0]
                    nodes.append({"name": node[1], "group": node[2]})
                    sizes.append(node[3])

                    links.append({"source": 0, "target": node_id})
                    if len(links_) == 1:
                        links.append({"source": node_id, "target": 0})
                except:
                    pass
        #print(nodes, links)
    return nodes, links, sizes

def create_select_graph_db():
    try:
        new_conn = sqlite3.connect("./db/graph.db")
                
        new_cursor = new_conn.cursor()
        new_cursor.execute("""
        CREATE TABLE nodes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        );             
        """)
        
        new_cursor.execute("""
        CREATE TABLE links (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            source INTEGER NOT NULL,
            target INTEGER NOT NULL
        );             
        """)
    except Exception as e:
        new_cursor.execute("DELETE FROM nodes;")
        new_cursor.execute("DELETE FROM links;")
        
def get_name_by_id(idx):
    print(idx)
    conn = sqlite3.connect("./db/results.db")
    cursor = conn.cursor()
    
    cursor.execute(f"""
    SELECT name FROM nodes
    WHERE id = "{idx}";               
    """)
    
    result = cursor.fetchone()
    
    print(result)
    name = result[0]
    
    return name
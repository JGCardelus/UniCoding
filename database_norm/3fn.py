class Node:
    def __init__(self, id_):
        self.id = id_
        self.goes_to = []
        self.comes_from = []

    def print_info(self):
        print("Node id: %s" % (self.id))

        if len(self.comes_from) > 0:
            print("Comes from nodes: ")
            for node_id in self.comes_from:
                print("     --> %s" % (node_id))

        if len(self.goes_to) > 0:
            print("Goes to nodes: ")
            for node_id in self.goes_to:
                print("     --> %s" % (node_id))


class Three_FN:
    def __init__(self):
        self.entities = ["vuelo", "destino", "avion", "compañia", "asiento", "pasajero"]
        self.rules = [
            [["vuelo"],["destino"]],
            [["vuelo"],["avion"]],
            [["vuelo"],["compañia"]],
            [["avion"],["compañia"]],
            [["pasajero"],["vuelo"]],
            [["asiento"],["pasajero", "vuelo"]],
            [["pasajero", "vuelo"], ["avion"]]
        ]
        self.nodes = []
        self.helper_nodes = []

        self.table_nodes = []

        #self.start()
        for entity in self.entities:
            node = Node(entity)
            self.nodes.append(node)

        self.define_relations()
        self.simplify_relations()

    def simplify_relations(self):
        keys = []
        for node in self.nodes:
            if len(node.goes_to) > 0:
                keys.extend(node.comes_from)
        print(keys)

        helper_keys = []
        for node in self.helper_nodes:
            helper_keys.append(node.id)

        self.remove_middleman(helper_keys)
        
        for node in self.nodes:
            if len(node.goes_to) > 0:
                values = node.goes_to
                values = self.delete_redundancies(values, keys, helper_keys)

                table_node = Node(str(len(self.table_nodes)))
                table_node.comes_from = node.comes_from
                table_node.goes_to = values
                self.table_nodes.append(table_node)

        print("Unsorted tables")
        for table_node in self.table_nodes:
            table_node.print_info()

    def remove_middleman(self, helper_keys):
        for node in self.nodes:
            if node.id not in helper_keys:
                node.comes_from, node.goes_to = self.translate_middleman(helper_keys, node.comes_from, node.goes_to)

    def translate_middleman(self, helper_keys, comes_from, goes_to):
        for key in comes_from:
            if key in helper_keys:
                comes_from.remove(key)
                comes_from.extend(self.get_node(key).comes_from)
        for key in goes_to:
            if key in helper_keys:
                goes_to.remove(key)
                goes_to.extend(self.get_node(key).goes_to)

        return comes_from, goes_to


    def delete_redundancies(self, values, keys, helper_keys):
        values_to_remove = []
        for value in values:
            if value in keys:
                key_node = self.get_node(value)
                
                for key_node_value in key_node.goes_to:
                    if (key_node_value in values) and (key_node_value not in keys):
                        print(key_node_value)
                        values.remove(key_node_value)
            if value in helper_keys:
                values.remove(value)
        return values

    def get_node(self, id_):
        node = None
        for test_node in self.nodes:
            if test_node.id == id_:
                node = test_node

        return node

    def define_relations(self):
        for rule in self.rules:
            keys, values = rule

            # Simple relation
            if len(keys) == 1:
                self.get_node(keys[0]).comes_from = keys
                self.define_node_relations(keys[0], values)
            else:
                i = len(self.helper_nodes)
                node = Node(str(i))
                node.comes_from.extend(keys)

                self.nodes.append(node)
                self.helper_nodes.append(node)

                for key in keys:
                    self.define_node_relations(key, str(i))
                
                self.define_node_relations(str(i), values)

        print("Initial node relations")
        for node in self.nodes:
            node.print_info()

    def define_node_relations(self, key, values):
        node = self.get_node(key)
        for value in values:
            node.goes_to.append(self.get_node(value).id)

    def start(self):
        raw_relation = input("Please enter relation -- A,B,C,D: ")
        self.entities = raw_relation.split(',')

        print("Your entities are: ")
        for entity in self.entities:
            node = Node(entity)
            self.nodes.append(node)
            print("     -> %s" % (entity))

        while True:
            raw_rule = input("Please enter rule (q, to stop) -- A,B,...,Z:A1,B1,...,Z1 : ")
            if raw_rule == "q":
                break
            if len(raw_rule.split(":")) == 2:
                raw_key,raw_value = raw_rule.split(":")
                
                key = raw_key.split(",")
                value = raw_value.split(",")

                if self.are_entity(key) and self.are_entity(value):
                    self.rules.append([key,value])
            else:
                print("You have to enter key/s:value/s. Please try again")

    def are_entity(self, entities):
        are_entities = True
        for entity in entities:
            if not self.is_entity(entity):
                are_entities = False
                break
                
        return are_entities

    def is_entity(self, entity):
        is_entity = True
        if entity not in self.entities:
            print("%s does not exist, please try again" % entity)
            is_entity = False

        return is_entity


fn = Three_FN()
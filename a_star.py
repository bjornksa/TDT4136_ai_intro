from Map_2 import Map_Obj
from Node import Node


def best_friend_search():
    open_nodes = []
    closed = []
    map_obj = Map_Obj(task=4)
    endpos = map_obj.get_goal_pos()

    start = Node(None, map_obj.get_start_pos(), endpos, 0)
    start.g = 0
    open_nodes.insert(0, start)

    i = 0

    while True:
        current = open_nodes.pop(0)

        if current.pos == endpos:
            print("Finished after {} iterations".format(i))
            endnode = current
            while current.parent is not None:
                map_obj.save_frame(i)
                print(current.pos)
                current = current.parent
                map_obj.set_cell_value(current.pos, 'p')
                i+=1
            map_obj.save_frame(i)
            return endnode, map_obj

        for pos in current.get_adjacent():
            if pos in [node.pos for node in closed]:
                continue

            if map_obj.get_cell_value(pos) == -1:
                continue

            cost = map_obj.get_cell_value(pos)
            if pos in [node.pos for node in open_nodes]:
                for node in open_nodes:
                    if node.pos == pos:
                        node.propogate(current)
                        break
                continue

            neighbour = Node(current, pos, endpos, current.g + cost)

            current.children.append(neighbour)
            priority_insert(open_nodes, neighbour)
            map_obj.set_cell_value(pos, 'o')

        closed.append(current)
        map_obj.set_cell_value(current.pos, 0)
        if len(open_nodes) == 0:
            print("No path found")
            return None, map_obj

        #if not i%10:
        map_obj.save_frame(i)
        i+=1


def priority_insert(list, node):
    for i, x in enumerate(list):
        if x.f > node.f:
            list.insert(i, node)
            return
    # If no nodes in the list are larger than node, append it
    list.append(node)


end, map_obj = best_friend_search()


map_obj.show_map()

from State import *
import copy
class Controller:
    def __init__(self, instance):
        self.__instance = instance

    def bfs(self, root):
        q = [State(root)]
        visited = []
        found = False
        prob = copy.deepcopy(self.__instance)
        while q != [] and not found:
            current = q.pop()
            #print(str(current))
            if current.isSolution() == True:
                s = ""
                for i in current.getMatrix():
                    for j in i:
                        s += str(j)
                        s += " "
                    s += "\n"
                print(s)
                found = True
            else:
                if prob.difference(current) == prob.getDim():
                    prob = copy.deepcopy(visited.pop(0))
                    if current.isValid() == False:
                        current = copy.deepcopy(prob)

                aux = prob.expand(current)
                q = q + [aux]
                if aux.isValid() and aux not in visited:
                    v = copy.deepcopy(aux)
                    visited.append(v)
                    #print("visited")
                    #for v in visited:
                        #print(str(v))
        return found

    def gbfs(self, root):
        n = root.getDim()
        #print(n)
        found = False
        visited = []
        toVisit = [root]
        k = 0
        prob = copy.deepcopy(self.__instance)
        while toVisit != [] and not found:
            #print("run " + str(k))
            if toVisit == []:
                return False
            #print("Current node")
            node = toVisit.pop(0)
            #print(node)
            visited = visited + [node]
            #print("visited")
            #for v in visited:
                #print(v)
            if node.isSolution(): #node == elem
                found = True
            else:
                aux = []
            #print("generated kids")
            prob = copy.deepcopy(node)
            for i in range(0, n):
                #first unvisited child of node
                #expand I believe, expand for n times, since we have n possible nodes, only add valid ones?
                child = prob.expand(node)
                #print(child)
                try:
                    if child.isValid() == True:
                        #print("child added")
                        print(child)
                        auxKid = copy.deepcopy(child)
                        aux = aux + [auxKid]
                except:
                    print()
            #print("aux")
            for a in aux:
                heu = a.heuristic()
                if node.difference(a) == heu:
                    aux.remove(a)
            toVisit = aux + toVisit #based on the heuristic function
            toVisit = [a] + toVisit
            #print("to Visit")
            #for v in toVisit:
                #print(str(v))
            k += 1
        return found

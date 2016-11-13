#URI 1049
class Node:
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

aguia = Node("aguia", None, None)
pomba = Node("pomba", None, None)
homem = Node("homem", None, None)
vaca = Node("vaca", None, None)
pulga = Node("pulga", None, None)
lagarta = Node("lagarta", None, None)
sanguessuga = Node("sanguessuga", None, None)
minhoca = Node("minhoca", None, None)

node0 = Node("carnivoro", aguia, None)
node1 = Node("onivoro", pomba, None)
node2 = Node("onivoro", homem, None)
node3 = Node("herbivoro", vaca, None)
node4 = Node("hematofago", pulga, None)
node5 = Node("herbivoro", lagarta, None)
node6 = Node("hematofago", sanguessuga, None)
node7 = Node("onivoro", minhoca, None)

nodeA = Node("ave", node0, node1)
nodeB = Node("mamifero", node2, node3)
nodeC = Node("inseto", node4, node5)
nodeD = Node("anelideo", node6, node7)

vertebrado = Node("vertebrado", nodeA, nodeB)
invertebrado = Node("invertebrado", nodeC, nodeD)

root = Node("", vertebrado, invertebrado)

v = input()
t = input()
a = input()
values = [v, t, a]
def find(root, value):
	if value == root.left.value:
		return root.left
	elif value == root.right.value:
		return root.right

for value in values:
	root = find(root, value)

print(root.left.value)

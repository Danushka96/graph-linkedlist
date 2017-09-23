class node:
	def __init__(self,data):
		self.data=data
		self.bottom=None
		self.next=[]

class graph:
	def __init__(self):
		self.head=None

	def add(self,vert,edge):
		if self.head==None:
			self.head=node(vert)
			self.head.next.append(edge)
		else:
			temp=self.head
			found=False
			while temp!=None and not found:
				if temp.data==vert:
					temp.next.append(edge)
					found=True
				temp=temp.bottom
			if not found:
				new=node(vert)
				new.bottom=self.head
				self.head=new
				self.head.next.append(edge)

	def insert(self,vert,edge):
		self.add(vert,edge)
		self.add(edge,vert)

	def delete(self,vert):
		temp=self.head
		while temp!=None:
			# Remove Verteces
			if self.head==vert:
				self.head=temp.bottom
			elif temp.bottom!=None:
				if vert==temp.bottom.data:
					temp.bottom=temp.bottom.bottom
			# Remove Edges
			if temp.next!=None:
				if vert in temp.next:
					temp.next.remove(vert)
			temp=temp.bottom

	def printme(self):
		temp=self.head
		while temp!=None:
			print(temp.data," -> ",temp.next)
			temp=temp.bottom

	def BFS(self,vert): #Vert is a node
		white=[] #white Nodes
		gray=[]	#Gray Nodes
		black=[] #Black Nodes
		Q=[]	#Main Queue
		dp=[]	#Distance and Parents
		temp=self.head
		#Changing the all node except vert to white
		while temp!=None:
			if temp.data!=vert.data:
				white.append(temp.data)
				dp.append([temp.data,None,None])
			temp=temp.bottom
		gray.append(vert.data)
		dp.append([vert.data,0,None])
		Q.append(vert)
		#Traversing
		while Q!=[]:
			u=Q.pop(0)
			for v in u.next:
				if v in white:
					white.remove(v)
					gray.append(v)
					dv=self.searchdp(dp,v)
					du=self.searchdp(dp,u.data)
					dp[dv]=[v,(int(dp[du][1])+1),u.data]
					Q.append(self.searchnode(v))
			black.append(u.data)
			print("------------------------")
			self.printer(black,white,gray,dp)
			print("-----------------------")

	def searchdp(self,dp,vert):
		for i in range (len(dp)):
			if dp[i][0]==vert:
				return i

	def searchnode(self,vert):
		temp=self.head
		while temp!=None:
			if temp.data==vert:
				return temp
				break
			temp=temp.bottom

	def traverse(self,vert):
		n=self.searchnode(vert)
		self.BFS(n)

	def printer(self,black,white,gray,dp):
		for i in gray:
			print("node= ",i,"\tParent= ", end="")
			index=self.searchdp(dp,i)
			print(dp[index][2],"\tDistance= ",dp[index][1],"\tcolor= ", end="")
			if i in white:
				color="white"
			elif i in black:
				color="black"
			else:
				color="gray"
			print(color)
		

a=graph()
r="r"
x="x"
v="v"
s="s"
w="w"
t="t"
u="u"
y="y"
a.insert(r,v)
a.insert(r,s)
a.insert(s,w)
a.insert(w,t)
a.insert(w,x)
a.insert(x,t)
a.insert(x,y)
a.insert(t,u)
a.insert(y,u)
a.printme()
# print("---------------------")
# a.delete(5)
# a.printme()
a.traverse(s)
import math
from haversine import haversine
import folium
import webbrowser
class node:
    name = ""
    Lat = 0.0
    Lng = 0.0
    adnd = []
    mult = 1
    def __init__(self, sx, sy, sname,smult): #�꾩튂 珥덇린��
        self.Lat = sx
        self.Lng = sy
        self.name = sname
        self.adnd = []
        self.mult = smult
    def anode(self, nd):
        self.adnd.append(nd)
        nd.adnd.append(self)
    def dist(self, nd):
        return (haversine([self.Lat, self.Lng],[nd.Lat, nd.Lng],unit = 'km')) * max(self.mult,nd.mult)
    def adist(self, nd):
        return (haversine([self.Lat, self.Lng],[nd.Lat, nd.Lng],unit = 'km'))

def daik(nds,start,end):
    path = {}
    fdist = {}
    rdist = {}
    for i in nds:
        rdist[i] = 99999.0
    rdist[start] = 0.0
    while rdist:
        m = min(rdist,key=rdist.get)
        fdist[m] = rdist[m]
        del rdist[m]
        for i in nds[m].adnd:
            temp = fdist[m] + nds[m].dist(nds[i.name])
            if i.name in rdist:
                if temp < rdist[i.name]:
                    rdist[i.name] = fdist[m] + nds[m].dist(nds[i.name])
                    path[i.name] = m  
    backtrack = end
    track = []
    while backtrack != start:
        track.append(backtrack)
        backtrack = path[backtrack]
    track.append(backtrack)
    track = track[::-1]    
    return track

    
dic = {}
dns = {}

latlng = []
linking = []
a = []
#a = [node(0,0,'a',1),node(1,0,'b',1),node(2,0,'c',1),node(0,1,'d',1),node(1,1,'e',7),node(2,1,'f',1),node(0,2,'g',1),node(1,2,'h',1),node(2,2,'i',1)]

file = open("노드.txt","r")
rf = file.readlines()
for r in rf:
    r = r.strip()
    latlng.append(r.split(" "))
file.close()

count = 0
for i in latlng:
    a.append(node(float(i[0]),float(i[1]),str(count),float(i[2])))
    count += 1
#print(haversine([37.541, 126.986],[43.65, -79.38],unit = 'km'))


for i in a:
    dic[i.name] = i

file = open("링크.txt","r")
rf = file.readlines()
for r in rf:
    r = r.strip()
    linking.append(r.split(" "))
file.close()

for i in linking:
    a[int(i[0])].anode(a[int(i[1])])


file = open("건물이름.txt","r")
rf = file.readlines()
Bindex = 756
for r in rf:
    r = r.strip()
    dns[r] = a[Bindex].name
    Bindex += 1
file.close()

webbrowser.open('휠체어 이동가능_불가능_완만_경로표시 (1).html')

Ssearch = ''
while Ssearch == '':
    print("\n출발할 건물을 입력하십시오 : ",end ='')
    Ssearch = str(input()) #찾을 건물을 입력받음
    if not Ssearch in dns:
        print("not found that building")
        Ssearch = ''
        
search = ''
while search == '':
    print("\n찾을 건물을 입력하십시오 : ",end ='')
    search = str(input()) #찾을 건물을 입력받음
    if not search in dns:
        print("not found that building")
        search = ''

a.append(node(dic[dns[Ssearch]].Lat, dic[dns[Ssearch]].Lng,str(count),1)) #시작점
count += 1

dic[a[count - 1].name] = a[count - 1]

dmin = 1000
for i in a:
    tdist = a[count - 1].adist(i)
    if(tdist < dmin and tdist != 0):
        dmin = tdist
        snode = i
a[count - 1].anode(snode)

tr = daik(dic,a[count - 1].name,dns[search]) #종점

m=folium.Map(location=[36.63149098563914, 127.45368120547008],
            zoom_start=17,
            )
folium.Marker([dic[dns[Ssearch]].Lat, dic[dns[Ssearch]].Lng],tooltip=Ssearch,popup='1').add_to(m)
folium.Marker([dic[dns[search]].Lat, dic[dns[search]].Lng],tooltip=search,popup='1',icon=folium.Icon(color="red")).add_to(m)
prev = -1
for i in tr:
    if(prev != -1):
        folium.PolyLine(locations=[[a[int(prev)].Lat,a[int(prev)].Lng],[a[int(i)].Lat,a[int(i)].Lng]], color="red", weight=2.5, opacity=1).add_to(m)
    prev = i

m.save('찾은 경로.html')
webbrowser.open('찾은 경로.html')

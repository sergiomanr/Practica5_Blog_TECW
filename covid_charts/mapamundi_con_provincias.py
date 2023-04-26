from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import csv
import json
fig = plt.figure(figsize=(12,9))

# m = Basemap(projection='mill',
#            llcrnrlat = -90,
#            urcrnrlat = 90,
#            llcrnrlon = -180,
#            urcrnrlon = 180,
#            resolution = 'l')
pais = input('Que país quiere que esté centrado:\n--->')
coords = []
with open('covid_charts/datos/paises.json',mode='r',encoding='utf8') as f:
    coords = json.load(f)[pais]
m = Basemap(projection='nsper',lon_0=coords[0],lat_0=coords[1],satellite_height=3000*1000,resolution='l')

m.drawcoastlines()
m.drawcountries(color='red')
# m.drawstates(color='blue')
m.drawcounties(color='orange')
# m.drawrivers(color='black')
# m.drawmapboundary(fill_color='aqua')
# m.fillcontinents(color='coral',lake_color='aqua')

m.drawmapboundary(color='pink', linewidth=1, fill_color='aqua')
m.fillcontinents(color='lightgreen', lake_color='aqua')

# m.drawlsmask(land_color='lightgreen', ocean_color='aqua', lakes=True)

# m.etopo()
# m.bluemarble()
# m.shadedrelief()


with open('covid_charts/datos/confirmed.csv',mode='r',encoding='utf8') as f:
    reader = csv.reader(f)
    next(reader)
    for i in reader:
        if len(i[0]) !=0 and i[2] != '':
            m.scatter(float(i[3]),float(i[2]),latlon=True,marker='*',c='deeppink')
            plt.annotate(i[0],m(float(i[3]),float(i[2])))
        elif i[2] != '':
            m.scatter(float(i[3]),float(i[2]),latlon=True)
            plt.annotate(i[1],m(float(i[3]),float(i[2])))
# m.drawparallels(np.arange(-90,90,20),labels=[True,False,False,False])
# m.drawmeridians(np.arange(-180,180,60),labels=[0,0,0,1])

# np.arange(start,stop,step)
# labels=[left,right,top,bottom] posicion de las labels
# plt.title('Basemap tutorial', fontsize=20)

plt.show()
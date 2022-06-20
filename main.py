
from turtle import position
import folium
from folium.features import CustomIcon
import os
import pandas as pd
import folium.plugins as plug
import fontawesome as fa
import base64



df=pd.read_excel('C:/Users/����ȯ/map_project/��ϴ� ��ü�ǹ���ǥ.xlsx')


m=folium.Map(location=[36.6286813647,127.4559668598],
zoom_start=16,
max_bounds = True,

min_zoom = 16,
min_lat = 36.621 ,
max_lat = 36.645,
min_lon= 127.449,
max_lon = 127.464)

icon_image1 = 'C:/Users/����ȯ/OneDrive/���� ȭ��/��ϴ��б�������.png'
shadow_image1 = 'C:/Users/����ȯ/OneDrive/���� ȭ��/��ϴ��б�������_�׸���.png'

icon1 = CustomIcon(
    icon_image1,
    icon_size=(50, 50),
    icon_anchor=(50,50),
    shadow_image=shadow_image1,
    shadow_size=(50, 50),
    shadow_anchor=(50,50),
    popup_anchor=(-25,-50)
)

# map�� S��, N��, E�� ������ MarkerCluster ��ü���� �� m�� �߰� #
mcg=plug.MarkerCluster(control=False)
m.add_child(mcg)

# MarkerCluster�� ���� �߰� #
Area_S_cluster=plug.FeatureGroupSubGroup(mcg,'S����').add_to(m)
Area_N_cluster=plug.FeatureGroupSubGroup(mcg,'N����').add_to(m)
Area_E_cluster=plug.FeatureGroupSubGroup(mcg,'E����').add_to(m)
Area_bus1678_cluster=plug.FeatureGroupSubGroup(mcg,'bus1678').add_to(m)
Area_bus1682_cluster=plug.FeatureGroupSubGroup(mcg,'bus1682').add_to(m)
Area_SupportCenter_cluster=plug.FeatureGroupSubGroup(mcg,'SupportCenter').add_to(m)
Area_Dormitory_cluster=plug.FeatureGroupSubGroup(mcg,'�л���Ȱ��').add_to(m)

# �˻� ��� ���� �� layer�� ������ geojson ��ü ���� �� �ʿ��� �ǹ� ��ǥ�� ������ �� ����Ʈ ���� #
point_list = []

for name, lat, lng, area, image in zip(df.�ǹ��̸�, df.����, df.�浵, df.�ǹ�����, df.����):
    if(area=='S'):
        pic = base64.b64encode(open(image,'rb').read()).decode()
        image_tag = '<img src="data:image/jpg;base64,{}">'.format(pic)
        iframe = folium.IFrame(image_tag, width=400, height=400)
        popup = folium.Popup(iframe, max_width=300)
        
        folium.Marker([lat,lng],
                      popup=popup,
                      tooltip=name,
                     icon=folium.Icon(color='orange',icon='university',prefix='fa')).add_to(Area_S_cluster)
    if(area=='N'):
        pic = base64.b64encode(open(image,'rb').read()).decode()
        image_tag = '<img src="data:image/jpg;base64,{}">'.format(pic)
        iframe = folium.IFrame(image_tag, width=400, height=400)
        popup = folium.Popup(iframe, max_width=300)
        
        folium.Marker([lat,lng],
                      popup=popup,
                      tooltip=name,
                     icon=folium.Icon(color='black',icon='university',prefix='fa')).add_to(Area_N_cluster)
    if(area=='E'):
        pic = base64.b64encode(open(image,'rb').read()).decode()
        image_tag = '<img src="data:image/jpg;base64,{}">'.format(pic)
        iframe = folium.IFrame(image_tag, width=400, height=400)
        popup = folium.Popup(iframe, max_width=300)
        
        folium.Marker([lat,lng],
                      popup=popup,
                      tooltip=name,
                     icon=folium.Icon(color='blue',icon='university',prefix='fa')).add_to(Area_E_cluster)
    if(area=='�л���Ȱ��'):
        pic = base64.b64encode(open(image,'rb').read()).decode()
        image_tag = '<img src="data:image/jpg;base64,{}">'.format(pic)
        iframe = folium.IFrame(image_tag, width=400, height=400)
        popup = folium.Popup(iframe, max_width=300)
        
        folium.Marker([lat,lng],
                      popup=popup,
                      tooltip=name,
                     icon=folium.Icon(color='green',icon='university',prefix='fa')).add_to(Area_Dormitory_cluster)
    
    if(area=='bus1678'):
        folium.Marker([lat,lng],
        popup='<h3 style="text-align:center;"><iframe src="https://m.map.kakao.com/actions/busStationInfo?busStopId=BS457974&q=%EC%B6%A9%EB%B6%81%EB%8C%80%20%EB%B2%84%EC%8A%A4%EC%A0%95%EB%A5%98%EC%9E%A5".html" width="400" height="300" marginwidth="0" marginheight="0" frameborder="2" scrolling="yes"></iframe></h3>',
        tooltip=name,
        icon=folium.Icon(icon='bus', prefix='fa', color='red')).add_to(Area_bus1678_cluster)

    if(area=='bus1682'):
        folium.Marker([lat,lng],
        popup='<h3 style="text-align:center;"><iframe src="https://m.map.kakao.com/actions/busStationInfo?busStopId=BS457984&q=%EC%B6%A9%EB%B6%81%EB%8C%80%20%EB%B2%84%EC%8A%A4%EC%A0%95%EB%A5%98%EC%9E%A5".html" width="400" height="300" marginwidth="0" marginheight="0" frameborder="2" scrolling="yes"></iframe></h3>',
        tooltip=name,
        icon=folium.Icon(icon='bus', prefix='fa', color='red')).add_to(Area_bus1682_cluster)

    if(area=='�����������'):
        folium.Marker([lat,lng],
        popup='<h3 style="text-align:center;"><iframe src="https://supporter.chungbuk.ac.kr".html" width="400" height="300" marginwidth="0" marginheight="0" frameborder="2" scrolling="yes"></iframe></h3>',
        tooltip=name,
        icon=icon1).add_to(Area_SupportCenter_cluster)
        
    
    # json ���� ���Ŀ� ���� point_list�� ��ǥ �� ���� ���� #
    # ����: http://www.gisdeveloper.co.kr/?p=8002
    point_list.append({
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [lng, lat]
      },
      "properties": {
        "name": name
      }
    })


    

# point_list Ȱ���Ͽ� Geojson ��ü�� ���� ��� �ϼ� #
points = {
    "type": "FeatureClooection",
    "features": point_list
}   

# points Ȱ���Ͽ� �˻��� ���� GeoJson ��ü ���� #
building_geojson_obj = folium.GeoJson(points, overlay=False).add_to(m)

# ������ geojson ��ü building_geojson_obj�� layer�� �����Ͽ� �˻� ��� ��ư ���� #
map_search = plug.Search(layer=building_geojson_obj,
            search_label="name",
            search_zoom=18,
            geom_type='Point',
            position='topleft'
           ).add_to(m)
    
## �� ��ġ Ȯ�� ��ư ���� ##
plug.LocateControl(auto_start=True).add_to(m)

## ��üȭ�� ��ư ���� ##
plug.Fullscreen(
    position='topright',
    title='Expand me',
    title_cancel='Exit me',
    force_separate_button=True  
).add_to(m)
folium.LayerControl().add_to(m)

## ��� ǥ�� ##
# ���� Ȥ�� �ϸ��� ����� ��� ǥ��#
location_data_df1 = pd.read_excel("C:/Users/����ȯ/map_project/��ü�����԰��ɿ���ǥ�ð��_�����Ǵ¸ſ�ϸ��Ѱ��.xlsx", sheet_name=None)


for sheet in list(location_data_df1.keys()) :
    location_data_posibile = []
    for lat, lng in zip(location_data_df1[sheet].����, location_data_df1[sheet].�浵) :
        location_data_posibile.append([lat, lng])
    folium.PolyLine(locations=location_data_posibile, tooltip="���� Ȥ�� �ϸ��� ���").add_to(m)

# ���ֽ� ��ü�� �̵� ���� ��� ǥ��#
location_data_df2 = pd.read_excel("C:/Users/����ȯ/map_project/��ü�����԰��ɿ���ǥ�ð��_���ֽ���ü���ݰ����Ѱ��.xlsx", sheet_name=None)


for sheet in list(location_data_df2.keys()) :
    location_data_posibile = []
    for lat, lng in zip(location_data_df2[sheet].����, location_data_df2[sheet].�浵) :
        location_data_posibile.append([lat, lng])
    folium.PolyLine(locations=location_data_posibile, color="yellow", tooltip="���ֽ� ��ü�� ��� ������ ���").add_to(m)  

# ���ֽ� ��ü�� �̵� �Ұ��� ��� ǥ��#
location_data_df3 = pd.read_excel("C:/Users/����ȯ/map_project/��ü�����԰��ɿ���ǥ�ð��_���ֽ���ü���ݰ���Ѱ��.xlsx", sheet_name=None)


for sheet in list(location_data_df3.keys()) :
    location_data_posibile = []
    for lat, lng in zip(location_data_df3[sheet].����, location_data_df3[sheet].�浵) :
        location_data_posibile.append([lat, lng])
    folium.PolyLine(locations=location_data_posibile, color="red", tooltip="���ֽ� ��ü�� ��� ����� ���").add_to(m)
    

m.save("��ü������ǥ_��_�˻���ɱ���.html")
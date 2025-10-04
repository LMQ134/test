import pygal
from pygal_maps_world.maps import World

wm = World()
wm.title='North,central,and South America'

wm.add('North America',['ca','mx','us'])
wm.add('central america',['bz','cr','gt','hn','pa','sv'])
wm.add('south america',['ar','bo','br','cl','co','ec','gf','gy','pe',
                        'py','sr','uy','ve'])
wm.render_to_file('americas.svg')

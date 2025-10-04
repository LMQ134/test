import pygal
from pygal_maps_world.maps import World

wm = World()

wm.title='Populations of countries in north america'
wm.add("north",{'ca':3412600,'us':309349000,'mx':113423000})

wm.render_to_file('na_population.svg')
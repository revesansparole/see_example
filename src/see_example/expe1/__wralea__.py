
# This file has been generated at Fri Jul 29 14:24:11 2016

from openalea.core import *


__name__ = 'see.ex.expe1'

__editable__ = True
__description__ = 'First experiment conducted on phenome'
__license__ = 'Cecill-C'
__url__ = ''
__alias__ = []
__version__ = '0.0.3'
__authors__ = 'Jerome Chopard'
__institutes__ = 'INRIA/CIRAD'
__icon__ = ''


__all__ = ['_140666437983312', 'see_example_library_image_apply_mask']



_140666437983312 = CompositeNodeFactory(uid='b373ae3953da11e6907fd4bed973e64a',
                             name='see_ex_size',
                             description='Workflow used to compute size of a plant from binary images',
                             category='Unclassified',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('see', 'load_data'), 3: ('see', 'load_data'), 6: ('see.ex.expe1', 'mask')},
                             elt_connections={  23810552: (2, 0, 6, 0), 23810576: (3, 0, 6, 1)},
                             elt_data={  2: {  'block': False,
         'caption': 'load_data',
         'delay': 0,
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -96.75558395353109,
         'posy': 64.24159239661068,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': 'load_mask',
         'delay': 0,
         'hide': True,
         'id': 3,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -30.266690608822746,
         'posy': 63.92315650747335,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   6: {  'block': False,
         'caption': 'mask',
         'delay': 0,
         'hide': True,
         'id': 6,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -50.18443815431721,
         'posy': 106.57387748151154,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set([]),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set([]),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [(0, "''"), (1, 'None')],
   3: [(0, "''"), (1, 'None')],
   6: [],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {'position': [-96.75558395353109, 64.24159239661068], 'userColor': None, 'useUserColor': False},
   3: {'position': [-30.266690608822746, 63.92315650747335], 'userColor': None, 'useUserColor': False},
   4: {  'position': [20, 150], 'useUserColor': False, 'userColor': None},
   6: {'position': [-50.18443815431721, 106.57387748151154], 'userColor': None, 'useUserColor': False},
   '__in__': {'position': [0, 0], 'userColor': None, 'useUserColor': True},
   '__out__': {'position': [0, 0], 'userColor': None, 'useUserColor': True}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




see_example_library_image_apply_mask = Factory(uid='b373ae3853da11e6907fd4bed973e64a',
                name='mask',
                authors='Jerome Chopard (wralea authors)',
                description='',
                category='Unclassified',
                nodemodule='see_example.library.image',
                nodeclass='apply_mask',
                inputs=({'interface': 'IImage', 'name': 'img'}, {'interface': 'IImage', 'name': 'mask'}),
                outputs=({'interface': 'IImage', 'name': 'img'},),
                widgetmodule=None,
                widgetclass=None,
               )





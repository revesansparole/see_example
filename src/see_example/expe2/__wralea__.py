
# This file has been generated at Wed Aug  3 19:36:33 2016

from openalea.core import *


__name__ = 'see.ex.expe2'

__editable__ = True
__description__ = 'First experiment conducted on phenome'
__license__ = 'Cecill-C'
__url__ = ''
__alias__ = []
__version__ = '0.0.3'
__authors__ = 'Jerome Chopard'
__institutes__ = 'INRIA/CIRAD'
__icon__ = ''


__all__ = ['_139812625850448']



_139812625850448 = CompositeNodeFactory(uid='146f9bb853db11e6907fd4bed973e64a',
                             name='see_ex_color',
                             description='Workflow used to average color of a plant from binary images',
                             category='Unclassified',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('see', 'load_data'),
   5: ('see', 'log_to_see'),
   6: ('see.ex.library', 'average')},
                             elt_connections={  32797176: (5, 0, 2, 1), 32797200: (2, 0, 6, 0)},
                             elt_data={  2: {  'block': False,
         'caption': 'load_data',
         'delay': 0,
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -77.6312745640333,
         'posy': 63.625819779335956,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   5: {  'block': False,
         'caption': 'log_to_see',
         'delay': 0,
         'hide': True,
         'id': 5,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -72.60482010929155,
         'posy': 14.881733314326837,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   6: {  'block': False,
         'caption': 'average',
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
                             elt_value={  2: [(0, "'ceb0d366599b11e6a3a6d4bed973e64a'")],
   5: [],
   6: [(1, '[]')],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {'position': [-77.6312745640333, 63.625819779335956], 'userColor': None, 'useUserColor': False},
   3: {  'position': [-5.747127145247607, 41.95108015699692],
         'useUserColor': False,
         'userColor': None},
   4: {  'position': [20, 150], 'useUserColor': False, 'userColor': None},
   5: {'position': [-72.60482010929155, 14.881733314326837], 'userColor': None, 'useUserColor': False},
   6: {'position': [-50.18443815431721, 106.57387748151154], 'userColor': None, 'useUserColor': False},
   '__in__': {'position': [0, 0], 'userColor': None, 'useUserColor': True},
   '__out__': {'position': [0, 0], 'userColor': None, 'useUserColor': True}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )





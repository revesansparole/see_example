
# This file has been generated at Tue Jul 26 11:34:46 2016

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


__all__ = ['_140407581631696']



_140407581631696 = CompositeNodeFactory(name='see_ex_color',
                             description='Workflow used to average color of a plant from binary images',
                             category='Unclassified',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('see', 'load_data'), 6: ('see.ex.library', 'average')},
                             elt_connections={  21479928: (2, 0, 6, 0)},
                             elt_data={  2: {  'block': False,
         'caption': 'load_data',
         'delay': 0,
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -118.09078852573283,
         'posy': 41.95108015699692,
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
                             elt_value={  2: [(0, "''"), (1, 'None')], 6: [(0, 'None')], '__in__': [], '__out__': []},
                             elt_ad_hoc={  2: {'position': [-118.09078852573283, 41.95108015699692], 'userColor': None, 'useUserColor': False},
   3: {  'position': [-5.747127145247607, 41.95108015699692],
         'useUserColor': False,
         'userColor': None},
   4: {  'position': [20, 150], 'useUserColor': False, 'userColor': None},
   6: {'position': [-50.18443815431721, 106.57387748151154], 'userColor': None, 'useUserColor': False},
   '__in__': {'position': [0, 0], 'userColor': None, 'useUserColor': True},
   '__out__': {'position': [0, 0], 'userColor': None, 'useUserColor': True}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )





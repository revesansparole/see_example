from openalea.core import Factory as Fa

__name__ = 'see.ex.expe1.nodes'
__description__ = 'First experiment conducted on phenome'
__license__ = 'Cecill-C'
__url__ = ''
__alias__ = []
__version__ = '0.0.3'
__authors__ = 'Jerome Chopard'
__institutes__ = 'INRIA/CIRAD'
__icon__ = ''

__all__ = ['mask']

mask = Fa(name='mask',
          authors='Jerome Chopard (wralea authors)',
          description='',
          category='Unclassified',
          nodemodule='see_example.library.image',
          nodeclass='apply_mask',
          inputs=({'interface': 'IImage', 'name': 'img'},
                  {'interface': 'IImage', 'name': 'mask'}),
          outputs=({'interface': 'IImage', 'name': 'img'},),
          widgetmodule=None,
          widgetclass=None,
          )

"""Example of nodes that manipulate images
"""

from openalea.core import Factory as Fa
# from openalea.core.interface import IInterface
from openalea.core.interface import *

__name__ = "see.ex.library"
__alias__ = []
__version__ = '0.0.3'
__license__ = "Cecill-C"
__authors__ = 'Jerome Chopard'
__institutes__ = 'INRIA/CIRAD'
__description__ = 'Algo for SEE example project'
__url__ = ''

__all__ = []


class IImage(IInterface):
    pass


lp = Fa(uid="5fd581484f6511e690ec0242b2ebf0f7",
        name="load",
        description="",
        category="",
        nodemodule="see_example.library.image",
        nodeclass="load_image",
        inputs=(dict(name="pth", interface=IStr),),
        outputs=(dict(name="img", interface=IImage),),
        )

__all__.append('lp')

sp = Fa(uid="5fd581494f6511e690ec0242b2ebf0f7",
        name="store",
        description="",
        category="",
        nodemodule="see_example.library.image",
        nodeclass="store_image",
        inputs=(dict(name="img", interface=IImage),
                dict(name="pth", interface=IStr),),
        outputs=(dict(name="pth", interface=IStr),),
        )

__all__.append('sp')

to_hsv = Fa(uid="5fd5814a4f6511e690ec0242b2ebf0f7",
            name="to_hsv",
            description="",
            category="",
            nodemodule="see_example.library.image",
            nodeclass="to_hsv",
            inputs=(dict(name="img", interface=IImage),),
            outputs=(dict(name="img", interface=IImage),),
            )

__all__.append('to_hsv')

to_rgb = Fa(uid="5fd5814b4f6511e690ec0242b2ebf0f7",
            name="to_rgb",
            description="",
            category="",
            nodemodule="see_example.library.image",
            nodeclass="to_rgb",
            inputs=(dict(name="img", interface=IImage),),
            outputs=(dict(name="img", interface=IImage),),
            )

__all__.append('to_rgb')

lower = Fa(uid="eec8694c528011e6b255d4bed973e64a",
           name="lower",
           description="",
           category="",
           nodemodule="see_example.library.image",
           nodeclass="lower",
           inputs=(dict(name="img", interface=IImage),
                   dict(name="threshold", interface=ISequence),),
           outputs=(dict(name="img", interface=IImage),),
           )

__all__.append('lower')

upper = Fa(uid="f2ef5332528011e6b255d4bed973e64a",
           name="upper",
           description="",
           category="",
           nodemodule="see_example.library.image",
           nodeclass="upper",
           inputs=(dict(name="img", interface=IImage),
                   dict(name="threshold", interface=ISequence),),
           outputs=(dict(name="img", interface=IImage),),
           )

__all__.append('upper')

avg = Fa(uid="ccb6d026531311e6a55fd4bed973e64a",
           name="average",
           description="",
           category="",
           nodemodule="see_example.library.image",
           nodeclass="average",
           inputs=(dict(name="img", interface=IImage),
                   dict(name="scaling", interface=ISequence),),
           outputs=(dict(name="val", interface=IFloat),),
           )

__all__.append('avg')

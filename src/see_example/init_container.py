from see_scripts.see_client import (connect, get_ro_def, get_single_by_name,
                                    log_to_see, register_ro, remove_ro)

container = "see.example"
session = log_to_see("revesansparole", "r")

# create container if it doesn't exist yet
try:
    cid = get_single_by_name('container', container, session)
    remove_ro(session, cid, True)
except KeyError:
    pass

cid = register_ro(session,
                  'container',
                  dict(name=container, id="6721cbfc526f11e6b255d4bed973e64a"))


# upload image on SEEweb
roid = '4f3a11b6528311e6b255d4bed973e64a'

if get_ro_def(roid, session) is not None:
    remove_ro(session, roid, False)

img = dict(id=roid, name="lena")
pid = register_ro(session, 'ro', img)
connect(session, cid, pid, 'contains')

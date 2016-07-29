import json

from see_scripts.see_client import (connect, get_single_by_name,
                                    log_to_see, register_ro, remove_ro)
from see_scripts.wlf_client import upload_prov


pth = "prov_size.json"
container = "expe1.executions"
session = log_to_see("revesansparole", "r")

# check existence of top container
top_cid = get_single_by_name('container', "see.ex.expe1", session)

# check existence of container
try:
    cid = get_single_by_name('container', container, session)
    remove_ro(session, cid, True)
except KeyError:
    pass
cid = register_ro(session,
                  'container',
                  dict(name=container, id="f2146486526f11e6b255d4bed973e64a"))
connect(session, top_cid, cid, 'contains')

# open provenance file
with open(pth, 'r') as f:
    prov = json.load(f)


# external inputs SEE
uid = get_single_by_name('ro', 'tryout_binarization_0', session)
prov['data'][2]['type'] = 'ref'
prov['data'][2]['value'] = uid

# upload provenance
upload_prov(session, prov, cid, overwrite=True)

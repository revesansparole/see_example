import json

from see_scripts.see_client import (connect, get_ro_def, get_single_by_name,
                                    log_to_see, register_ro, remove_ro)
from see_scripts.wlf_client import upload_prov


def get_data_def(did):
    for data in prov['data']:
        if data['id'] == did:
            return data

    raise KeyError("no data recorded with this id")


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

# find associated workflow on SEE
uid = get_single_by_name('workflow', 'see_ex_size', session)
prov['workflow'] = uid

# find lena id on SEE
uid = get_single_by_name('ro', 'lena', session)
prov['data'][0]['type'] = 'ref'
prov['data'][0]['value'] = uid

uid = get_single_by_name('ro', 'tryout_binarization_0', session)
prov['data'][2]['type'] = 'ref'
prov['data'][2]['value'] = uid

# upload provenance
upload_prov(session, prov, cid, overwrite=True)
# # check that all input data that correspond to remote data on the platform
# # are actually registered on the platform
# input_data = set()
# for pexec in prov["executions"]:
#     for port in pexec['inputs']:
#         if port['data'] is not None:
#             input_data.add(port['data'])
#
# input_ref = set()
# for did in input_data:
#     ddata = get_data_def(did)
#     if ddata['type'] == 'ref':
#         if get_ro_def(session, ddata['value']) is None:
#             msg = "data '%s' used as input is not registered on SEE" % ddata['value']
#             raise UserWarning(msg)
#         else:
#             input_ref.add(ddata['value'])
#
# # upload output data as separate Ros
# output_data = set()
# for pexec in prov["executions"]:
#     for port in pexec['outputs']:
#         if port['data'] is not None:
#             output_data.add(port['data'])
#
# for i, did in enumerate(output_data):
#     # upload object as new data
#     ddata = dict(get_data_def(did))
#     # ddata['type'] = "$ref"
#     ddata['name'] = "%s_%d" % (prov['name'], i)
#     did = register_ro(session, 'ro', ddata)
#     connect(session, cid, did, 'contains')
#
# # upload prov on SEEweb
# if 'id' in prov:
#     if get_ro_def(session, prov['id']) is not None:
#         remove_ro(session, prov['id'], False)
#
# pid = register_ro(session, 'workflow_prov', prov)
# connect(session, cid, pid, 'contains')
#
# # connect prov to data manipulated
# for did in input_ref:
#     connect(session, pid, did, 'consume')
#
# for did in output_data:
#     connect(session, pid, did, 'produce')

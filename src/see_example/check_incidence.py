from openalea.container import Graph

from see_scripts.see_client import get_single_by_name, log_to_see, search

session = log_to_see("revesansparole", "r")

g = Graph()
vprop = {}


def get_by_id(uid):
    for vid, (name, roid) in vprop.items():
        if roid == uid:
            return vid

    raise KeyError("no RO registered with this id")


# retrieve id of workflow that want to be modified
wid = get_single_by_name('workflow', "see_ex_binarize", session)
rid = g.add_vertex()
vprop[rid] = ("see_ex_binarize", wid)

# find all executions of this workflow
query = dict(type='workflow_prov', use=wid)
exec_ids = search(query, session)
for eid in exec_ids:
    vid = g.add_vertex()
    vprop[vid] = ('wprov', eid)
    g.add_edge(rid, vid)


# find all data produced by these executions
produced_data = set()
for eid in exec_ids:
    pid = get_by_id(eid)
    query = dict(type='workflow_prov', produce=eid)
    for did in search(query, session):
        if did in produced_data:
            vid = get_by_id(did)
        else:
            produced_data.add(did)
            vid = g.add_vertex()
            vprop[vid] = ('data', did)
        g.add_edge(pid, vid)

# find all executions that consume these data
exec_ids = set()
for did in produced_data:
    pid = get_by_id(did)
    query = dict(type='workflow_prov', consume=did)
    for eid in search(query, session):
        if eid in exec_ids:
            vid = get_by_id(eid)
        else:
            exec_ids.add(eid)
            vid = g.add_vertex()
            vprop[vid] = ('wprov', eid)
        g.add_edge(pid, vid)

# find set of data that have been modified
produced_data = set()
for eid in exec_ids:
    pid = get_by_id(eid)
    query = dict(type='workflow_prov', produce=eid)
    for did in search(query, session):
        if did in produced_data:
            vid = get_by_id(did)
        else:
            produced_data.add(did)
            vid = g.add_vertex()
            vprop[vid] = ('data', did)
        g.add_edge(pid, vid)


# create dot graph
def title(vid):
    typ, uid = vprop[vid]
    txt = typ + "_" + uid[:10]
    return txt


with open("graph.txt", 'w') as f:
    f.write("digraph {\n")
    for eid in g.edges():
        st = title(g.source(eid))
        tt = title(g.target(eid))
        f.write(" %s -> %s\n" % (st, tt))
    f.write("}\n")


# transform it into png
import subprocess

subprocess.call("dot -Tpng -ograph.png graph.txt", shell=True)

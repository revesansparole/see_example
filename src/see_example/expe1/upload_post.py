from see_scripts.see_client import (connect, get_single_by_name,
                                    log_to_see)

session = log_to_see("revesansparole", "r")

top = get_single_by_name(session, 'container', "see.example")
cid = get_single_by_name(session, 'container', "see.ex.expe1")
connect(session, top, cid, 'contains')
cid = get_single_by_name(session, 'container', "see.ex.expe1.nodes")
connect(session, top, cid, 'contains')

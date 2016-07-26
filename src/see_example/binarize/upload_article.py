from see_scripts.see_client import (connect, get_single_by_name, get_ro_def,
                                    log_to_see, register_ro, remove_ro)

session = log_to_see("revesansparole", "r")

# check existence of container
cid = get_single_by_name(session, 'container', "see.ex.binarize")

# upload article on SEEweb
aid = 'd3cf5fee526511e6b255d4bed973e64a'

if get_ro_def(session, aid) is not None:
    remove_ro(session, aid, False)

article = dict(id=aid, name="see.ex.binarize.article")
pid = register_ro(session, 'article', article)
connect(session, cid, pid, 'contains')

# create use link for article on workflow
wid = get_single_by_name(session, 'workflow', "see_ex_binarize")
connect(session, pid, wid, 'use')

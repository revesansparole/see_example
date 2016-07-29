from see_scripts.see_client import (connect, get_single_by_name,
                                    log_to_see)

session = log_to_see("revesansparole", "r")

top = get_single_by_name('container', "see.example", session)
cid = get_single_by_name('container', "see.ex.library", session)
connect(session, top, cid, 'contains')

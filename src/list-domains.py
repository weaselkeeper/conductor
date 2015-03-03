#!/usr/bin/env  python

import libvirt
conn = libvirt.open("qemu:///session")

for dom_id in conn.listDomainsID():
    dom = conn.lookupByID(dom_id)
    infos = dom.info()
    print dom_id, dom.name()

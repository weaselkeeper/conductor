#!/usr/bin/env  python
""" List running domains on the local qemu session """
import libvirt
conn = libvirt.open("qemu:///session")

for dom_id in conn.listDomainsID():
    dom = conn.lookupByID(dom_id)
    infos = dom.info()
    print dom_id, dom.name()

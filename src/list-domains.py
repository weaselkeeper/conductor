#!/usr/bin/env  python

import libvirt
conn=libvirt.open("qemu:///session")

for id in conn.listDomainsID():
   dom = conn.lookupByID(id)
   infos = dom.info()
   print id, dom.name()

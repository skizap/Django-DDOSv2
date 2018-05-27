# -*- coding: utf-8 -*-

class DNSFlood():
    def __init__(self, dst, qname, qtype, count):
        self.dst   = dst
        self.qname = qname
        self.qtype = qtype
        self.count = count

#!/usr/bin/env python2
# -*- coding: utf-8-*-


class Ca:
    def __init__(good, v,z):
        good.name = v+z
        print "我被构造出来了"

    def pr(self):
        print "a--->"


ia = Ca("Jeapedu","godie")
ia.pr
Ca.pr(ia)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickledb
import time

def load(location, option):
    return pcache(location, option)

class pcache:

    def __init__(self, location, option):
        self.cache = pickledb.load(location, option)
    
    def set(self, key, value, dur):
        try:
            dur = float(dur)
        except ValueError as e:
            print e
            return False
        self.cache.set(key, {
            "value": value,
            "expire": time.time() + dur if dur > 0.0 else 0.0
        })
        return True

    def get(self, key):
        c = self.cache.get(key)
        if c is None:
            return None
        exp = c.get("expire")
        if time.time() >= exp:
            # expired
            self.cache.rem(key)
            return None
        return c.get("value")

    def delete(self, key):
        self.cache.rem(key)
    
    def expire(self, key, dur):
        try:
            dur = float(dur)
        except ValueError as e:
            print e
            return False
        c = self.cache.get(key)
        if c is not None:
            c["expire"] = time.time() + dur if dur > 0.0 else 0.0
            self.cache.set(key, c)
            return True
        return False
    
    def drop(self):
        self.cache.deldb()
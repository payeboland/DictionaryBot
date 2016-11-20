#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3



def find(word):
    conn = sqlite3.connect('dic.db')
    c = conn.cursor()
    c.execute("SELECT mean FROM dictionary WHERE word = '%s'" % word)
    
    return c.fetchone()[0]




# -*- coding: utf-8 -*-
'''
This entire problem is a horrible mess of confusion and bad ideas.
'''

quality_max = 50
quality_min = 0
sell_in_threshold = 0

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def rule_default(self, item):
        item.dec('sell_in')

        if item.sell_in < sell_in_threshold:
            item.dec('quality', 2)
        else:
            item.dec('quality')

    def rule_backstage(self, item):
        if item.sell_in < sell_in_threshold:
            item.change('quality', 0)
        elif item.sell_in < 6:
            item.inc('quality', 3)
        elif item.sell_in < 11:
            item.inc('quality', 2)
        else:
            item.inc('quality')

        item.dec('sell_in')

    def rule_brie(self, item):
        item.dec('sell_in')

        if item.sell_in < sell_in_threshold:
            item.inc('quality', 2)
        else:
            item.inc('quality')

    def rule_noop(self, item):
        pass

    def rules(self, item):
        backstage = "Backstage passes to a TAFKAL80ETC concert"
        brie = "Aged Brie"
        sulfuras = "Sulfuras, Hand of Ragnaros"

        if item.name == backstage:
            self.rule_backstage(item)
        elif item.name == brie:
            self.rule_brie(item)
        elif item.name == sulfuras:
            self.rule_noop(item)
        else:
            self.rule_default(item)

    def update_quality(self):
        for item in self.items:
            self.rules(item)

class Item(object):

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def change(self, p, value):

        if p == 'sell_in':
            self.sell_in += value

        if p == 'quality':
            nq = self.quality + value
            if nq > quality_max:
                nq = quality_max
            elif nq < quality_min:
                nq = quality_min

            if self.quality != nq:
                self.quality = nq

    def inc(self, p, value=1):
        self.change(p, value)

    def dec(self, p, value=-1):
        if value > 0:
            value = -value
        self.change(p, value)

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

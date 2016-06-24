# -*- coding: utf-8 -*-
'''
This entire problem is a horrible mess of confusion and bad ideas.
'''

backstage = "Backstage passes to a TAFKAL80ETC concert"
brie = "Aged Brie"
sulfuras = "Sulfuras, Hand of Ragnaros"
cake = "Conjured Mana Cake"
quality_max = 50
quality_min = 0
sell_in_threshold = 0

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def rules(self, item):

        # rule 1 - increment quality
        if item.name in [backstage, brie] \
        and item.quality < quality_max:
            item.inc('quality')

        # rule 2 - increment quality
        if item.name == backstage \
        and item.quality < quality_max:
            if item.sell_in < 11:
                item.inc('quality')

            if item.sell_in < 6:
                item.inc('quality')

        # rule 3 - decrease sell_in
        if item.name != sulfuras:
            item.dec('sell_in')

        # rule 4 - decrease quality
        if item.name not in [backstage, brie, sulfuras] \
        and item.quality > quality_min:
            item.dec('quality')

        # rule 5 - decrease quality
        if item.sell_in < sell_in_threshold \
        and item.name not in [backstage, brie, sulfuras] \
        and item.quality > quality_min:
            item.dec('quality')

        # rule 6 - decrease quality
        if item.sell_in < sell_in_threshold \
        and item.name == backstage:
            item.quality = 0

        # rule 7 - increase quality
        if item.sell_in < sell_in_threshold \
        and item.name == brie \
        and item.quality < quality_max:
            item.inc('quality')

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
            self.quality += value

    def inc(self, p, value=1):
        self.change(p, value)

    def dec(self, p, value=-1):
        if value > 0:
            value = -value
        self.change(p, value)

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

# -*- coding: utf-8 -*-
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONCERT_TICKETS = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"
AGED_BRIE_QUALITY_INCREASE_NEGATIVE_SELLIN = 2
DEFAULT_QUALITY_UNIT = 1
DOUBLE_QUALITY_UNIT = 2


TOP_QUALITY = 50
MIN_QUALITY = 0

CLOSE_DATE_QUALITY_INCREASE = 2
CLOSE_DATE_DAYS_LIMIT = 10
VERY_CLOSE_DATE_QUALITY_INCREASE = 3
VERY_CLOSE_DATE_DAYS_LIMIT = 5

DEFAULT_SELL_IN_UNIT = 1

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == SULFURAS:
                self.update_sulfuras(item)
            elif item.name == AGED_BRIE:
                self.update_aged_brie(item)
            elif item.name == CONCERT_TICKETS:
                self.update_concert_tickets(item)
            else:
                self.update_normal_item(item)

    def update_normal_item(self, item):
        if item.sell_in < 0:
            item.quality -= DOUBLE_QUALITY_UNIT
            item.sell_in -= DEFAULT_SELL_IN_UNIT
        else:
            item.sell_in -= DEFAULT_SELL_IN_UNIT
            item.quality -= DEFAULT_QUALITY_UNIT
        if item.quality < MIN_QUALITY:
            item.quality = MIN_QUALITY
        elif item.quality > TOP_QUALITY:
            item.quality = TOP_QUALITY

    def update_sulfuras(self, item):
        item.quality = 80

    def update_aged_brie(self, item):
        if item.sell_in < 0:
            item.quality += AGED_BRIE_QUALITY_INCREASE_NEGATIVE_SELLIN
        elif item.quality < TOP_QUALITY:
            item.quality += DEFAULT_QUALITY_UNIT
        item.sell_in -= DEFAULT_SELL_IN_UNIT

    def update_concert_tickets(self, item):
        if item.sell_in < 0:
            item.quality = MIN_QUALITY
        elif item.sell_in <= VERY_CLOSE_DATE_DAYS_LIMIT:
            item.quality += VERY_CLOSE_DATE_QUALITY_INCREASE
        elif item.sell_in <= CLOSE_DATE_DAYS_LIMIT:
            item.quality += CLOSE_DATE_QUALITY_INCREASE
        else:
            item.quality += DEFAULT_QUALITY_UNIT
        item.sell_in -= DEFAULT_SELL_IN_UNIT


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

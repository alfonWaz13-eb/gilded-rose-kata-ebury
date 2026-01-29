# -*- coding: utf-8 -*-

class GildedRose(object):

    SPECIAL_ITEMS = [
        "Aged Brie",
        "Backstage passes to a TAFKAL80ETC concert",
        "Sulfuras, Hand of Ragnaros",
    ]

    def __init__(self, items):
        self.items = items

    def _calculate_quality(self, item):
        # dummy items
        if item.name not in self.SPECIAL_ITEMS and item.quality > 0:
            item.quality = item.quality - 1

            if item.name == "Conjured Items":
                item.quality = item.quality - 1
        # special items Aged and Basckstage
        else:
            if item.quality < 50:
                # Aged Brie
                item.quality = item.quality + 1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1

        if item.sell_in < 0:
            if item.name not in self.SPECIAL_ITEMS and item.quality > 0:
                item.quality = item.quality - 1

                if item.name == "Conjured Items":
                    item.quality = item.quality - 1

            elif item.name=="Backstage passes to a TAFKAL80ETC concert":
                item.quality = item.quality - item.quality
            else:
                # Aged Brie
                if item.quality < 50:
                    item.quality = item.quality + 2

        return item.quality

    def _calculate_sell_in(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1

        return item.sell_in

    def update_quality(self):
        for item in self.items:
            item.sell_in = self._calculate_sell_in(item)
            item.quality = self._calculate_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

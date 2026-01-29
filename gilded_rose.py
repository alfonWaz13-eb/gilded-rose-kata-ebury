# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def _update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1

    def update_quality(self):
        for item in self.items:
            item.update_item()


class Item:
    def __init__(self, name, sell_in, quality, sell_in_change_rate=-1):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self._change_rate = lambda x: -1 if self.sell_in >= 0 else -2
        self._sell_in_change_rate = sell_in_change_rate

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def _update_quality(self):
        self.quality += self._change_rate()

    def _check_quality_limits(self):
        self.quality = max(min(self.quality, 50), 0)

    def _update_sell_in(self):
        self.sell_in += self._sell_in_change_rate

    def update_item(self):
        self._update_sell_in()
        self._update_quality()
        self._check_quality_limits()


class AgedBrie(Item):
    def __init__(self, **kwargs):
        super().__init__(name="Aged Brie", **kwargs)
        self._change_rate = lambda x: 1 if self.sell_in >= 0 else 2


class Sulfuras(Item):
    def __init__(self, **kwargs):
        super().__init__(name = "Sulfuras, Hand of Ragnaros", quality=80, sell_in_change_rate=0, **kwargs)
        self._change_rate = lambda x: 0


class BackstagePasses(Item):
    def __init__(self, **kwargs):
        super().__init__(name="Backstage Passes", **kwargs)
        self._change_rate = lambda x: 1 if self.sell_in >= 11 else 2 if self.sell_in >= 6 else 3

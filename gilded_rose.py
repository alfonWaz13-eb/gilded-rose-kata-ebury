# -*- coding: utf-8 -*-
from constants import *

class ItemUpdater:

    def __init__(self, item):
        self.item = item

    def update(self):
        self.update_quality()
        self.update_sell_in()
        self.update_expired()

    def update_quality(self):
        raise NotImplementedError

    def update_sell_in(self):
        self.item.sell_in -= 1

    def update_expired(self):
        pass

    def increase_quality(self, amount=1):
        self.item.quality = min(MAX_QUALITY, self.item.quality + amount)

    def decrease_quality(self, amount=1):
        self.item.quality = max(MIN_QUALITY, self.item.quality - amount)

    def is_expired(self):
        return self.item.sell_in < 0


class ItemUpdaterFactory:

    @staticmethod
    def create(item):
        updater_cls = REGISTRY.get(item.name)
        if updater_cls:
            return updater_cls(item)

        if item.name.lower().startswith(CONJURED_PREFIX):
            return ConjuredUpdater(item)

        return NormalItemUpdater(item)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = ItemUpdaterFactory.create(item)
            updater.update()


class NormalItemUpdater(ItemUpdater):

    def update_quality(self):
        self.decrease_quality(1)

    def update_expired(self):
        if self.is_expired():
            self.decrease_quality(1)


class ConjuredUpdater(ItemUpdater):

    def update_quality(self):
        self.decrease_quality(2)

    def update_expired(self):
        if self.is_expired():
            self.decrease_quality(2)


class AgedBrieUpdater(ItemUpdater):

    def update_quality(self):
        self.increase_quality(1)

    def update_expired(self):
        if self.is_expired():
            self.increase_quality(1)


class BackstagePassUpdater(ItemUpdater):

    def update_quality(self):
        if self.item.sell_in <= 5:
            self.increase_quality(3)
        elif self.item.sell_in <= 10:
            self.increase_quality(2)
        else:
            self.increase_quality(1)

    def update_expired(self):
        if self.is_expired():
            self.item.quality = MIN_QUALITY


class SulfurasUpdater(ItemUpdater):

    def update(self):
        pass

REGISTRY = {
    AGED_BRIE: AgedBrieUpdater,
    BACKSTAGE_PASSES: BackstagePassUpdater,
    SULFURAS: SulfurasUpdater,
}


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

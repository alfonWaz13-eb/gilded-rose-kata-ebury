from available_items import SULFURAS, BACKSTAGE_PASS, AGED_BRIE, AgedBrie, BackstagePass, Sulfuras, NormalItem

class GildedRose(object):

    AVAILABLE_ITEMS = {
        AGED_BRIE: AgedBrie,
        BACKSTAGE_PASS: BackstagePass,
        SULFURAS: Sulfuras,
        NormalItem: NormalItem
    }

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            gilded_rose_product= self.AVAILABLE_ITEMS[item](sell_in=item.sell_in, quality=item.quality)
            gilded_rose_product.update_state()
            item.quality = gilded_rose_product.quality
            item.sell_in = gilded_rose_product.sell_in

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)



from gilded_rose import GildedRose, Item, AgedBrie, Backstage, Sulfuras, Conjured


def test_foo():
    items = list()
    items.append(Item("foo", 0, 10))
    items.append(AgedBrie("Aged Brie", 0, 0))
    items.append(Backstage("Backstage passes to a TAFKAL80ETC concert", 0, 0))
    items.append(Conjured("Conjured Item", 0, 4))
    items.append(Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80))
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    for item in items:
        assert item.__repr__() in [
            "foo, -1, 9",
            "Aged Brie, -1, 1",
            "Backstage passes to a TAFKAL80ETC concert, -1, 3",
            "Conjured Item, -1, 2",
            "Sulfuras, Hand of Ragnaros, -1, 80"
        ]
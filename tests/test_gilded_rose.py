from gilded_rose import GildedRose, Item


def test_foo():
    items = list()
    items.append(Item("foo", 0, 10))
    items.append(Item("Aged Brie", 0, 0))
    items.append(Item("Backstage passes to a TAFKAL80ETC concert", 0, 0))
    items.append(Item("Sulfuras, Hand of Ragnaros", 0, 80))
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    for item in items:
        assert item.__repr__() in ["foo, -1, 8", "Aged Brie, -1, 2", "Backstage passes to a TAFKAL80ETC concert, -1, 0", "Sulfuras, Hand of Ragnaros, 0, 80"]
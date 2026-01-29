from gilded_rose import GildedRose, Item


def test_general_item_reduces_quality_every_day():
    item = Item("foo", 10, 10)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 9
    assert item.quality == 9

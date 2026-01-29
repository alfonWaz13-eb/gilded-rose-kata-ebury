from gilded_rose import GildedRose, Item


def test_foo():
    item = Item("foo", 0, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "foo"asdas
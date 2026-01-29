from gilded_rose import GildedRose, Item


def test_foo():
    item = Item("foo", 0, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "foo"

def test_normal_item_when_sellin_positive():
    item = Item("Normal Item", 10, 20)
    gilder_rose = GildedRose([item])
    gilder_rose.update_quality()

    assert item.sell_in == 9
    assert item.quality == 19

def test_normal_item_when_sellin_negative():
    item = Item("Normal Item", -1, 20)
    gilder_rose = GildedRose([item])
    gilder_rose.update_quality()

    assert item.sell_in == -2
    assert item.quality == 18

def test_normal_item_when_sellin_negative_quality_zero():
    item = Item("Normal Item", -1, 0)
    gilder_rose = GildedRose([item])
    gilder_rose.update_quality()

    assert item.sell_in == -2
    assert item.quality == 0

def test_aged_brie_increase_quality():
    item = Item("Aged Brie", 2, 0)
    gilder_rose = GildedRose([item])
    gilder_rose.update_quality()

    assert item.sell_in == 1
    assert item.quality == 1

def test_aged_brie_increase_quality_max_50():
    item = Item("Aged Brie", 2, 50)
    gilder_rose = GildedRose([item])
    gilder_rose.update_quality()

    assert item.sell_in == 1
    assert item.quality == 50

def test_aged_brie_when_sellin_negative():
    item = Item("Aged Brie", -1, 48)
    gilder_rose = GildedRose([item])
    gilder_rose.update_quality()

    assert item.sell_in == -2
    assert item.quality == 50

def test_sulfuras_no_change():
    item = Item("Sulfuras, Hand of Ragnaros", 10, 80)
    gilder_rose = GildedRose([item])
    gilder_rose.update_quality()

    assert item.sell_in == 10
    assert item.quality == 80

def test_sulfuras_sellin_dont_change_over_time():
    item = Item("Sulfuras, Hand of Ragnaros", 9, 80)
    gilder_rose = GildedRose([item])
    gilder_rose.update_quality()
    days = 20
    for _ in range(days):
        gilder_rose.update_quality()
    assert item.sell_in == 9

def test_backstage_pass_increase_quality_more_than_10_days():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    gilder_rose = GildedRose([item])
    gilder_rose.update_quality()

    assert item.sell_in == 14
    assert item.quality == 21

def test_backstage_pass_increase_quality_between_6_and_10_days():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 25)
    gilder_rose = GildedRose([item])
    gilder_rose.update_quality()

    assert item.sell_in == 9
    assert item.quality == 27

def test_backstage_pass_increase_quality_between_0_and_5_days():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 30)
    gilder_rose = GildedRose([item])
    gilder_rose.update_quality()

    assert item.sell_in == 4
    assert item.quality == 33

def test_backstage_pass_increase_quality_between_0_and_5_days_and_quality_not_higher_than_50():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 50)
    gilder_rose = GildedRose([item])
    gilder_rose.update_quality()

    assert item.sell_in == 4
    assert item.quality == 50


def test_backstage_pass_quality_drops_to_zero_after_concert():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 40)
    gilder_rose = GildedRose([item])
    gilder_rose.update_quality()

    assert item.sell_in == -1
    assert item.quality == 0


def test_print_item():
    item = Item("Test Item", 5, 10)
    assert repr(item) == "Test Item, 5, 10"






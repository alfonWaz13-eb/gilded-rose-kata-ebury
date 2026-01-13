import pytest
from gilded_rose import (
    Item, GildedRose, ItemUpdaterFactory, NormalItemUpdater, ConjuredUpdater,
    AgedBrieUpdater, BackstagePassUpdater, SulfurasUpdater,
    MAX_QUALITY, MIN_QUALITY,
    AGED_BRIE, BACKSTAGE_PASSES, SULFURAS
)


def test_factory_returns_correct_updater():
    items = [
        Item(AGED_BRIE, 10, 10),
        Item(BACKSTAGE_PASSES, 10, 10),
        Item(SULFURAS, 0, 80),
        Item("Conjured Mana Cake", 5, 10),
        Item("Normal Item", 5, 10)
    ]

    updaters = [ItemUpdaterFactory.create(item) for item in items]

    assert isinstance(updaters[0], AgedBrieUpdater)
    assert isinstance(updaters[1], BackstagePassUpdater)
    assert isinstance(updaters[2], SulfurasUpdater)
    assert isinstance(updaters[3], ConjuredUpdater)
    assert isinstance(updaters[4], NormalItemUpdater)


def test_normal_item_degrades():
    item = Item("Normal Item", 10, 20)
    updater = NormalItemUpdater(item)
    updater.update()
    assert item.sell_in == 9
    assert item.quality == 19

def test_normal_item_expired_degrades_twice():
    item = Item("Normal Item", 0, 20)
    updater = NormalItemUpdater(item)
    updater.update()
    assert item.sell_in == -1
    assert item.quality == 18

def test_normal_item_quality_never_negative():
    item = Item("Normal Item", 5, 0)
    updater = NormalItemUpdater(item)
    updater.update()
    assert item.quality == 0

def test_conjured_item_degrades_twice():
    item = Item("Conjured Mana Cake", 10, 20)
    updater = ConjuredUpdater(item)
    updater.update()
    assert item.sell_in == 9
    assert item.quality == 18

def test_conjured_item_expired_degrades_double_twice():
    item = Item("Conjured Mana Cake", 0, 20)
    updater = ConjuredUpdater(item)
    updater.update()
    assert item.sell_in == -1
    assert item.quality == 16

def test_conjured_quality_never_negative():
    item = Item("Conjured Mana Cake", 0, 1)
    updater = ConjuredUpdater(item)
    updater.update()
    assert item.quality == 0

def test_aged_brie_increases_quality():
    item = Item(AGED_BRIE, 10, 10)
    updater = AgedBrieUpdater(item)
    updater.update()
    assert item.sell_in == 9
    assert item.quality == 11

def test_aged_brie_max_quality():
    item = Item(AGED_BRIE, 10, MAX_QUALITY)
    updater = AgedBrieUpdater(item)
    updater.update()
    assert item.quality == MAX_QUALITY

@pytest.mark.parametrize("sell_in,expected_inc", [(15,1), (10,2), (5,3)])
def test_backstage_pass_increases_quality(sell_in, expected_inc):
    item = Item(BACKSTAGE_PASSES, sell_in, 10)
    updater = BackstagePassUpdater(item)
    updater.update()
    assert item.quality == 10 + expected_inc

def test_backstage_pass_after_concert():
    item = Item(BACKSTAGE_PASSES, 0, 10)
    updater = BackstagePassUpdater(item)
    updater.update()
    assert item.quality == MIN_QUALITY

def test_sulfuras_immutable():
    item = Item(SULFURAS, 0, 80)
    updater = SulfurasUpdater(item)
    updater.update()
    assert item.sell_in == 0
    assert item.quality == 80

def test_gilded_rose_update_quality():
    items = [
        Item("Normal Item", 5, 10),
        Item(AGED_BRIE, 5, 10),
        Item(BACKSTAGE_PASSES, 5, 10),
        Item(SULFURAS, 0, 80),
        Item("Conjured Mana Cake", 5, 10)
    ]

    gr = GildedRose(items)
    gr.update_quality()

    # Normal
    assert items[0].sell_in == 4
    assert items[0].quality == 9
    # Brie
    assert items[1].sell_in == 4
    assert items[1].quality == 11
    # Backstage
    assert items[2].sell_in == 4
    assert items[2].quality == 13
    # Sulfuras
    assert items[3].sell_in == 0
    assert items[3].quality == 80
    # Conjured
    assert items[4].sell_in == 4
    assert items[4].quality == 8

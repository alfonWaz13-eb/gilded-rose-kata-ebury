# ⚔️ Gilded Rose Kata: A Refactoring Guide

Welcome, team! 🎉  
Today, we’ll be working together on the famous **Gilded Rose Kata**. It’s a fun programming exercise that’s great for practice, learning, and collaborating in squads.

## Background

We run the **Gilded Rose Inn**, managed by Allison the innkeeper.  
Our job is to handle inventory: buying and selling various goods. Each item has:

- **SellIn**: Number of days left to sell it
- **Quality**: How valuable it is

Every day, our system automatically updates these numbers!

## General Rules (Business Rules)

- Every item loses **1 Quality** and **1 SellIn** each day.
- If the sell-by date is **past** (SellIn < 0), **Quality** drops **twice as fast** (–2/day).
- **Quality never goes below 0**, and never above **50** (some exceptions).

### Special Item Rules (extra rules)

- **Aged Brie**:  
  - Gets better with age: **Quality increases** each day (up to 50).
  - if sellin <0 in aged brie, quality increases in two.

- **Sulfuras, Hand of Ragnaros**:  
  - Legendary, never sold!  
  - **Quality always 80** and never changes.
  
- **Backstage Passes**:  
  - Improve as the concert approaches:
    - +1 Quality per day
    - If 10 days left: **+2 Quality**
    - If 5 days left: **+3 Quality**
    - **After the concert (SellIn < 0): Quality drops to 0**

- **Conjured Items (TO BE IMPLEMENTED)**:  
  - Spoil faster: **Quality drops twice as fast as normal items**.

**Run the `gilded_rose_example.py` file to see the behavior of the system.**

### Your Mission

- **Add support for "Conjured" items**: They go bad twice as fast as regular items.
- You can change the `UpdateQuality` method and add any code you need.
- **But:** Don’t change the `Item` class or the `Items` property (the goblin in the corner will get very angry! 🧙‍♂️).

## Kata Guidelines

- You cannot refactor **anything** until you have **100% test coverage** on the existing code.
- Babby steps (atomic commits): Every relevant change should be committed to the repository with clear messages.
Example: one commit for adding a small group of tests, another for refactoring a specific method, etc.
- **Everytime someone makes a commit, another team member should take the lead**, pulling the latest changes and sharing their screen.
- Tests should clearly express **what** business rule is being tested, not just the function being called.
Example: `test_quality_of_item_is_never_more_than_50` is good, while `test_item_quality` is not.
- The goal is not to rewrite the code from scratch, but to improve its design incrementally, ensuring that the existing tests do not break in the process.
- You are free to use any library or framework that helps you achieve the goal, but should not alter the existing functionality.
- **Once you finish refactoring the code, add the new feature for "Conjured" items along with the necessary tests.**

Let’s have some fun and see how creative we can get! 🚀

---

## GETTING STARTED

1. **Create a new branch for your squad** of this repository in your own GitHub account, so you can make changes with your colleagues and work over the same project
2. Clone the repository in your local machine.
3. Create a Python virtual environment
```
python3 -m venv .venv
source .venv/bin/activate
```
4. Install dependencies
```
pip install -r requirements.txt
```
5. Make sure the tests run
```
python -m pytest
```

---

### TEST COVERAGE

A vital part of this exercise is ensuring that the existing code is completely covered by tests before beginning any refactoring. This allows us to quickly detect if any change breaks the existing functionality.

To check the test coverage, a `Makefile` has been included with a specific task for this purpose. Simply execute the following command in your terminal:

```bash
make test-coverage
```
**In case all tests do not pass, the report won't be generated.**

<img src="images/project_tree.png" alt="Estructura del Proyecto" width="500"/>

<img src="images/main_file_coverage.png" alt="Reporte de Cobertura del Archivo Principal" width="600"/>

---


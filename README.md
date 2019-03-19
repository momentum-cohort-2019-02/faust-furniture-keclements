# Small Business Website

Faust Furniture is a local vintage furniture retailer with a constantly changing selection. Their showroom has limited floor space so they built a website to show all their inventory.

They only need pages to show what products they currently have -- no e-commerce options. But they've had trouble maintaining the site because they can't easily synchronize the items on the page with the continuously changing items in stock.

Your task is to create a Django app for Faust Furniture. Their current inventory is in a `.csv` file and you will have to import that data.

## Requirements

There should be 2 types of pages: the home page, which shows all available products, and a single-product detail page.

- [ ] Create a `Product` `model` with attributes matching the CSV file headers.
- [ ] Create a `method` that identifies items on clearance and adjusts the price.
- [ ] Apply a 10% discount on the price for items that are in 'good' condition.
- [ ] Apply a 20% discount on the price for items that are in 'average' condition.
- [ ] For each clearance item on the page, make sure that the site indicates that the item is on clearance (next to the price, for instance).
- [ ] Do not show items on the site that have a quantity of 0.
- [ ] You will need to add the Product model to the admin to allow users to update the inventory. For the condition, the user should have a dropdown selection of 'very good', 'good', and 'average' conditions.
- [ ] This site should be designed to be usable, but does not have to be ornate. 
- [ ] "Aesthetically neutral" is a good way to go. 
- [ ] Specifically, you need to demonstrate that you can use the correct HTML elements for items and write CSS to style them.

- [ ] Create a `Product` model with attributes matching the CSV file headers.
- [ ] Create a `method` that identifies items on clearance and adjusts the price.
    - [ ] Apply a 10% discount on the price for items that are in 'good' condition.
    - [ ] pply a 20% discount on the price for items that are in 'average' condition.
    - [ ] For each clearance item on the page, make sure that the site indicates that the item is on clearance (next to the price, for instance).
- [ ] Do not show items on the site that have a quantity of 0.

You will need to add the `Product` `model` to the `admin` to allow users to update the inventory. For the condition, the _user should have a dropdown_ selection of 'very good', 'good', and 'average' conditions.

This site should be designed to be usable, but does not have to be ornate. "Aesthetically neutral" is a good way to go. Specifically, you need to demonstrate that you can use the correct HTML elements for items and write CSS to style them.

The [CSV file is in this repository](inventory.csv).

## Extra Challenges

If you complete the above, here are suggestions to keep going.

1. Organize the items by furniture category on the product list page.
2. Make a new home page that shows the furniture categories as options that the user can select. When they click on a category, they go to a product list page that only shows items of the category they selected. e.g. if a user selects 'tables', they will only see the items that are in the 'tables' category.

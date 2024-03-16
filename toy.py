# To view the generated HTML page, run:
#     python3 toy.py > MISC.html
#

# The main page of the html
PAGE_HTML = """
<p>Welcome, {name}!</p>
<p>Products:</p>
<ul>
{products}
</ul>"""

PRODUCT_HTML = """    <li>{product_name}: ${product_price}</li>
"""

def make_page(username, products):
    product_html = ""
    for name, price in products.items():
        product_html += PRODUCT_HTML.format(
            product_name=name,
            product_price=price
        )

    return PAGE_HTML.format(name=username, products=product_html)

print(make_page("Hafs", {"Apple": 1.00,
                    "Fig": 1.50,
                   "Pomegranate": 3.25}))


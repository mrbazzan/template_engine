
def render_function(context, do_dots):
    c_name = context["name"] 
    c_products = context["products"]
    c_lower = context["lower"]

    result = []
    append_result = result.append
    extend_result = result.extend
    to_str = str

    extend_result([
        "<p> Welcome, ",
        to_str(c_name),
        "! </p>\n<p> Products:</p>\n<ul>\n",
    ])

    # for block
    for c_product in c_products:
        extend_result([
            "<li> ",
            to_str(c_lower(do_dots(c_product, "name"))),
            ": $",
            to_str(do_dots(c_product, "price")),
            "</li>\n"
        ])

    append_result("\n</ul>")
    return "".join(result)


products = {"Apple": 1.00,
            "Fig": 1.50, 
            "Pomegranate": 3.25}
print(render_function(
    {"name": "Hafs",
     "products": products,
     "lower": str.lower},
    lambda x,y: x if y == "name" else products[x]
    ))

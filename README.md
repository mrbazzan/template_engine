
# TEMPLATE ENGINE

Read **template_engine.txt**

## SUPPORTED SYNTAX

i)
Data is inserted using double dollar sign

    <p>Welcome, $$user$$</p>


ii)
The dot notation will be used to access object
attributes, dictionary values. If the resulting
value is callable, it will be automatically called.

    <p>The price is: $$product.price$$. </p>


iii)
Filters are also provided to modify values

    <p>$$ blog.title | lower | slugify $$</p>


iv)
Conditionals

    $! if product.price !$
        <p> Price is: $$ product.price $$</p>
    $! endif !$


v)
Loops
    $! for product in products !$
        <p> Price is: $$$ product.price $$</p>
    $! endfor !$

vi)
Comments

    $# This is a simple template engine #$


# TEMPLATE ENGINE

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


## EXAMPLE

```python3

from engine import Template

template = Template("""
<h1>Hello $$name|upper$$!</h1>
<h2>You have $\x01$$account$$ in your account</h2>
$# For loop #$
$! for topic in topics !$
    <p> Status: $$topic.status|upper|lower$$.</p>
    $! if topic.subject !$
        <p>You are interested in $$topic.subject$$.</p>
    $! endif !$
$! endfor !$
<h3>Thank you for your services</h3>
""", {'upper': str.upper,'lower': str.lower})

text = template.render({
    'name': "Ned",
    'account': 2.00,
    'topics': [{"subject":'', "status": lambda : repr(None)},
               {"subject":'Python', "status": "Enjoy"},
               {"subject":'Geometry', "status": "??"},
               {"subject":'Juggling', "status": "Hard"}]
})
print(text)
```

For more information, read **template_engine.txt**


Implementation gotten from [A Template Engine](https://aosabook.org/en/500L/a-template-engine.html)


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

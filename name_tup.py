from string import Template

message = Template('$imie jest na $miejsce miejscu!!')

info = [
    ('Michal', 5),
    ('Radek', 1),
    ('Agnieszka', 10),
    ('Ernest', 2)
]

for i, m in info:
    text = message.substitute(imie=i, miejsce = m)
    print(text)
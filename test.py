from worksheetgen import main

title = 'Worksheet test'
set = [
    ['This is the first problem', 'firstans'],
    ['This is the second problem', 'secondans'],
    ['This is a really really really really really really really really really really really really really really really really long problem', 'secondans'],
    ['This is a really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really long problem', 'secondans'],
]

main.write_pdf(title, set)

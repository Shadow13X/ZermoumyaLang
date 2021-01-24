('ASS', 
    ('a', 'var'), 
    ('NUMBER', 10)
)
('FOR', 
    ('ASS', ('i', 'var'), ('NUMBER', 0)), #ass
    ('<', ('VAR', ('i', None)), ('VAR', ('a', None))), #cond
    ('SUM', ('VAR', ('i', None)), ('NUMBER', 1)), #incre
    ('BLOC', 
        (
            ('COND', 
                (('IFCOND', ('==', ('VAR', ('i', None)), ('NUMBER', 5)), ('BLOC', ('BREAK',))),)
            ),
        )
    )
)
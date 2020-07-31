# Scheme is a famous functional programming language from the 1970s.
# It is a dialect of Lisp (which stands for LISt Processing).

# A symbol acts a lot like a Python name, but not exactly. Specifically, a symbol in Scheme is also a type of value.
# On the other hand, in Python, names only serve as expressions; a Python expression can never evaluate to a name.

# (if <predicate> <if-true> [if-false])
# Evaluate <predicate>.
# If <predicate> evaluates to a truth-y value, evaluate and return the value if the expression <if-true>.
# Otherwise, evaluate and return the value of [if-false] if it is provided.

# scm> (if (> 5 3)
#      1
#      2)

# (define <symbol> <expression>)

# scm> (define pi 3.14)
# pi
# scm> (* pi 2)
# 6.28

# (define (<symbol> <formal parameters>) <body>)

# scm> (define (abs x)
#      (if (< x 0)
#      (- x)
#      x))
# abs
# scm> (abs -3)
# 3

# scm> (define (average x y) (/ (+ x y) 2))
# average
# scm> (average 10 20)
# 15

# scm> (define (square x) (* x x))
# square
# scm> (square 3)
# 9

# multi-clause if/elif/else conditional expression in Python.
# cond takes in an arbitrary number of arguments known as clauses.
# A clause is written as a list containing two expressions: (<p> <e>).
# (cond
#     (<p1> <e1>)
#     (<p2> <e2>)
#     ...
#     (<pn> <en>)
#     [(else <else-expression>)])
# The first expression in each clause is a predicate.
# The second expression in the clause is the return expression corresponding to its predicate.
# The optional else clause has no predicate.

# scm> (cond
#      ((> 0 0) 'positive)
#      ((< 0 0) 'negative)
#      (else 'zero))

# The rules of evaluation are as follows:
# Evaluate the predicates <p1>, <p2>, ..., <pn> in order until you reach one that evaluates to a truth-y value.
# If you reach a predicate that evaluates to a truth-y value, evaluate and return the corresponding expression in the clause.
# If none of the predicates are truth-y and there is an else clause, evaluate and return <else-expression>.

#(lambda (<formal-parameter>) <body>)

# scm> (define (plus4 x) (+ x 4))
# plus4
# scm> (plus4 4)
# 8

# scm> (define plus4 (lambda (x) (+ x 4)))
# plus4
# scm> (plus4 4)
# 8
# scm> plus4
# (lambda (x) (+ x 4))
# scm>

# lambda can be directly called
# scm> ((lambda (x y z) (+ x y z)) 1 2 3)
# 6

# list
# cons: Two-argument procedure that creates a linked list
# Cons. The primitive procedure cons means "construct."

# car:  return the first element of a list
# refers to the "Contents of Address part of Register"

# cdr:  return the rest of a list
# cdr refers to the phrase "Contents of Decrement part of Register."

# cadr = second item
# cadr:  "contents of address part of contents of decrement part of register".

# nil:  the empty list
# scm> (list 1 2 3 4)
# (1 2 3 4)

# scm> (define b 2)
# b
# scm> '(a b c)
# (a b c)
# scm> '(a ,b c)
# (a (unquote b) c)
# scm> `(a b c)
# (a b c)
# scm> `(a ,b c)
# (a 2 c)
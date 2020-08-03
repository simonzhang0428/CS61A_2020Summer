# (define (reverse lst)
# 	(define (reverse-sofar lst lst-sofar)
# 		(if (null? lst)
# 			lst-sofar
# 			(reverse-sofar (cdr lst) (cons (car lst) lst-sofar))))
# 	(reverse-sofar lst nil))
#
#
# (define (insert n lst)
# 	(define (insert-helper n lst seen)
# 		(cond ((null? lst) (append seen (list n)))
# 			((< n (car lst)) (append seen (list n) lst))
# 			(else (insert-helper n (cdr lst)
# 				(append seen (list (car lst)))))))
# 	(insert-helper n lst nil))

def list_5(expr):
	return eval("[" + expr + " for i in range(5)]")

lst = list_5("print(10)")
print(lst)

def make_lambda(params, body):
	return eval(f"lambda {params}: {body}")
	# return eval("lambda " + params + " : " + body)

f = make_lambda('x, y', 'x + y')
print(f(1, 2))
g = make_lambda("a, b, c", "c if a > b else -c")
print(g(1, 2, 3))

# define-macro allows us to define what’s known as a macro,
# which is simply a way for us to combine unevaluated input expressions together into another expression.

# We evaluated lambda procedures in the following way:
# 1. Evaluate operator
# 2. Evaluate operands
# 3. Apply operator to operands, evaluating the body of the procedure

# However, the rules for evaluating calls to macro procedures are:
# 1. Evaluate operator
# 2. Apply operator to unevaluated operands
# 3. Evaluate the expression returned by the macro in the frame it was called in.
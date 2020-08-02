(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (sign num)
  (cond 
    ((> num 0) 1)
    ((= num 0) 0)
    ((< num 0) -1)
  )
)

(define (square x) (* x x))

(define (pow x y) 
    (cond ((= y 0) 1)
        ((even? y) (square (pow x (/ y 2))))
        ((odd? y) (* x (pow x (- y 1)))))
)

(define (unique s) 
    (if (null? s) nil
      (cons (car s)
            (unique (filter (lambda (x) (not (eq? (car s) x))) (cdr s)))))
)

(define (replicate x n) 'YOUR-CODE-HERE)

(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
)

(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
)

(define-macro
 (list-of map-expr for var in lst if filter-expr)
 'YOUR-CODE-HERE
)

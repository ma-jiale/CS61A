(define (factorial x)
    (if (= x 1) 
        1
        (* x (factorial (- x 1)))
    )
)

(define (fib n)
    (if (or (= n 1) (= n 2))
        1
        (+ (fib (- n 1)) (fib (- n 2)))
    )
)

(define (my-append a b)
    (define (helper a)
        (if (equal? a nil)
            b
            (cons (car a) (helper (cdr a)))
        )
    )
    (helper a)
)

(define (duplicate lst)
    (if (equal? lst nil)
        nil
        (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
    )
)

(define (insert element lst index)
    (if (equal? (cdr lst) nil)
        (cond
            ((= index 0) (list element (car lst)))
            ((= index 1) (list (car lst) element))
        )
        (if (= index 0)
            (cons element (cons (car lst) (cdr lst)))
            (cons (car lst) (insert element (cdr lst) (- index 1)))
        )
    )
)
    
    
        
        
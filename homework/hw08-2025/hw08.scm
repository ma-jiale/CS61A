(define (ascending? s) 
    (if (null? (cdr s))
        #t
        (and (<= (car s) (car (cdr s))) (ascending? (cdr s)))
    )
)

(define (my-filter pred s)
    (if (null? s)
        nil
        (if (pred (car s))
            (cons (car s) (my-filter pred (cdr s)))
            (my-filter pred (cdr s))
            )
    )
)

(define (interleave lst1 lst2)
    (cond
        ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2)))))
    )
)

(define (no-repeats s)
    (define (not-in a s)
        (if (null? s)
            #t
            (if (not (= a (car s)))
                (not-in a (cdr s))
                #f
            )
        )
    )
    (define (hepler s s-before)
        (if (null? s)
            nil
            (if (not-in (car s) s-before)
                (cons (car s) (hepler (cdr s) (cons (car s) s-before)))
                (hepler (cdr s) s-before)
                )
            )

    )
    (hepler s nil)
)

(no-repeats (list 5 4 5 4 2 2))



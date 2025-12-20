(define (split-at lst n)
   (define (helper lst cur)
   (if (null? lst)
      (list nil)
      (if (> cur n)
      (cons nil lst)
      (begin 
        (define new (helper (cdr lst) (+ cur 1)))
        (cons (cons (car lst) (car new)) (cdr new))
      )
      )
   )
   )
   (helper lst 1)
)

(define (compose-all funcs)
  (define (func x)
    (if (null? funcs)
    x
    ((compose-all (cdr funcs)) ((car funcs) x))
    )
  )
  func
)

; scm> (split-at (list 1 2 3 4) 2)
; ((1 2) 3 4)
; scm> (define (plus_one x) (+ x 1))
; plus_one
; scm> (define (sub_two x) (- x 2))
; scm> ((compose-all (list plus_one plus_one sub_two)) 1)
; 1
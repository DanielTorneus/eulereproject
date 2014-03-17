(ns project-euler)

; Authors: Crobol
; Complexity: ?
; Output: 104761

(def n 10001)

(defn prime? [x]
  (.isProbablePrime (BigInteger/valueOf x) 10))

(println
  (nth
    (filter
      prime?
      (iterate inc 1))
    (dec n)))

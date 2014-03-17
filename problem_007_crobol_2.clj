(ns project-euler)

; Authors: Crobol
; Complexity: ?
; Output: 104761

(def n 10001)

(defn prime? [x primes]
  (every? #(not= (mod x %) 0) primes))

(defn nth-prime [n]
  (loop [primes [2] x 3]
    (if 
      (== (count primes) n)
        (last primes)
        (recur (if (prime? x primes) (conj primes x) primes) (inc x)))))

(println (nth-prime n))

(defquery get_book_by_age_group
  (declare (variables ?age_group))
  ?book_fact <- (books (score ?score) (age_group ?age_group))
)
(defquery get_book_by_pacing
  (declare (variables ?pacing))
  ?book_fact <- (books (score ?score) (pacing ?pacing))
)
(defquery get_book_by_genre
  (declare (variables ?genre))
  ?book_fact <- (books (score ?score) (genre $? ?genre $?))
)
(defquery get_book_by_language
  (declare (variables ?language))
  ?book_fact <- (books (score ?score) (language ?language))
)
(defquery get_book_by_style
  (declare (variables ?style))
  ?book_fact <- (books (score ?score) (style ?style))
)

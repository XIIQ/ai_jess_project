(deffunction register_user (?username ?genre ?author ?language ?age_group ?pacing ?style)
  (assert
    (users
      (username ?username)
      (genre ?genre)
      (author ?author)
      (language ?language)
      (age_group ?age_group)
      (pacing ?pacing)
      (style ?style)
    )
  )
  (increment_score ?age_group ?pacing ?genre ?language ?style)
)

(deffunction read_user_details ()
  (bind ?username (read_username))
  (bind ?genres (read_genres))
  (bind ?author (read_author))
  (bind ?age_group (read_age_group))
  (bind ?language (read_language))
  (bind ?style (read_style))
  (bind ?pacing (read_pacing))
  (register_user ?username ?genres ?author ?language ?age_group ?pacing ?style)
)

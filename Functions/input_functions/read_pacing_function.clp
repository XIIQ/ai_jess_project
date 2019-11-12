(deffunction read_pacing ()
  (printout t "Please enter your pacing!!" crlf)
  (bind ?result (run-query* get_all_pacings))
  (bind ?counter 1)
  (while (?result next)
    (printout t ?counter ". " (?result getString type) crlf)
    (++ ?counter)
  )
  (bind ?pacing (read))
  (return ?pacing)
)

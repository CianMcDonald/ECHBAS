def calculate_triage(entered):
      """
      Function thats gets data from form and calculates the patients triage score
      """
      # get triage from db
      triage_score = entered
      # if the triage is a number
      if str(triage_score).isdigit():
          if int(triage_score) <= 5 and int(triage_score) >= 1:
         # add triage to entry box
            return True
      else:
         # triage is not a number so display error
         return False
   
from docx import Document
from docx.shared import Pt
doc = Document()

while True:
  Execercise = input("What is the exercise: ")
    
  if Execercise.lower() == "end":
    break
  Weight = input("how much weight do you want to change (defaults to 5): ")
  if Weight == "":
    Weight = int(5)
  paragraph = doc.add_paragraph(style='Normal')
  run21 = paragraph.add_run(Execercise)
  run21.font.name = 'Courier New'
  run21.font.size = Pt(15)
  paragraph.alignment = 1
  Bench_Press_lbs = list(
      map(float,
          input("Enter lbs for each set separated by space: ").split()))
  how_many_reps = list(
      map(int,
          input("Enter reps for each set separated by space: ").split()))
    
    # Check if the lengths of both lists match
  if len(Bench_Press_lbs) != len(how_many_reps):
      print("Error: The number of pound inputs and rep inputs must be the same.")
  else:
      # Process each set
    spam = 0 
    repsamount = 11
    for lbs, reps in zip(Bench_Press_lbs, how_many_reps, strict=True):
      if reps >= 12 - spam:
        increase_lbs = lbs + float(Weight)
        paragraph1 = doc.add_paragraph(style='Normal')
        run1 = paragraph1.add_run(f"{increase_lbs} lbs x {repsamount} reps")
        run1.font.name = 'Courier New'
        run1.font.size = Pt(15)
        paragraph1.alignment = 1
      elif 7 - spam <= reps <= 12 - spam:
        keep_lbs = lbs
        paragraph2 = doc.add_paragraph(style='Normal')
        run2 = paragraph2.add_run(f"{keep_lbs} lbs x {repsamount} reps")
        run2.font.name = 'Courier New'
        run2.font.size = Pt(15)
        paragraph2.alignment = 1
      elif 6 - spam >= reps >= 0:
        lower_lbs = lbs - float(Weight)
        paragraph3 = doc.add_paragraph(style='Normal')
        run3.font.name = 'Courier New'
        run3 = paragraph3.add_run(f"{lower_lbs} lbs x {repsamount} reps")
        run3.font.size = Pt(15)
        paragraph3.alignment = 1
      spam += 2
      repsamount -= 2
doc.save('workout_results.docx')

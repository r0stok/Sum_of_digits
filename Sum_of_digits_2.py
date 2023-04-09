class Student:
    def __init__(self, student_id, first_name, last_name):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.exam_scores = []

    def add_score(self, score):
        if score >= 0 and score <= 100:
            self.exam_scores.append(score)
        else:
            print("Invalid score. Score must be in the range [0, 100].")

    def show_scores(self):
        print("Student scores:", end=' ')
        for score in self.exam_scores:
            print(score, end=' ')
        print()

    def score_average(self):
        if len(self.exam_scores) == 0:
            print("The student hasn't passed any exam yet.")
        else:
            average_score = sum(self.exam_scores) / len(self.exam_scores)
            return average_score

    def course_passed(self):
        passed_scores = [score for score in self.exam_scores if score > 60]
        if len(passed_scores) >= 3:
            return True
        else:
            return False

# Create instances of the Student class
john = Student(1, 'John', 'Doe')
linda = Student(2, 'Linda', 'Jones')
jason = Student(3, 'Jason', 'Kirk')
jane = Student(4, 'Jane', 'Doe')

# Add scores for the students
john.add_score(100)
john.add_score(95)
linda.add_score(25)
linda.add_score(65)
linda.add_score(80)
linda.add_score(75)
jason.add_score(50)
jason.add_score(60)
jason.add_score(55)
jane.add_score(95)
jane.add_score(80)
jane.add_score(100)

# Show scores for each student
john.show_scores()
linda.show_scores()
jason.show_scores()
jane.show_scores()

# Compute and show average score for each student
print("John's average score:", john.score_average())
print("Linda's average score:", linda.score_average())
print("Jason's average score:", jason.score_average())
print("Jane's average score:", jane.score_average())

# Check if each student passed the course
print("Did John pass the course?", john.course_passed())
print("Did Linda pass the course?", linda.course_passed())
print("Did Jason pass the course?", jason.course_passed())
print("Did Jane pass the course?", jane.course_passed())

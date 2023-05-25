class Student:
    def __init__(self, student_id: int, first_name: str, last_name: str):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.exam_scores = []

    def add_score(self, score: int):
        if 0 <= score <= 100:
            self.exam_scores.append(score)

    def show_scores(self):
        print("Exam Scores:", end=" ")
        for score in self.exam_scores:
            print(score, end=" ")
        print()

    def score_average(self):
        if len(self.exam_scores) == 0:
            print("This student hasn't taken any exams yet.")
        else:
            average = sum(self.exam_scores) / len(self.exam_scores)
            return average

    def course_passed(self):
        passed_scores = [score for score in self.exam_scores if score > 60]
        return len(passed_scores) >= 3
# Create the Student objects
student1 = Student(1, "John", "Doe")
student1.add_score(100)
student1.add_score(95)

student2 = Student(2, "Linda", "Jones")
student2.add_score(25)
student2.add_score(65)
student2.add_score(80)
student2.add_score(75)

student3 = Student(3, "Jason", "Kirk")
student3.add_score(50)
student3.add_score(60)
student3.add_score(55)

student4 = Student(4, "Jane", "Doe")
student4.add_score(95)
student4.add_score(80)
student4.add_score(100)

# Test the methods for each student
print("Student 1:")
student1.show_scores()
print("Average score:", student1.score_average())
print("Course passed?", student1.course_passed())

print("Student 2:")
student2.show_scores()
print("Average score:", student2.score_average())
print("Course passed?", student2.course_passed())

print("Student 3:")
student3.show_scores()
print("Average score:", student3.score_average())
print("Course passed?", student3.course_passed())

print("Student 4:")
student4.show_scores()
print("Average score:", student4.score_average())
print("Course passed?", student4.course_passed())
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
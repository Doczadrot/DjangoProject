from .models import Student, Grade

class StudentService:

    @staticmethod
    # метод для получения полного имени студента
    def get_full_name(student_id):
        student = Student.objects.get(id=student_id) #через гет по id  мы получаем значения студента
        return f'{student.first_name} {student.last_name}'



    @staticmethod #Метод для расчетного среднего балла

    def calculate_average(student_id):  #по id мы можем найти все оценки студента

        #grades во  множественном числе потому возвращаем все оценки
        grades = Grade.objects.filter(student_id=student_id)

        if not grades.exists(): #если оценок нет получаем нон - 0
            return None
        #если оценки есть мы можем посчитать итогову сумму
        total_score = sum(grade.score for grade in grades)
        average_score = total_score / grades.count() #среднеее значение

        return average_score

    @staticmethod
#метод лоя проверки сдал студент на основе среднего балла
    def has_passed(student_id, passing_score=60):
        average_score = StudentService.calculate_average(student_id)

        if average_score in None:
            return None

        return average_score >= passing_score


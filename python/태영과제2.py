def display_menu() :
    print("1. 추가")
    print("2. 평균계산")
    print("3. 등수에 따른 검색")
    print("4. 삭제")
    print("5. 등수별 출력")
    print("6. 종료")
    user = int(input("메뉴 항목을 선택하시오: "))
    return user


def rank_students(students):
    students.sort(key=lambda x: x['average'], reverse=True)
    rank = 1
    for student in students:
        student['rank'] = rank
        rank += 1
    return students
        

def main():
    students = []
    while True:
        user = display_menu()
        if user == 1:
            name = input("이름을 입력하세요: ")
            student_id = input("학번을 입력하세요: ")
            eng = []
            math = []
            kor = []

            for i in range(3):
                temp_eng = int(input("영어 점수를 입력하세요: "))
                eng.append(temp_eng)
            for i in range(3):
                temp_math = int(input("수학 점수를 입력하세요: "))
                math.append(temp_math)
            for i in range(3):
                temp_kor = int(input("국어 점수를 입력하세요: "))
                kor.append(temp_kor)

            total_avg_list=eng+math+kor
            total_avg=sum(total_avg_list)/len(total_avg_list)

            student = {
                "name": name,
                "student_id": student_id,
                "eng": eng,
                "math": math,
                "kor": kor,
                "average":total_avg,
                "rank":-1
            }

            students.append(student)
            print("성적이 추가되었습니다.")

        elif user == 2:
            
            total_avg = []
            student_id = input("평균을 계산할 학생의 학번을 입력하세요: ")
            
            for student in students:
                if student["student_id"] == student_id:
                    print(f"{student['name']} 학생의 성적 평균: {student['average']:}")
                    break

        elif user == 3:
            rank = int(input("검색할 등수를 입력하세요: "))
            students=rank_students(students)
            print(students[rank-1]["name"], students[rank-1]["average"])
            
        elif user == 4:
            student_id = input("삭제할 학생의 학번을 입력하세요: ")
            found = False

            for i, student in range(students):
                if student["student_id"] == student_id:
                    del students[i]
                    found = True
                    print("삭제되었습니다.")
                    break

        elif user == 5:
            students=rank_students(students)
            print(students)

        elif user == 6:
            break
    

main()
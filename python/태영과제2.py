def display_menu() :
    print("1. 추가")
    print("2. 평균계산")
    print("3. 등수에 따른 검색")
    print("4. 삭제")
    print("5. 등수별 출력")
    print("6. 종료")
    user = int(input("메뉴 항목을 선택하시오: "))
    return user


def search_rank(student_list):
    rank = int(input("검색할 등수를 입력하세요: "))
    rank_list = []
    for student in student_list:
        total_score = sum(student.scores)
        count = 0
        for other_student in student_list:
            if sum(other_student.scores) > total_score:
                count += 1
        if count+1 == rank:
            rank_list.append(student)
    if rank_list:
        print("등수가 {}등인 학생 목록:".format(rank))
        for student in rank_list:
            print("이름: {}, 학번: {}".format(student.name, student.number))
    else:
        print("해당 등수의 학생이 없습니다.")
        

def main():
    user = display_menu()
    students = []
    if user == 1:
        name = input("이름을 입력하세요: ")
        student_id = input("학번을 입력하세요: ")
        eng = []
        math = []
        kor = []

        for i in range(3):
            eng = int(input("영어 점수를 입력하세요: "))
            eng.append(eng)
        for i in range(3):
            math = int(input("수학 점수를 입력하세요: "))
            math.append(math)
        for i in range(3):
            kor = int(input("국어 점수를 입력하세요: "))
            kor.append(kor)

        total_avg_list=eng+math+kor
        total_avg=sum(total_avg_list)/len(total_avg_list)

        student = {
            "name": name,
            "student_id": student_id,
            "eng": eng,
            "math": math,
            "kor": kor,
            "average":total_avg
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

        n = len(students)
        rank = [1] * n

        for i in range(n):
            for j in range(n):
                if students[i]["average"] < students[j]["average"]:
                    rank[i] += 1

        for i in range(n):
            print(f"{rank[i]}등 - 이름: {students[i]['name']}, 학번: {students[i]['student_id']}, 평균점수: {students[i]['average']:.1f}")

    elif user == 6:
        break
    
    
    
main()
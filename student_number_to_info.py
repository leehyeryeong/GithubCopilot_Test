#학번을 입력 받아 첫번째는 학년, 두번째는 반, 세번째는 번호를 출력하는 프로그램을 작성하시오.
def student_number_to_info(student_number):
    year = student_number[0]
    class_number = student_number[1]
    #반이 1, 2이면 뉴미디어소프트웨어과, 3, 4이면 뉴미디어웹솔루션과, 5, 6이면 뉴미디어디자인과 출력하기
    if class_number == '1' or class_number == '2':
        major = '뉴미디어소프트웨어과'
    elif class_number == '3' or class_number == '4':
        major = '뉴미디어웹솔루션과'
    elif class_number == '5' or class_number == '6':
        major = '뉴미디어디자인과'
    else:
        major = '없음'
    number = student_number[2]
    return year, class_number, number, major

    student_number = student_number[2]
    return year, class_number, student_number

print(student_number_to_info("2311"))
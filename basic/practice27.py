for week in range(1,4):
    with open(str(week) + "주차.txt", "w", encoding="utf8") as week_file:
        week_file.write("- {0} 주차 주간보고 -\n부서 :\n이름 :\n업무요약 :".format(week))

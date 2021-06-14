def get_age(year):
    age = 2017 - year + 1
    if 20 <= age <= 26:
        return "대학생"
    elif 17 <= age < 20:
        return "고등학생"
    elif 14 <= age < 17:
        return "중학생"
    elif 8 <= age < 14:
        return "초등학생"
    else:
        return "학생이 아닙니다."


if __name__ == "__main__":
    y = int(input("enter your birth year:"))
    print(get_age(y))

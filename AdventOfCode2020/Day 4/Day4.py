def CheckValid(Person):
    if len(Person) == 8:
        return True
    elif len(Person) == 7:
        CheckingValid = True
        for field in Person:
            if field[0] == "c":
                CheckingValid = False
                break
        if CheckingValid:
            return True
    return False


def Part1():
    File = open("Input.txt").read().split("\n\n")
    File = [x.replace("\n", " ").split(" ") for x in File]

    Valid = 0

    for Person in File:
        if CheckValid(Person):
            Valid += 1
    return Valid


def Part2():
    File = open("Input.txt").read().split("\n\n")
    File = [x.replace("\n", " ").split(" ") for x in File]

    NoOfValid = 0

    for Person in File:
        if CheckValid(Person):
            # 2 e's, 2 h's
            Valid = True

            for Field in Person:
                Code = Field.split(":")[0]
                Answer = Field.split(":")[1]
                if Code[0] == "b":
                    if int(Answer) < 1920 or int(Answer) > 2002:
                        Valid = False
                        break
                elif Code[0] == "i":
                    if int(Answer) < 2010 or int(Answer) > 2020:
                        Valid = False
                        break
                elif Code[0] == "e" and Code[1] == "y":
                    if int(Answer) < 2020 or int(Answer) > 2030:
                        Valid = False
                        break
                elif Code[0] == "h" and Code[1] == "g":
                    if Answer[-1] == "m":
                        if int(Answer[:-2]) < 150 or int(Answer[:-2]) > 193:
                            Valid = False
                            break
                    elif Answer[-1] == "n":
                        if int(Answer[:-2]) < 59 or int(Answer[:-2]) > 76:
                            Valid = False
                            break
                    else:
                        break
                elif Code[0] == "h" and Code[1] == "c":
                    if Answer[0] != "#":
                        Valid = False
                        break
                    if len(Answer) != 7:
                        Valid = False
                        break
                    if Answer.lower() != Answer.upper() or not (Answer[1:].isalnum()):
                        Valid = False
                        break
                elif Code[0] == "e" and Code[1] == "c":
                    if (
                        Answer != "amb"
                        and Answer != "blu"
                        and Answer != "Answer"
                        and Code != "Answer"
                        and Answer != "grn"
                        and Answer != "hzl"
                        and Answer != "oth"
                    ):
                        Valid = False
                        break
                elif Code[0] == "p":
                    if not (len(Answer) == 9 and Answer.isnumeric()):
                        Valid = False
                        break
            if Valid:
                NoOfValid += 1
    return NoOfValid


print(Part1())
print(Part2())

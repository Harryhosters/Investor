# A PROGRAM TO CALCULATE AND FILL OUT THE GPA FOR P.E CLASSESS



print("please enter your name below ")
your_name = input("What\'s your name? ").upper()

print("please enter the grade here for your subjects, please make sure that grades are valid, Example A ,B ,C ,D or F")

mapping = {
    "A":5,
    "B":4,
    "C":3,
    "D":2,
    "F":1,
    }

hisabati = input("hesabu ").upper()
uraia = input("uraia ").upper()
english = input("english ").upper()
sayansi = input("sayansi ").upper()
tehama = input("tehema ").upper()
elimu_kwa_michezo = input("elimu kwa michezo ").upper()
ualimu_kwa_michezo = input("ualimu kwa michezo ").upper()
ICT = input("ICT ").upper()
vielelezo = input("vielelezo na teknolojia ").upper()
communication_skills = input("communication skills ").upper()
kiswahili = input("kiswahili ").upper()

grade_count = (hisabati + uraia + english + sayansi + tehama + elimu_kwa_michezo + ualimu_kwa_michezo + ICT + vielelezo + communication_skills + kiswahili) 

TS = 11
his = mapping.get(hisabati, 0)
ura = mapping.get(uraia, 0)
eng = mapping.get(english, 0)
ualimu_mich = mapping.get(ualimu_kwa_michezo, 0)
elimu_mich = mapping.get(elimu_kwa_michezo, 0)
teh = mapping.get(tehama, 0)
say = mapping.get(sayansi, 0)
kisw = mapping.get(kiswahili, 0)
comm = mapping.get(communication_skills, 0)
ICT_mapped = mapping.get(ICT, 0)
vel = mapping.get(vielelezo, 0)


gpa = (his + ura + eng + ualimu_mich + elimu_mich + say + kisw + comm + ICT_mapped + vel + teh) / TS
gpa_rounded = round(gpa, 1)
print("Total subjects is 11. data has been submitted successful as shown below")

print(f"hisabati: {hisabati}")
print(f"uraia: {uraia}")
print(f"english: {english}")
print(f"ualimu kwa michezo : {ualimu_kwa_michezo}")
print(f"elimu kwa michezo: {elimu_kwa_michezo}")
print(f"tehama: {tehama}")
print(f"ICT: {ICT}")
print(f"vielelezo na teknolojia: {vielelezo}")
print(f"sayansi: {sayansi}")
print(f"communication skills: {communication_skills}")
print(f"kiswahili : {kiswahili}")


print(f"HELLO {your_name}, the GPA you have is: {gpa_rounded}")


if 4.5 <= gpa_rounded <= 5.0:
    print("Excellent ,You have distinction")

if 3.5 <= gpa_rounded <=  4.4:
    print("very good, You have credit")

if 2.0 <= gpa_rounded <= 3.4:
    print("Good, you have a pass")

if 1.0 <= gpa_rounded <= 1.9:
    print("Very bad, you have a fail")

print("This is the summary for your grades")
print("You have 'A' ", grade_count.count("A"))
print("You have 'B' ", grade_count.count("B"))
print("You have 'C' ", grade_count.count("C"))
print("You have 'D' ", grade_count.count("D"))
print("You have 'F' ", grade_count.count("F"))

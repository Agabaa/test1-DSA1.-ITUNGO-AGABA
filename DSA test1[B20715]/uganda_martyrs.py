#number 1
# List of Catholic Martyrs
catholic_martyrs = [
    "Achileo Kiwanuka",
    "Adolphus Ludigo-Mukasa",
    "Ambrosius Kibuuka",
    "Anatoli Kiriggwajjo",
    "Andrew Kaggwa",
    "Antanansio Bazzekuketta",
    "Bruno Sserunkuuma",
    "Charles Lwanga",
    "Denis Ssebuggwawo Wasswa",
    "Gonzaga Gonza",
    "Gyavira Musoke",
    "James Buuzaabalyaawo",
    "John Maria Muzeeyi",
    "Joseph Mukasa Kizito",
    "Lukka Baanabakintu",
    "Matiya Mulumba",
    "Mbaga Tuzinde",
    "Mugagga Lubowa",
    "Mukasa Kiriwawanvu",
    "Nowa Mawaggali",
    "Ponsiano Ngondwe"
]

# List of Anglican Martyrs
anglican_martyrs = [
    "Aaron Lubega",
    "Apollo Kivebulaya",
    "Eria Sebukyala",
    "Fredrick Kizza",
    "George Kizza",
    "James Hannington",
    "Janani Luwum",
    "Joseph Balikuddembe Kizito",
    "Mark Kakumba",
    "Matia Mulumba",
    "Nuhu Mbegu",
    "Robert Munyagayirwa",
    "Samwiri Mukasa",
    "Yefusa Namayanja",
    "Yohana Mukasa",
    "Yosefu Lugalama",
    "Yowana Kitaka",
    "Yowana Maria Mukasa",
    "Yowana Mukiibi",
    "Yusufu Lugalama",
    "Zakayo Lubega"
]
#number 2
catholic_martyrs = [
    "Achileo Kiwanuka",
    "Adolphus Ludigo-Mukasa",
    "Ambrosius Kibuuka",
    "Anatoli Kiriggwajjo",
    "Andrew Kaggwa",
    "Antanansio Bazzekuketta",
    "Bruno Sserunkuuma",
    "Charles Lwanga",
    "Denis Ssebuggwawo Wasswa",
    "Gonzaga Gonza",
    "Gyavira Musoke",
    "James Buuzaabalyaawo",
    "John Maria Muzeeyi",
    "Joseph Mukasa Kizito",
    "Lukka Baanabakintu",
    "Matiya Mulumba",
    "Mbaga Tuzinde",
    "Mugagga Lubowa",
    "Mukasa Kiriwawanvu",
    "Nowa Mawaggali",
    "Ponsiano Ngondwe"
]

anglican_martyrs = [
    "Aaron Lubega",
    "Apollo Kivebulaya",
    "Eria Sebukyala",
    "Fredrick Kizza",
    "George Kizza",
    "James Hannington",
    "Janani Luwum",
    "Joseph Balikuddembe",
    "Kizito Mark Kakumba",
    "Matia Mulumba",
    "Nuhu Mbegu",
    "Robert Munyagayirwa",
    "Samwiri Mukasa",
    "Yefusa Namayanja",
    "Yohana Mukasa",
    "Yosefu Lugalama",
    "Yowana Kitaka",
    "Yowana Maria Mukasa",
    "Yowana Mukiibi",
    "Yusufu Lugalama",
    "Zakayo Lubega"
]
catholic_set = set(catholic_martyrs)
anglican_set = set(anglican_martyrs)

duplicates = catholic_set.intersection(anglican_set)


catholic_set -= duplicates
anglican_set -= duplicates

catholic_martyrs = list(catholic_set)
anglican_martyrs = list(anglican_set)

#number 3

def martyr_count(name):
    if name in catholic_martyrs:
        return "Catholic"
    elif name in anglican_martyrs:
        return "Anglican"
    else:
        return "non of the lists"

martyr_name = "Charles Lwanga"
group = martyr_count(martyr_name)
print(f"{martyr_name} belongs to the {group} group.")
#number 4
martyr_name = "Kizito"
group = martyr_count(martyr_name)
print(f"{martyr_name} belongs to the {group} group.")
#number 5
def is_uganda_martyr(name):
    catholic_martyrs = [
        "Achileo Kiwanuka", "Adolphus Ludigo-Mukasa", "Ambrosius Kibuuka",
        "Anatoli Kiriggwajjo", "Andrew Kaggwa", "Antanansio Bazzekuketta",
        "Bruno Sserunkuuma", "Charles Lwanga", "Denis Ssebuggwawo Wasswa",
        "Gonzaga Gonza", "Gyavira Musoke", "James Buuzaabalyaawo",
        "John Maria Muzeeyi", "Joseph Mukasa Kizito", "Lukka Baanabakintu",
        "Matiya Mulumba", "Mbaga Tuzinde", "Mugagga Lubowa", "Mukasa Kiriwawanvu",
        "Nowa Mawaggali", "Ponsiano Ngondwe"
    ]

    anglican_martyrs = [
        "Aaron Lubega", "Apollo Kivebulaya", "Eria Sebukyala", "Fredrick Kizza",
        "George Kizza", "James Hannington", "Janani Luwum", "Joseph Balikuddembe",
        "Mark Kakumba", "Matia Mulumba", "Nuhu Mbegu", "Robert Munyagayirwa",
        "Samwiri Mukasa", "Yefusa Namayanja", "Yohana Mukasa", "Yosefu Lugalama",
        "Yowana Kitaka", "Yowana Maria Mukasa", "Yowana Mukiibi", "Zakayo Lubega"
    ]

    return name in catholic_martyrs and name in anglican_martyrs

input_name = "Charles Lwanga"
martyr_name = input("Please enter a martyr's name: ")
print(f"You entered the name: {martyr_name}")
result = is_uganda_martyr(input_name)
print(result) 




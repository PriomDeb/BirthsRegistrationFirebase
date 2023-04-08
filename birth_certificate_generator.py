import cv2

def generate_birth_certificate(name, father_name, mother_name, date_of_birth, birth_location, key):
    list_names = [name, father_name, mother_name, date_of_birth, birth_location]

    # for index, name in enumerate(list_names):
    template = cv2.imread("Template.jpg")
    cv2.putText(template, list_names[0], (650, 788), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(template, list_names[1], (250, 1100), cv2.FONT_HERSHEY_COMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(template, list_names[2], (1000, 1100), cv2.FONT_HERSHEY_COMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(template, list_names[3], (500, 1350), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(template, list_names[4], (450, 1650), cv2.FONT_HERSHEY_COMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.imwrite(f"Birth_Certificates/{list_names[0]}_Child_ID_{key}.jpg", template)
    return True


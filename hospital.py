def extract_info(hospital_list):
    result = []
    for hospital in hospital_list:
        city = hospital.contents[1].string
        district = hospital.contents[2].string
        hospi = hospital.contents[3].text.split()[0]
        number = hospital.contents[4].string

        hospital_info = {
            "시도" : city,
            "시군구" : district,
            "선별진료소(이름)" : hospi,
            "전화번호" : number
        }
        result.append(hospital_info)
    
    return result
    print(result)

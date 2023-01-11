from pydantic import ValidationError
from input_data import raw_info
from models import CandidateInfo, ResultInfo
import json


def change_structure(data):
    coordinates = {
        "latitude": data.address.lat,
        "longitude": data.address.lng
    }

    phone = {
        "city": str(data.contacts.phone[1:4]),
        "country": str(data.contacts.phone[:1]),
        "number": f'{data.contacts.phone[4:7]}-{data.contacts.phone[7:9]}-{data.contacts.phone[9:]}'
    }

    contacts = {
        "email": data.contacts.email,
        "name": data.contacts.fullName,
        "phone": phone
    }

    salary = {
        "from": data.salary.from_,
        "to": data.salary.to
    }

    schedule = {
        "id": data.employment
    }

    result = {
        "address": data.address.value,
        "contacts": contacts,
        "coordinates": coordinates,
        "description": data.description,
        "experience": '',
        "name": data.name,
        "salary": data.salary.to,
        "salary_range": salary,
        "schedule": schedule
    }
    outcome = ResultInfo.parse_obj(result)
    return outcome.json(ensure_ascii=False, sort_keys=True, by_alias=True)


if __name__ == '__main__':
    try:
        data = CandidateInfo.parse_raw(raw_info)
    except ValidationError as er:
        print('#####Error#####')
        print(er.json())
    else:
        print('Success!')
        res = change_structure(data)
        with open('result.json', 'w', encoding='UTF-8') as file:
            json.dump(res, file, ensure_ascii=False, indent=4, separators=(',', ': '))

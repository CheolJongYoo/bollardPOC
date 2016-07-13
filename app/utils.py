from flask_sqlalchemy import Pagination
import json

#결과코드 등의 enumeration을 위한 함수
#적용은 나중에..

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)

class PagingMap():
    totalCount = 0
    totalPage = 0
    curPage = 0
    countPerPage = 0
    data = None

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

class ResultMap():
    result = False
    code = 0
    message = ''
    data = None

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

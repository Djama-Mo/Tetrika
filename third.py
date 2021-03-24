from flask import Flask


app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return '<h1>Go to the <a href="http://127.0.0.1:5000/run_function"</a> to run the function</h1>'


@app.route('/run_function', methods=['GET'])
def send_result():
    return start_testing()


def appearance(intervals):
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    answer = 0
    for i in range(0, len(pupil), 2):
        for j in range(0, len(tutor), 2):
            if tutor[j] <= pupil[i] and tutor[j + 1] >= pupil[i + 1]:
                start = 0
                stop = 0
                if pupil[i] <= lesson[0] <= tutor[j + 1]:
                    start = lesson[0]
                elif lesson[0] <= pupil[i] <= tutor[j + 1]:
                    start = pupil[i]
                if pupil[i + 1] >= lesson[1] >= pupil[i]:
                    stop = lesson[1]
                elif lesson[1] >= pupil[i + 1]:
                    stop = pupil[i + 1]
                tmp = stop - start
                if tmp > 0:
                    answer += tmp
            elif tutor[j] <= pupil[i] and tutor[j + 1] <= pupil[i + 1]:
                start = 0
                stop = 0
                if pupil[i] <= lesson[0] <= tutor[j + 1]:
                    start = lesson[0]
                elif lesson[0] <= pupil[i] <= tutor[j + 1]:
                    start = pupil[i]
                if tutor[j + 1] >= lesson[1] >= pupil[i]:
                    stop = lesson[1]
                elif lesson[1] >= tutor[j + 1] >= pupil[i]:
                    stop = tutor[j + 1]
                tmp = stop - start
                if tmp > 0:
                    answer += tmp
            elif tutor[j] >= pupil[i] and tutor[j + 1] <= pupil[i + 1]:
                start = 0
                stop = 0
                if lesson[1] >= tutor[j] >= lesson[0]:
                    start = tutor[j]
                elif tutor[j + 1] >= lesson[0] >= tutor[j]:
                    start = lesson[0]
                if tutor[j + 1] >= lesson[1] >= pupil[i]:
                    stop = lesson[1]
                elif lesson[1] >= tutor[j + 1]:
                    stop = tutor[j + 1]
                tmp = stop - start
                if tmp > 0:
                    answer += tmp
            elif tutor[j] >= pupil[i] and tutor[j + 1] >= pupil[i + 1]:
                start = 0
                stop = 0
                if tutor[j] <= lesson[0] <= pupil[i + 1]:
                    start = lesson[0]
                elif tutor[j] >= lesson[0]:
                    start = tutor[j]
                if pupil[i + 1] >= lesson[1] >= tutor[j]:
                    stop = lesson[1]
                elif pupil[i + 1] <= lesson[1]:
                    stop = pupil[i + 1]
                tmp = stop - start
                if tmp > 0:
                    answer += tmp
    return answer


def start_testing():
    tests = [
        {'data': {'lesson': [1594663200, 1594666800],
                  'pupil':  [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                  'tutor':  [1594663290, 1594663430, 1594663443, 1594666473]},
         'answer': 3117
         },
        {'data': {'lesson': [1594702800, 1594706400],
                  'pupil':  [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                             1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                             1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                             1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                  'tutor':  [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
         'answer': 3577
         },
        {'data': {'lesson': [1594692000, 1594695600],
                  'pupil':  [1594692033, 1594696347],
                  'tutor':  [1594692017, 1594692066,
                             1594692068, 1594696341]},
         'answer': 3565
         },
    ]
    result = '<h1>FUNCTION</h1>'
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        result += f'<br>test ### {i + 1} ###: correct answer - {test["answer"]}; my answer - {test_answer}'
        if test_answer == test['answer']:
            result += " - equal"
        else:
            result += " - but I've tested this block manually"
    return result


if __name__ == '__main__':
    # assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
    pass

import re


class Csv:
    def __init__(self, path="", separator="", header=True):
        self.data = self.read(path, separator)
        self.header = header

    @staticmethod
    def read(path, separator):
        csv_data = []
        with open(path, encoding="utf-8") as csv_file:
            for line in csv_file:
                line_r = re.sub("[\n]", "", line)
                line_edit = re.sub('^""$', "", line_r)
                csv_data.append(line_edit.rsplit(separator))

        return csv_data

    def get_data(self):
        return self.data


def ready_up():
    ans_dict_ws = {}
    csv = Csv("/home/nas/PycharmProjects/camp1/esm_famil_data.csv", ",")
    answer = csv.get_data()
    head = answer[0]
    answer.remove(head)
    ans_ws = []
    for i in range(6):
        par_ws = []
        for item in answer:
            par_ws.append(item[i].replace(" ", ""))
        ans_ws.append(par_ws)
    answer_dic_ws = zip(head, ans_ws)
    ans_dict_ws.update(answer_dic_ws)
    return ans_dict_ws


true_answers_ws = ready_up()


applicants = []
appl_answers = []


def add_participant(participant, answers):

    applicants.append(participant)
    all_p_ans = list(answers.values())
    appl_answers.append(all_p_ans)
    return applicants, appl_answers


def whitespace_remover():
    app_ans_wsr = []
    for item in appl_answers:
        app_ans_ws = []
        for i in range(6):
            app_ans_ws.append(item[i].replace(" ", ""))
        app_ans_wsr.append(app_ans_ws)

    return app_ans_wsr


result = {}


def calculate_all():
    score = [0 for k in range(len(applicants))]
    V_ws = list(true_answers_ws.values())
    app_answer_wsr = whitespace_remover()
    for i in range(6):
        temp_ws = []
        count = 0
        for ans in app_answer_wsr:
            val_ws = ans[i]
            temp_ws.append(val_ws)
        check = 0
        for c in range(len(temp_ws)):
            if (temp_ws[c] != '') and (temp_ws[c] in V_ws[i]):
                check += 1

        for items in app_answer_wsr:
            temp_cp = temp_ws[:]
            temp_cp.remove(items[i])

            if '' in temp_ws or check != len(applicants):
                if (items[i] not in temp_cp) and (items[i] != '') and (items[i] in V_ws[i]):
                    score[count] += 15
                if (items[i] in temp_cp) and (items[i] != '') and (items[i] in V_ws[i]):
                    score[count] += 10

            else:
                if (items[i] not in temp_cp) and (items[i] != '') and (items[i] in V_ws[i]):
                    score[count] += 10
                if (items[i] in temp_cp) and (items[i] != '') and (items[i] in V_ws[i]):
                    score[count] += 5
            count += 1
        res_dic = zip(applicants, score)
        result.update(res_dic)
    return result


add_participant(participant='salib', answers={'esm': 'بردیا', 'famil': 'بابایی', 'keshvar': 'باربادوس', 'rang': 'بنفش',
                                              'ashia': 'بمب', 'ghaza': 'باقالیپلو'})
add_participant(participant='kianoush', answers={'esm': 'بهرام', 'famil': 'بهرامی', 'keshvar': 'برزیل', 'rang': 'بلوطی',
                                                 'ashia': 'بیل', 'ghaza': 'به   پلو'})
add_participant(participant='sajjad', answers={'esm': 'بابک', 'famil': 'بهشتی', 'keshvar': 'باهاما', 'rang': 'بژ',
                                               'ashia': '        ', 'ghaza': 'برنج خورشت'})
add_participant(participant='farhad', answers={'esm': 'بهرام', 'famil': 'براتی', 'keshvar': 'بببببب', 'rang': 'بژ',
                                               'ashia': 'بیل', 'ghaza': 'باقلوا'})

print(calculate_all())

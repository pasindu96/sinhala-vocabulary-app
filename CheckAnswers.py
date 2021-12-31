import pandas as pd
from fuzzywuzzy import process
import DBConnection


class StudentResult:
    def __init__(self, student_id, question_type, question, answer, letter_count, result,
                 similarity, weaken_letter_types, time_taken):
        self.student_id = student_id
        self.question_type = question_type
        self.question = question
        self.answer = answer
        self.letter_count = letter_count
        self.result = result
        self.similarity = similarity
        self.weaken_letter_types = weaken_letter_types
        self.time_taken = time_taken


# Function for getting the similarity fuzzy value
def get_matches(word, choices):
    results = process.extract(word, choices, limit=1)
    return results


# Test case
# test = ["ගෝණා"]
# print(get_matches("ගණඑළවළු", test))


# Compare the answer with given word
def CompareWord(question, answer, letter_count):
    if question == answer:
        # Store in DB -> userid, score, time taken, similarity
        result = StudentResult(1, "MCQ", question, answer, letter_count, "Correct", 1, [], 800)
        DBConnection.writeToDatabase(result)
        return
    else:
        # Check the similarity and get the fuzzy value
        similarity = get_matches(answer, [question])[0][1]
        # Check the mismatching letter is mahaprana, sanghaka or moordhaja
        characterList = CheckLetters(question, answer)
        # print(characterList)
        # Store in DB -> userid, score, time taken, weaken area
        # student_id, question_type, question, answer, result,similarity, weaken_letter_types, time_taken
        result = StudentResult(1, "MCQ", question, answer, letter_count, "Incorrect", float(similarity)/100, characterList, 2400)
        DBConnection.writeToDatabase(result)
        return


def CheckLetters(question, answer):
    questionList = []
    answerList = []

    for i in range(0, len(question)):
        # characterList.append(word[i])
        if questionType(question[i]) != "default":
            questionList.append(questionType(question[i]))

    for i in range(0, len(answer)):
        # characterList.append(word[i])
        if questionType(answer[i]) != "default":
            answerList.append(questionType(answer[i]))

    return findWeakLetterTypes(questionList, answerList)


# Identify the special letter types which are not included in provided answer
def findWeakLetterTypes(question, answer):
    list1 = question.copy()
    list2 = answer.copy()
    for i in question:
        if len(list2) > 0:
            for j in answer:
                if i == j:
                    list1.remove(i)
                    list2.remove(j)

    return list1 + list2


# Check the Type of the incorrect answer letter
def questionType(category):
    switcher = {
        'ණ': 'ණ-Moordhaja',
        'ළ': 'ළ-Moordhaja',
        'ෂ': 'ෂ-Moordhaja',

        'ඟ': 'ඟ-Sanghaka',
        'ඦ': 'ඦ-Sanghaka',
        'ඬ': 'ඬ-Sanghaka',
        'ඳ': 'ඳ-Sanghaka',
        'ඹ': 'ඹ-Sanghaka',

        'ඵ': 'ඵ-Mahaprana',
        'භ': 'භ-Mahaprana',
        'ධ': 'ධ-Mahaprana',
        'ථ': 'ථ-Mahaprana',
        'ඨ': 'ඨ-Mahaprana',
        'ඡ': 'ඡ-Mahaprana',
        'ඪ': 'ඪ-Mahaprana',
        'ඝ': 'ඝ-Mahaprana',
        'ඛ': 'ඛ-Mahaprana',
        'ඣ': 'ඣ-Mahaprana'
        
    }
    return switcher.get(category, "default")


CompareWord("ගෝණා", "ගණ", 2)
CompareWord("පැළ", "පැළ", 2)
CompareWord("යාළුවා", "යාලුවා", 3)
CompareWord("කුඹුර", "කුබුර", 3)
CompareWord("කොස්ස", "කොස්ස", 3)
CompareWord("නළාව", "නළාව", 3)
CompareWord("රේඛාව", "රේඛාව", 3)
CompareWord("ඔටුන්න", "ඔටුන්න", 4)
CompareWord("ඉබ්බා", "ඉබ්බා", 3)
CompareWord("ඖෂධ", "ඖෂද", 3)
CompareWord("එළවළු", "එලවළු", 4)
CompareWord("ත්‍රිකෝණය", "ත්‍රිකෝනය", 4)
CompareWord("කළු ලෑල්ල", "කළු ලෑල්ල", 5)
CompareWord("ෆලූඩා", "ෆලූඩා", 3)
CompareWord("වඳුරා", "වදුරා", 3)
CompareWord("පඬුරු", "පඬුරු", 3)
CompareWord("භාජනය", "භාජනය", 4)
CompareWord("විශ්වය", "විශ්වය", 4)
CompareWord("භය", "බය", 2)
CompareWord("ජිරාෆ්", "ජිරාෆ්", 3)

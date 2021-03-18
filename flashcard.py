import re
import random
import streamlit as st
import numpy as np

source = 'C:/Users/chisa/desktop/FlashCard/verb01.txt'

f = open(source, "r", encoding='utf-8')
d = f.read()
f.close()

keys = re.findall(r'[^a-z\n]+', d)

source02 = 'C:/Users/chisa/desktop/FlashCard/verb01answer.txt'

f2 = open(source02, "r", encoding='utf-8')
d2 = f2.read()
f2.close()

values = re.findall(r'[^a-z\n]+', d2)

word_dict = dict(zip(keys,values))

st.title('古文単語練習')

"""
### 次の（　）の単語の意味を答えなさい。

"""
question_num = 1
for q in range(question_num):

    random_index = np.random.randint(
        low=0, high=len(keys), size=question_num)

    question_word = keys[random_index[q]]
    correct_answer = word_dict[question_word]
    c_answer = keys[random_index[q]]

    st.header(question_word)

    values_copy = values.copy()
    values_copy.remove(correct_answer)
    wrong_answers = random.sample(values_copy, 3)

    answer_options = [correct_answer] + wrong_answers
    random.shuffle(answer_options)

    st.subheader(answer_options)

    expander = st.beta_expander('答えを表示する')
    expander.header(c_answer)


button = st.button('次の問題を表示する')

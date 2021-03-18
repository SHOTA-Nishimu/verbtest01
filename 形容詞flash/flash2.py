import re
import random
import streamlit as st
import numpy as np

source = 'C:\\Users\\chisa\\desktop\\FlashCard\\形容詞flash\\形容詞.txt'

with open(source, encoding='utf-8') as f:
        d = f.read()    

keys = re.findall('[一-𥻘あ-ん()=~[\]、。「」々・……]+',d)
#print(d)

source02 ='C:/Users/chisa/desktop/FlashCard/形容詞flash/形容詞answer.txt'

with open(source02, encoding='utf-8') as f2:
    d2 = f2.read()    

values = re.findall('[一-𥻘あ-ん()=~[\]、。「」々・……]+',d2)
#print(d2)

word_dict = dict(zip(keys, values))
#print(word_dict)

st.title('古文単語確認～形容詞～')

"""
### 次の（　）の単語の意味を答えなさい。

"""



question_num=1
for q in range(question_num):

    random_index=np.random.randint(low=0, high=len(keys),size=question_num )

    question_word = keys[random_index[q]]
    correct_answer = word_dict[question_word]
    c_answer = values[random_index[q]]

    st.header(question_word)

    values_copy= values.copy()
    values_copy.remove(correct_answer)
    wrong_answers = random.sample(values_copy, 3)
            
    answer_options = [correct_answer]+ wrong_answers
    random.shuffle(answer_options)
    
    st.subheader(answer_options)
    
    expander = st.beta_expander('答えを表示する')
    expander.header(c_answer)


button =st.button('次の問題を表示する')

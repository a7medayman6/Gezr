import sys

import streamlit as st

from streamlit import cli as stcli

from ArStem import ArabicStemmer


stemmer = ArabicStemmer()


def main():
    st.title('ArStem Stemmer')
    st.markdown('''##### ArStem is a light-based Arabic stemmer.''')

    sentence = str(st.text_area('الجٌملة', placeholder='ادخل جملة لاستخراج جذورها')).strip()
    if st.button('Stem'):
        stemmed, df = stemmer.stem(sentence, verbose=True)

        simplified_df = df[['Root', 'Tokens']]

        st.markdown('''### Stemmed Sentence''')
        st.write(stemmed)

        st.markdown('''### Results''')
        st.dataframe(simplified_df)

        st.markdown('''### Detailed Results''')
        st.dataframe(df)

# تمركز, تزحلق, ترجمان, مطلسم, جمهورية, يتمرجح, هرولة, متعجرف, تزعزع, اتبع, أفاستسقيناكموها, وليتلطف, مخطئ
# يذهب الرجل إلى عمله يوميًا بسيارته. 

if __name__ == '__main__':
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
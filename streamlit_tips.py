import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title('Streamlit tips and tricks 🎈')

st.sidebar.subheader('App inputs')
select_size = st.sidebar.selectbox('Choose header type', [3, 2, 1])
subheader_size = '#' * select_size

st.write(subheader_size, 'Tip 1: Show off your work')
st.write('''Your project needs visuals, whether that\'s a video, audio clip, image, map, chart, or table. Streamlit supports
all major charting libraries. Check out [docs.streamlit.io](http://docs.streamlit.io) to explore all the options.''')

data = [15, 10, 7]
labels = ['Good', 'Bad', 'Ugly']

fig = go.Figure(data=[go.Pie(labels=labels, values=data, hole=.5)])
fig.update_layout(
    autosize=False,
    width=500,
    height=300)
st.write(fig)

'-------------------'

st.write(subheader_size, 'Tip 2: Make it interactive')
st.write('''Any variable can be made interactive by using a widget. Use widgets like `st.slider`, `st.selectbox`, and `st.radio`
to let users of your app change parameters, select different inputs, or modify the output.
''')
number = st.number_input('Number', value=1)
exponent = st.slider('Exponent',1,100)
output = number ** exponent
st.write(number, ' to the power of ', exponent, ' equals ', output)

'-------------------'

st.write(subheader_size, 'Tip 3: Move widgets to sidebar')
st.write('''By adding `st.sidebar` to any of your widgets you can move them to the sidebar on the left. This
cleans up the layout and makes sure that your controls are always visible. _Note: some widgets are best
left inline, especially if they only control one small part of the app._
''')

sidebar_code = (
'''
st.sidebar.subheader('App inputs')
select_size = st.sidebar.selectbox('Choose header type', [3, 2, 1])
''')

st.code(sidebar_code, language='python')

st.write('#### 👈👈 &nbsp; use the selectbox to change the header types!')

'-------------------'

st.write(subheader_size, 'Tip 4: Add some text')
st.write('''Write out the important parts that need explanation or use text to break up the layout of the app.
Have a friend play with the app and tell you what isn't obvious, so you can add text for those sections.
If you want to add text in the sidebar use `st.sidebar.subheader` or `st.sidebar.text`.''')

'-------------------'

st.write(subheader_size, 'Tip 5: Hide extra text')
st.write('''To keep your app layout clean, you can add in explanations or extra info, graphs, etc. by hiding
that information behind a checkbox or a selectbox. See two examples below.''')

st.write('###')

if st.checkbox('Show explanation'):
    st.write('''
        > ###### We balance probabilities and choose the most likely. It is the scientific use of the imagination, but we have always some material basis on which to start our speculation. - Sherlock Holmes
        ''')

st.write('###')

selectbox = st.selectbox('Show more analyses', ('','Raw data', 'Extra chart'))

data = np.random.rand(3,2)

if selectbox == 'Raw data':
    st.table(data)
elif selectbox == 'Extra chart':
    st.line_chart(data)

'-------------------'

st.write(subheader_size, 'Tip 6: Use caching to speed up your app')
st.write('''You want the app to run quickly for your users, so use `st.cache` for any expensive
computation or data pulls. Read more about [how st.cache works](https://docs.streamlit.io/caching.html)
and check out [documentation on advanced caching](https://docs.streamlit.io/advanced_caching.html)
for how use `st.cache` to store a TensorFlow object or read from a MySQL database''')

'-------------------'

st.write(subheader_size, 'Tip 7: Put the good stuff at the top')
st.write('''If your project is a step by step walk through - then ignore this. If it\'s an app for someone to use, then you want
to get them to the good, interactive stuff as soon as possible. This also means setting your app to have a default good outcome
that users can see first before interacting with the app.''')

dog_img = 'https://www.publicdomainpictures.net/pictures/240000/velka/funny-dog-15091160994Oj.jpg'
with st.echo():
    show_image = st.empty()
    if st.checkbox('Show image', value=True):
        show_image.image(dog_img, width=250)

st.write('''One way you can do that is with `st.empty`, which allows you to choose the order of where elements appear in the app.
In the example above the code for the checkbox has to come before the image, but we can use `st.empty` to have the image render
above the checkbox.''')

'-------------------'

st.write(subheader_size, 'Tip 8: Show some code (maybe)')
st.write('''If you're teaching a concept it can be useful to show off some code. You can use `st.code` to format code, or if
you want to show the code for something you are doing in the app you can use `with st.echo()` to have code shown inline with output.
''')

with st.echo():
    tasty = 'nom '
    st.write(tasty * 3)


'-------------------'
st.write(subheader_size, 'Tip 9: Do something delightful')
st.write('''Whenever possible try to use more exciting or fun examples, or for bonus points, add an
unexpected and memorable interaction.
''')
if st.button('Balloons!!!'):
    st.balloons()

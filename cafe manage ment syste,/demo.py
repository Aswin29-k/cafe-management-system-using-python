import streamlit as st

# Title of the app
st.title("Cafe management system")

# Slider to select a number
st.text("welcome to my cafa  please place your order")

 

# Radio button to choose an option
option = st.radio('Choose your favorite snack:', ['milkshake', 'vada', 'tea', 'Grapes','juice'])


st.write(f'You selected: {option}')

st.subheader("description about the food")
  
if option == 'milkshake':
    st.write('the milkshake contain the milk,cream,sugar,choaclate,sugar 45 mg,rich protein 233mg')

elif option == 'vada':

    

    st.write('the vada contain high calioric and high fat content 23mg ')
elif option == 'tea':
    st.write('the teacontain the milk,cream,,sugar 100 mg,teapowder 233mg')

    
elif option == 'juice':
    st.write('the juice contain the apple,banana,mango,grapes,sugarcane,rich sugar content 233mg')

else:
    st.write('the milkshake contain the milk,cream,sugar,choaclate,sugar 45 mg,rich protein 233mg')


quantity=st.number_input("enter the quantity nof the order food")
if option == 'milkshake':
    st.write(f'sir your order  {option} and the quantity of the food   {quantity}and the biil rs  {100*quantity}')

elif option == 'vada':
    st.write(f'sir your order  {option} and the quantity of the food   {quantity}and the biil rs  {50*quantity}')
    
elif option == 'tea':st.write(f'sir your order  {option} and the quantity of the food   {quantity}and the biil rs  {70*quantity}')

    
elif option == 'Grapes':
    st.write(f'sir your order  {option} and the quantity of the food   {quantity}and the biil rs  {180*quantity}')
elif option == 'juice':
    st.write(f'sir your order  {option} and the quantity of the food   {quantity}and the biil rs  {200*quantity}')
    
    
else:
    st.write("plesase order some think")

if st.button("show rate"):
    st.write("milk shake:100rs")
    st.write("vada:100rs")
    st.write("tea:70rs")
    st.write("grapes:95rs")
    st.write("juice:60rs")
else:
    pass

with st.container():
    
    st.write("Here we can group multiple elements together.")
    comment=  st.chat_input("enter the comments here and share your personal  experience with us",)




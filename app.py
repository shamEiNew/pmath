from streamlit.proto.Button_pb2 import Button
from sympy.series.gruntz import build_expression_tree
from numtheory._continued_fractions import *
import streamlit as st



st.title("Some Theoretic Functions")


#Continued Fractions---1
def std_out(rational=True):
    if rational:
        a = st.text_input("Enter the numerator for Continued Fraction:")
        b = st.text_input("Enter the denominator for Continued Fraction:")
        if (a!='') and (b!=''):
            st.markdown(f"$${continued_fraction(f'{a}/{b}')}$$")
    else:
        st.markdown("**Use sqrt, pi, E, for entering square roots, pi, e respectively.\n  Use ^ for powers like 2^(1/5)**")
        x = st.text_input("Enter the number for Continued Fraction")
        k = st.text_input("Enter the number of terms to print:", value="15")
        if x!='':
                st.text(f"{k} terms are shown")
                st.markdown(f"$${continued_fraction(x, _rational=False, k=int(k))}$$")

def check_inputs():
    st.subheader("Continued Fractions")
    type_of_number = st.selectbox("Type of number",["Rational", "Irrational"])

    
    if type_of_number=="Rational":
        std_out()
        
    else:
        std_out(rational=False)

if __name__=="__main__":
    check_inputs()





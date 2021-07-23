from streamlit.proto.Button_pb2 import Button
from sympy.series.gruntz import build_expression_tree
from pymath.numtheory._continued_fractions import *
import streamlit as st
from pymath.numtheory import _sieves as sieves


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

def till_primes():
    st.header('Calculate Primes using Eratosthenes Sieve')
    a = st.text_input("Enter a positive integer for evaluating primes.")
    if a:
        try:
            st.markdown(f"The following is the list of primes upto {a}.")
            st.markdown(f"{sieves.eratosthenes_sieve(int(a))}")
        except:
            st.markdown("Please enter a valid positive integer")

if __name__=="__main__":
    apps = ('Continued Fractions', 'Primes')
    sidenav = st.sidebar.radio('Apps', apps, help='Choose to evaluate')
    if sidenav==apps[1]:
        till_primes()
    elif sidenav==apps[0]:
        check_inputs()
    
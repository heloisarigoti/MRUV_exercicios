import random
import streamlit as st
import cmath

st.set_page_config(page_title='Exercícios sobre MRUV para a prova de Física', page_icon="🧠", layout = 'centered', initial_sidebar_state = 'collapsed')

col1, col2 = st.columns(2)
with col1:
   apenas_int = st.toggle("Apenas números inteiros")

with col2:
   st.button("Nova questão")

def resolve_equacao(a, b, c):
    delta = (b ** 2) - (4 * a * c)

    sol1 = (-b + cmath.sqrt(delta)) / (2 * a)
    sol2 = (-b - cmath.sqrt(delta)) / (2 * a)

    return sol1, sol2

def criar_equacao(apenas_int=False):
    while True:
        sinal_a = (-1) ** random.randint(1, 2)
        sinal_b = (-1) ** random.randint(1, 2)
        sinal_c = (-1) ** random.randint(1, 2)

        a = random.randint(1, 30) * sinal_a
        b = random.randint(1, 30) * sinal_b
        c = random.randint(1, 30) * sinal_c

        if (apenas_int == True) and ((4 * a * c) < (b ** 2)) and (resolve_equacao(a, b, c)[0].real.is_integer()) and (resolve_equacao(a, b, c)[1].real.is_integer()) and (-b/(2*a)).is_integer():
            break

        if (apenas_int == False) and ((4 * a * c) < (b ** 2)):
            break

    return a, b, c, sinal_a, sinal_b, sinal_c

# print(a)
# print(b)
# print(c)
#
# print(f"S={c:+}{b:+}t{a:+}t²")


#Questao
i = random.randint(1,5)
if i==1:
    enunciado = "Um trem se move de acordo com a equação horária da posição"
if i==2:
    enunciado = "Uma bicicleta está se movendo segundo a equação horária da posição"
if i==3:
    enunciado = "Um avião está voando de acordo com a equação horária da posição"
if i==4:
    enunciado = "Um barco está navegando segundo a equação horária da posição"
if i==5:
    enunciado = "O Flash está correndo de acordo com a equação horária da posição"

a, b, c, sinal_a, sinal_b, sinal_c = criar_equacao(apenas_int)

st.header(enunciado + f" S={c:+}{b:+}t{a:+}t².", anchor = False)
st.header("Determine:", anchor = False)


#A
st.subheader(f"a) A posição inicial.", anchor = False)
with st.expander("Ver resposta"):
    st.write(f"S\u1D62 = {c:+} m")

#B
st.subheader(f"b) A velocidade inicial.", anchor = False)
with st.expander("Ver resposta"):
    st.write(f"V\u1D62 = {b:+} m/s")

# C
st.subheader(f"c) A aceleração.", anchor=False)
with st.expander("Ver resposta"):
    st.write(f"a = {2*a:+} m/s²")

# D
instante_letra_d = random.randint(1,10)

def posicao_no_instante_x(t):
    posicao = c + b*t + a*t*t
    return posicao

st.subheader(f"d) A posição no instante {instante_letra_d} s.", anchor=False)
with st.expander("Ver resposta"):
    st.write(f"S({instante_letra_d}) = {posicao_no_instante_x(instante_letra_d):+} m")

# E
st.subheader(f"e) A equação horária da velocidade.", anchor=False)
with st.expander("Ver resposta"):
    st.write(f"V = {b:+}{2*a:+}t")

# F
instante_letra_f = random.randint(1,10)

def velocidade_no_instante_x(t):
    velocidade = b + 2*a*t
    return velocidade

st.subheader(f"f) A velocidade no instante {instante_letra_f} s.", anchor=False)
with st.expander("Ver resposta"):
    st.write(f"V({instante_letra_f}) = {velocidade_no_instante_x(instante_letra_f)} m/s")


# G
if apenas_int:
    num_random = random.randint(1, 20)
    posicao_letra_g = posicao_no_instante_x(num_random)
else:
    num_random = random.randint(1, 10)
    posicao_letra_g = random.randint(posicao_no_instante_x(num_random)-100,posicao_no_instante_x(num_random)+100)



st.subheader(f"g) O instante em que a posição é {posicao_letra_g} m.", anchor=False)
with st.expander("Ver resposta"):
    sol1, sol2 = resolve_equacao(a, b, c-posicao_letra_g)
    if  sol1.real < 0:
        st.markdown("~~" + f"t₁ = {sol1.real:.2f} s".replace('.', ',') + "~~" + " :x:")
    else:
        st.markdown(f"t₁ = {sol1.real:.2f} s".replace('.', ',') + " :heavy_check_mark:")

    if  sol2.real < 0:
        st.markdown("~~" + f"t₂ = {sol2.real:.2f} s".replace('.', ',') + "~~" + " :x:")
    else:
        st.markdown(f"t₂ = {sol2.real:.2f} s".replace('.', ',') + " :heavy_check_mark:")

# H
num_random = random.randint(1,50)
velocidade_letra_h = velocidade_no_instante_x(num_random)


st.subheader(f"h) O instante em que a velocidade é {velocidade_letra_h} m/s.", anchor=False)
with st.expander("Ver resposta"):
    resposta = (velocidade_letra_h-b)/(2*a)
    st.markdown(f"t = {resposta:.0f} s".replace('.', ','))

# I
st.subheader(f"I) A classificação do movimento no momento inicial", anchor=False)
with st.expander("Ver resposta"):
    if sinal_b>0:
        movimento1 = "Progressivo"
    else:
        movimento1 = "Retrógrado"

    if sinal_a == sinal_b:
        movimento2 = "Acelerado"
    else:
        movimento2 = "Retardado"

    st.markdown(f"{movimento1}  {movimento2}")

# J
st.subheader(f"J) O instante em que o movimento muda de sentido", anchor=False)
with st.expander("Ver resposta"):
    if -b/(2*a) < 0:
        st.markdown("~~" + f"t = {-b/(2*a):.0f} s".replace('.', ',') + "~~" + " :x:")
        st.markdown("O tempo negativo significa a mudança de sentido aconteceu antes do início do movimento, o que não possui sentido físico. Em outras palavras, esse movimento não muda de sentido.")
    else:
        st.markdown(f"t = {-b/(2*a):.0f} s".replace('.', ',') + " :heavy_check_mark:")

# K
st.subheader(f"K) A posição na qual o movimento muda de sentido", anchor=False)
with st.expander("Ver resposta"):

    if -b/(2*a) < 0:
        st.markdown("~~" + f"S({-b/(2*a):.0f}) = {posicao_no_instante_x(-b/(2*a)):.0f} m".replace('.', ',') + "~~" + " :x:")
        st.markdown("O tempo negativo significa algo que aconteceu antes do início do movimento, o que não possui sentido físico. Em outras palavras, o objeto nunca estará nessa posição")
    else:
        st.markdown(f"S({-b/(2*a):.0f}) = {posicao_no_instante_x(-b/(2*a)):.0f} m".replace('.', ',') + " :heavy_check_mark:")


import random
import streamlit as st
import cmath

st.set_page_config(page_title='Exercícios sobre MRUV para a prova de Física', page_icon="🧠", layout = 'centered', initial_sidebar_state = 'collapsed')

col1, col2 = st.columns(2)
with col1:
   apenas_int = st.toggle("Apenas números inteiros", value=True)

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

        a = random.randint(1, 20) * sinal_a
        b = random.randint(1, 50) * sinal_b
        c = random.randint(1, 30) * sinal_c

        if (apenas_int == True) and ((4 * a * c) > (b ** 2)) and (resolve_equacao(a, b, c)[0].real.is_integer()) and (resolve_equacao(a, b, c)[1].real.is_integer()) and (-b/(2*a)).is_integer():
            break

        if (apenas_int == False) and ((4 * a * c) > (b ** 2)):
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
    st.write(f"Para calcular a posição precisamos usar a equação horária da posição.")
    st.latex(f"S={c:+}{b:+}t{a:+}t²")
    st.write(f"Como queremos calcular a posição no instante t = {instante_letra_d} s, substítuímos t na equação acima por {instante_letra_d} s")
    st.latex(f"S({instante_letra_d})={c:+}{b:+}\\times{instante_letra_d}{a:+}\\times{instante_letra_d}²")
    st.write(f"Primeiro resolvemos a potência {instante_letra_d}².")
    st.latex(f"S({instante_letra_d})={c:+}{b:+}\\times{instante_letra_d}{a:+}\\times{instante_letra_d*instante_letra_d}")
    st.markdown(f"Agora resolvemos as multiplicações ${b:+}\\times{instante_letra_d}$ e ${a:+}\\times{instante_letra_d*instante_letra_d}$.")
    st.latex(f"S({instante_letra_d})={c:+}{b*instante_letra_d:+}{a*instante_letra_d*instante_letra_d:+}")
    st.write(f"Finalmente, somamos todos os valores positivos e subtraímos todos os valores negativos.")
    st.latex(f"S({instante_letra_d})={c+b*instante_letra_d+a*instante_letra_d*instante_letra_d:+} m")

    #st.write(f"S({instante_letra_d}) = {posicao_no_instante_x(instante_letra_d):+} m")

# E
st.subheader(f"e) A equação horária da velocidade.", anchor=False)
with st.expander("Ver resposta"):
    st.write(f"A equação horária da velocidade segue o seguinte modelo.")
    st.latex(f"V = V_i + at")
    st.markdown(f"Como vimos na letra b), $V_i = {b:+} m/s$.")
    st.markdown(f"Como vimos na letra c), $a = {2*a:+} m/s²$.")
    st.markdown(f"Substituindo $V_i$ e $a$ na equação, temos:")
    st.latex(f"V = {b:+}{2*a:+}t")

    #st.write(f"V = {b:+}{2*a:+}t")

# F
instante_letra_f = random.randint(1,10)

def velocidade_no_instante_x(t):
    velocidade = b + 2*a*t
    return velocidade

st.subheader(f"f) A velocidade no instante {instante_letra_f} s.", anchor=False)
with st.expander("Ver resposta"):
    st.write(f"Para calcular a velocidade precisamos usar a equação horária da velocidade, que montamos na letra e).")
    st.latex(f"V = {b:+}{2 * a:+}t")
    st.write(f"Como queremos calcular a velocidade no instante t = {instante_letra_f} s, substítuímos t na equação acima por {instante_letra_f} s.")
    st.latex(f"V = {b:+}{2 * a:+}\\times{instante_letra_f}")
    st.markdown(f"Primeiro resolvemos a multiplicação ${2 * a:+}\\times{instante_letra_f}$.")
    st.latex(f"V = {b:+}{2 * a * instante_letra_f:+}")
    st.write(f"Finalmente, somamos todos os valores positivos e subtraímos todos os valores negativos.")
    st.latex(f"V = {b+2 * a * instante_letra_f:+} m/s")

    #st.write(f"V({instante_letra_f}) = {velocidade_no_instante_x(instante_letra_f)} m/s")


# G
posicao_letra_g = posicao_no_instante_x(random.randint(1, 20))



st.subheader(f"g) O instante em que a posição é {posicao_letra_g} m.", anchor=False)
with st.expander("Ver resposta"):
    st.write(f"Para calcular o instante em que a posição é {posicao_letra_g} m, precisamos usar a equação horária da posição.")
    st.latex(f"S={c:+}{b:+}t{a:+}t²")
    st.write(f"Primeiro substituímos o valor de $S = {posicao_letra_g} m$")
    st.latex(f"{posicao_letra_g}={c:+}{b:+}t{a:+}t²")
    st.write(f"Agora passamos o ${posicao_letra_g}$ para o outro lado, trocando a operação.")
    st.latex(f"0={-posicao_letra_g:+}{c:+}{b:+}t{a:+}t²")
    st.write(f"Resolvemos a conta ${-posicao_letra_g:+}{c:+}$.")
    st.latex(f"0={-posicao_letra_g+c:+}{b:+}t{a:+}t²")
    st.write(f"A equação acima é uma equação de segundo grau e pode ser resolvida usando a fórmula de Bhaskara:")
    st.latex(r"t = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
    st.write(f"Onde a é o número multiplicando t², b é o número multiplicando t, e c é o número que está sozinho.")
    st.write(f"""Nesse caso:
            \n $a = {a:+}$ 
            \n $b = {b:+}$
            \n $c = {-posicao_letra_g+c:+}$
""")
    st.write(f"Agora resolvemos a parte de dentro da raiz quadrada, que é o delta (Δ).")
    st.latex(r"\Delta = b^2 - 4ac")
    st.latex(f"\Delta = ({b:+})^2 - 4\\times({a:+})\\times({-posicao_letra_g+c:+})")
    st.write(f"Resolvemos a potência $({b:+})^2$.")
    st.latex(f"\Delta = {b*b:+} - 4\\times({a:+})\\times({-posicao_letra_g + c:+})")
    st.write(f"Resolvemos a multiplicação $- 4\\times({a:+})\\times({-posicao_letra_g + c:+})$.")
    st.latex(f"\Delta = {b * b:+}{-4*a*(-posicao_letra_g + c):+}")
    st.latex(f"\Delta = {(b * b)-4*a*(-posicao_letra_g + c):+}")
    st.write(f"Agora que calculamos o delta, precisamos calcular as duas raízes. Começamos substituindo a, b e Δ.")

    delta = (b * b) - 4 * a * (-posicao_letra_g + c)
    resultado_raiz = delta ** 0.5

    colA, colB = st.columns(2)
    with colA:
        st.latex(r"t_1 = \frac{-b + \sqrt{\Delta}}{2a}")
        if a < 0:
            st.latex(f"t_1 = \\frac{{{-b} + \\sqrt{{{delta}}}}}{{2\\times({a})}}")
            st.latex(f"t_1 = \\frac{{{-b} + {resultado_raiz:.0f}}}{{2\\times({a})}}")
            st.latex(f"t_1 = \\frac{{{-b} + {resultado_raiz:.0f}}}{{{2*a}}}")
        else:
            st.latex(f"t_1 = \\frac{{{-b} + \\sqrt{{{delta}}}}}{{2\\times{a}}}")
            st.latex(f"t_1 = \\frac{{{-b} + {resultado_raiz:.0f}}}{{2\\times{a}}}")
            st.latex(f"t_1 = \\frac{{{-b} + {resultado_raiz:.0f}}}{{{2*a}}}")

        st.latex(f"t_1 = \\frac{{{(-b+resultado_raiz):.0f}}}{{{2 * a}}}")

        if apenas_int:
            st.latex(f"t_1 = {((-b + resultado_raiz)/(2 * a)):.0f} s")
        else:
            st.latex(f"t_1 = {((-b + resultado_raiz) / (2 * a)):.2f} s")
    with colB:
        st.latex(r"t_2 = \frac{-b - \sqrt{\Delta}}{2a}")
        if a < 0:
            st.latex(f"t_2 = \\frac{{{-b} - \\sqrt{{{delta}}}}}{{2\\times({a})}}")
            st.latex(f"t_2 = \\frac{{{-b} - {resultado_raiz:.0f}}}{{2\\times({a})}}")
            st.latex(f"t_2 = \\frac{{{-b} - {resultado_raiz:.0f}}}{{{2 * a}}}")
        else:
            st.latex(f"t_2 = \\frac{{{-b} - \\sqrt{{{delta}}}}}{{2\\times{a}}}")
            st.latex(f"t_2 = \\frac{{{-b} - {resultado_raiz:.0f}}}{{2\\times{a}}}")
            st.latex(f"t_2 = \\frac{{{-b} - {resultado_raiz:.0f}}}{{{2 * a}}}")

        st.latex(f"t_2 = \\frac{{{(-b - resultado_raiz):.0f}}}{{{2 * a}}}")

        if apenas_int:
            st.latex(f"t_2 = {((-b - resultado_raiz) / (2 * a)):.0f} s")
        else:
            st.latex(f"t_2 = {((-b - resultado_raiz) / (2 * a)):.2f} s")

    st.write("Valores negativos de tempos não possuem significado físico, por isso apenas as raízes positivas são respostas da questão g).")


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
    st.write(f"Para calcular o instante em que a velocidade é {velocidade_letra_h} m/s, precisamos usar a equação horária da velocidade, que montamos na letra e).")
    st.latex(f"V = {b:+}{2 * a:+}t")
    st.write(
        f"Substítuímos V na equação acima por {velocidade_letra_h} m/s.")
    st.latex(f"{velocidade_letra_h:+} = {b:+}{2 * a:+}t")
    st.markdown(f"Primeiro passamos {b:+} para o outro lado, trocando seu sinal.")
    st.latex(f"{velocidade_letra_h:+} {-b:+}= {2 * a:+}t")
    st.latex(f"{(velocidade_letra_h-b):+} = {2 * a:+}t")
    st.write(f"Agora, passamos o {2*a:+} dividindo.")
    st.latex(f"\\frac{{{(velocidade_letra_h-b):+}}}{{{(2 * a):+}}} = t")
    st.latex(f"{((velocidade_letra_h-b)/(2 * a)):+.0f} = t")
    st.write(f"Ou seja.")
    st.latex(f"t = {((velocidade_letra_h-b)/(2 * a)):+.0f} s")




# I
st.subheader(f"I) A classificação do movimento no momento inicial", anchor=False)
with st.expander("Ver resposta"):
    if sinal_b>0:
        st.write("Como o sinal (sentido) da velocidade é positivo, temos um movimento PROGRESSIVO.")
        movimento1 = "Progressivo"
    else:
        st.write("Como o sinal (sentido) da velocidade é negativo, temos um movimento RETRÓGRADO.")
        movimento1 = "Retrógrado"

    if sinal_a == sinal_b:
        st.write("Como os sinais (sentidos) da velocidade e da aceleração são iguais, temos um movimento ACELERADO.")
        movimento2 = "Acelerado"
    else:
        st.write("Como os sinais (sentidos) da velocidade e da aceleração são contrários, temos um movimento RETARDADO.")
        movimento2 = "Retardado"
    st.write("Assim, temos um:")
    st.markdown(f"{movimento1}  {movimento2}")

# J
st.subheader(f"J) O instante em que o movimento muda de sentido", anchor=False)
with st.expander("Ver resposta"):
    st.write(
        f"O movimento muda de sentido quando a velocidade passa pelo 0 m/s. Assim, a resolução é parecida com a letra h), mas agora a velocidade é 0 m/s.")
    st.latex(f"V = {b:+}{2 * a:+}t")
    st.write(
        f"Substítuímos V na equação acima por 0 m/s.")
    st.latex(f"0 = {b:+}{2 * a:+}t")
    st.markdown(f"Primeiro passamos {b:+} para o outro lado, trocando seu sinal.")
    st.latex(f"0 {-b:+}= {2 * a:+}t")
    st.latex(f"{(0 - b):+} = {2 * a:+}t")
    st.write(f"Agora, passamos o {2 * a:+} dividindo.")
    st.latex(f"\\frac{{{(0 - b):+}}}{{{(2 * a):+}}} = t")
    st.latex(f"{((0 - b) / (2 * a)):+.0f} = t")
    st.write(f"Ou seja.")
    st.latex(f"t = {((0 - b) / (2 * a)):+.0f} s")

    if -b/(2*a) < 0:
        st.markdown("~~" + f"t = {-b/(2*a):.0f} s".replace('.', ',') + "~~" + " :x:")
        st.markdown("O tempo negativo significa a mudança de sentido aconteceu antes do início do movimento, o que não possui sentido físico. Em outras palavras, esse movimento não muda de sentido.")
    else:
        st.markdown(f"t = {-b/(2*a):.0f} s".replace('.', ',') + " :heavy_check_mark:")

# K
st.subheader(f"K) A posição na qual o movimento muda de sentido", anchor=False)
with st.expander("Ver resposta"):
    st.write("Para descobrir a posição na qual o movimento muda de sentido, usamos a resposta da questão j) aplicada na equação horária da velocidade")
    st.latex(f"t = {((0 - b) / (2 * a)):+.2f} s")
    st.write(f"Para calcular a posição precisamos usar a equação horária da posição.")
    st.latex(f"S={c:+}{b:+}t{a:+}t²")
    st.write(
        f"Como queremos calcular a posição no instante t = {((0 - b) / (2 * a)):+.2f} s, substítuímos t na equação acima por {((0 - b) / (2 * a)):.2f} s")
    st.latex(f"S({((0 - b) / (2 * a)):+.2f})={c:+}{b:+}\\times{((0 - b) / (2 * a)):+.2f}{a:+}\\times{((0 - b) / (2 * a)):.2f}²")
    st.write(f"Primeiro resolvemos a potência {((0 - b) / (2 * a)):.2f}².")
    st.latex(
        f"S({((0 - b) / (2 * a)):+.2f})={c:+}{b:+}\\times{((0 - b) / (2 * a)):+.2f}{a:+}\\times{((0 - b) / (2 * a)) * ((0 - b) / (2 * a)):.2f}")
    st.markdown(
        f"Agora resolvemos as multiplicações ${b:+}\\times{((0 - b) / (2 * a)):+.2f}$ e ${a:+}\\times{((0 - b) / (2 * a)) * ((0 - b) / (2 * a)):.2f}$.")
    st.latex(f"S({((0 - b) / (2 * a)):+.2f})={c:+}{b * ((0 - b) / (2 * a)):+}{a * ((0 - b) / (2 * a)) * ((0 - b) / (2 * a)):.2f}")
    st.write(f"Finalmente, somamos todos os valores positivos e subtraímos todos os valores negativos.")
    st.latex(f"S({((0 - b) / (2 * a)):+.2f})={c + b * ((0 - b) / (2 * a)) + a * ((0 - b) / (2 * a)) * ((0 - b) / (2 * a)):.2f} m")


    if -b/(2*a) < 0:
        st.markdown("~~" + f"S({-b/(2*a):.2f}) = {posicao_no_instante_x(-b/(2*a)):.2f} m".replace('.', ',') + "~~" + " :x:")
        st.markdown("O tempo negativo significa algo que aconteceu antes do início do movimento, o que não possui sentido físico. Em outras palavras, o objeto nunca esteve nem estará nessa posição.")
    else:
        st.markdown(f"S({-b/(2*a):.2f}) = {posicao_no_instante_x(-b/(2*a)):.2f} m".replace('.', ',') + " :heavy_check_mark:")


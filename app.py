import streamlit as st
from pandas import DataFrame

st.set_page_config(layout="wide",page_title="Regras de convivência")

st.sidebar.markdown("<H1 style = 'color:Blue'>Acordo de Convivencia</H1>",unsafe_allow_html=True)
st.sidebar.markdown("<H4 style='color:#05f729'>Por </H4>",unsafe_allow_html=True)
st.sidebar.markdown("<H4 style='color:#05f729'>Pedro Alvares </H4>",unsafe_allow_html=True)
st.sidebar.markdown("<H4 style='color:#05f729'>Geovana </H4>",unsafe_allow_html=True)
st.sidebar.markdown("<H4 style='color:#05f729'>Ramos </H4>",unsafe_allow_html=True)

st.markdown("<H1 style = 'color:#05f729'>1- Manter o celular desligado ou em modo silencioso durante as aulas</H1>",unsafe_allow_html=True)
st.markdown("<H3> • O celular pode ser uma grande distração para os alunos em sala de aula.</H3>",unsafe_allow_html=True)
st.markdown("<H3> •  Em um único aparelho pode haver mil e uma utilidades que podem retirar a atenção de um aluno durante a aula</H3>",unsafe_allow_html=True)
st.markdown("<H3> • Segundo pesquisar da Fundação Getúlio Vargas (FGV), revelou que o uso excessivo do telefone durante a sala de aula pode reduzir a efetividade da vida escolar em até 50% porcento. </H3>",unsafe_allow_html=True)

banco = DataFrame({"Estado":["Usam celular","Usam celular","Não usam celular","Não usam celular"],"Eficiência":[4,5,9,7]})

st.image("img.png",use_column_width=True)

st.markdown("<H1 style = 'color:#05f729'>2- Cumprir as tarefas escolares dentro dos prazos estabelecidos</H1>",unsafe_allow_html=True)
st.markdown("<H3> • Estudos comprovam que alunos cujo realizam as tarefas escolares dentro dos prazos estabelecidos, tem uma fixação melhor da matéria, assim obtendo um aumento gradual no desempenho escolar, quando comparado com alunos que não fazem as tarefas escolares. </H3>",unsafe_allow_html=True)

banco = DataFrame({"Estado":["Entregam no prazo","Entregam no prazo","Não entregam no prazo","Não entregam no prazo"],"Eficiência":[9,9,4,3]})

st.image("img2.png",use_column_width=True)

st.markdown("<H1 style = 'color:#05f729'>3- Estar aberto ao aprendizado e demonstrar interesse nas matérias estudadas </H1>",unsafe_allow_html=True)
st.markdown("<H3> • Estar aberto ao aprendizado, e uma das partes mais importantes na vida acadêmica de um estudante. Ter interesse em uma matéria, pode ampliar sua capacidade de memorização e aprendizado em grande escalar, tornando também o aprendizado algo satisfatório e divertido. </H3>",unsafe_allow_html=True)
st.markdown("<H3> • De acordo com pesquisar realizadas por escolas, usar um método mais “divertido” que possa prender o interesse da personalidade, pode ampliar o desempenho escolar em até 86% o desempenho de um aluno. </H3>",unsafe_allow_html=True)


banco = DataFrame({"Estado":["Alunos cujo gostam da matéria","Alunos cujo gostam da matéria","Não cujo não gostam da materia","Não cujo não gostam da materia"],"Eficiência":[9,8,1,1]})

st.image("img3.png",use_column_width=True)

st.markdown("<H1 style = 'color:#05f729'>4-  Não utilizar linguagem ofensiva ou desrespeitosa em sala de aula. </H1>",unsafe_allow_html=True)
st.markdown("<H3> • Usufruir que linguagem ofensiva ou desrespeitosa em sala de aula, pode ocasionar na síntese de um ambiente não amigável, e ofensivo, que poderá gerar um desinteresse e distração durante as aulas, fazendo da escola um lugar de “tormento”, de acordo com pesquisar realizadas em escolas e universidades, um ambiente mais amigável pode aumentar em até 3 vezes o desempenho acadêmico do aluno.  </H3>",unsafe_allow_html=True)

banco = DataFrame({"Estado":["Sala com linguagens ofensivas","Sala com linguagens ofensivas","Salas sem linguagens ofensivas","Salas sem linguagens ofensivas"],"Eficiência":[1,5,9,6]})

st.image("img4.png",use_column_width=True)

st.markdown("<H1 style = 'color:#05f729'>5- Levantar Dúvidas e fazer perguntas quando algo não estiver claro.  </H1>",unsafe_allow_html=True)
st.markdown("<H3> • Sanar dúvidas sobre a matéria é um marco importante no desenvolvimento escolar de um aluno, essa ação, pode impedir a síntese de lacunas, que mais cedo ou mais tarde, ocasionariam em dificuldades durante o seu ano letivo e na vida.</H3>",unsafe_allow_html=True)

st.markdown("<H1 style = 'color:#05f729'>6- Manter um ambiente de trabalho silencioso e propício ao estudo durante as atividades individuais </H1>",unsafe_allow_html=True)
st.markdown("<H3> • Um ambiente de trabalho silencioso, pode evitar possíveis distrações, tais distrações que poderiam reduzir o desempenho acadêmico, de acordo com pesquisar realizadas em escolas e universidades, ter um ambiente silencioso, pode aumentar a concentração e agilidade em resolver exercícios em até 3 vezes maior quando comparado a um ambiente barulhento </H3>",unsafe_allow_html=True)

banco = DataFrame({"Estado":["Atividade em silêncio","Atividade em silêncio","Atividade em ambiente barulhento","Atividade em ambiente barulhento"],"Eficiência":[10,9,1,4]})

st.image("img5.png",use_column_width=True)

st.markdown("<H1 style = 'color:#05f729'>7-  Evitar interrupções desnecessárias durante as explicações  </H1>",unsafe_allow_html=True)
st.markdown("<H3> • Durante o pensamento humano, criamos um fluxo de informações, cujo gira em torno de ideias criadas gradualmente em sua mente, esse fluxo pode ser facilmente interrompido, e em muitos casos, a possibilidade de recuperar a linha de raciocínio pode ser quase nula, assim, com isso, um professor pode perder totalmente a linha de pensamentos por uma simples interrupção, reduzindo assim a eficiência da aula. </H3>",unsafe_allow_html=True)

st.markdown("<H1 style = 'color:#05f729'>8- Prestar atenção e participar ativamente das atividades em sala de aula. </H1>",unsafe_allow_html=True)
st.markdown("<H3> • No processo de aprendizado, prestar atenção na aula e participar ativamente das aulas, força seu celebro a pensar, ajudando no processo de memorização, de acordo com estudos realizados em escolas e universidades, esses 2 hábitos podem aumentar o processo de aprendizado em até 150% em relação a pessoas que não tem esses hábitos. </H3>",unsafe_allow_html=True)

banco = DataFrame({"Estado":["Pessoas com esses hábitos","Pessoas com esses hábitos","Pessoas sem esses hábitos","Pessoas sem esses hábitos"],"Eficiência":[10,9,5,4]})

st.image("img6.png",use_column_width=True)

st.markdown("<H1 style = 'color:#05f729'>9-  Respeitar as regras de uso da tecnologia estabelecidas pela escola  </H1>",unsafe_allow_html=True)
st.markdown("<H3> • A tecnologia evolui gradualmente a cada ano, com isso, essa feramente pode ser um impulso no processo de ensino brasileiro, porém, essa tecnologia pode ser usada tanto para o impulso, quanto para o retardo da educação, em universidade mais modernas, foram utilizados tablets para o ensino, de acordo com dados estatísticos, com o uso dessa tecnologia para estudos, usada de maneira correta , ocasionou um rendimento de 79%, porém, essa tecnologia, se usada de forma errada pode também causa, um desempenho negativo. </H3>",unsafe_allow_html=True)

banco = DataFrame({"Estado":["Escolas que utilizam essa tecnologia","Escolas que utilizam essa tecnologia","Escolas que não utilizam essa tecnologia","Escolas que não utilizam essa tecnologia"],"Eficiência":[7,9,1,2]})

st.image("img7.png",use_column_width=True)

st.markdown("<H1 style = 'color:#05f729'>10- Tratar o material escolar e as instalações da sala de aula com cuidado e respeito </H1>",unsafe_allow_html=True)
st.markdown("<H3> • Todos gostamos que o material que usufruímos esteja em bons estados, porém, para que isso seja possível, precisamos que todos tratem tal material com respeito e cuidado, para que esse material venha durar anos e anos. </H3>",unsafe_allow_html=True)

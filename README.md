


### Desenvolva um código em na linguagem C/C++, Java, JS ou Python que emule cadeias geradas por expressões regulares. De modo geral, o usuário informará uma expressão regular e terá como retorno algumas cadeias desta expressão.


#### Obs.1: A documentação também será ponto de avaliação. 
#### Obs.2: A atividade pode ser realizada em dupla.

#### Ex1:
- ./a.out  01*
- Resultado: 0, 01, 011,...

#### Ex2:
- ./a.out  01^+
- Resultado: 01, 011, 0111,...

#### Ex3:
- ./a.out  (01)^+
- Resultado: 01, 0101, 010101,...

#### Ex4:
- ./a.out  (a+b)a*
- Resultado: a, b, aa, ba, aaa, baa, aaaa, baaa, ...



### Como rodar o projeto
    - pip install virtualenv
    - python3 -m virtualenv venv
    - linux
        - source venv/bin/activate
    - windows
        - venv\Scripts\activate
    - pip install Flask==2.1.2
    - export FLASK_APP=app.py
    - export FLASK_ENV=development



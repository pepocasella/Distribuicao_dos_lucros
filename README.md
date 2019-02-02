# Distribuição dos lucros (desafio Stone Pagamentos)

![stone_pagamentos](https://user-images.githubusercontent.com/11545292/51984146-c2daa180-2481-11e9-8dd4-6317ee169e30.png)

# Objetivo

Avaliar o candidato (a) nos conceitos de orientação a objeto, qualidade de código, aplicação de padrões, resiliência, disponibilidade, performance, capacidade de monitoramento, testes em suas diversas formas e o bom uso do git (clareza dos commits, divisão do trabalho e melhores práticas).

# Descritivo do desafio

Uma empresa fechou o ano de operação com lucro e deseja reparti-lo entre seus funcionários, com o objetivo de ser justa criou uma regra para a distribuição deste montante por: área, tempo de empresa, e faixa salarial (os funcionários que ganham menos teriam sua participação incrementada). Para isso foi solicitado ao time de tecnologia que desenvolva uma API REST que receba um valor máximo para distribuir e distribua o montante para os funcionários já cadastrados com os dados abaixo. Tal distribuição segue determinadas regras descritas a seguir

. Regras Gerais Foi estabelecido um peso por área de atuação: 

- Peso 1: Diretoria; 
- Peso 2: Contabilidade, 
- Financeiro, Tecnologia; 
- Peso 3: Serviços Gerais; 
- Peso 5: Relacionamento com o Cliente; 

Foi estabelecido um peso por faixa salarial e uma exceção para estagiários: 

- Peso 5: Acima de 8 salários mínimos; 
- Peso 3: Acima de 5 salários mínimos e menor que 8 salários mínimos; 
- Peso 2: Acima de 3 salários mínimos e menor que 5 salários mínimos; 
- Peso 1: Todos os estagiários e funcionários que ganham até 3 salários mínimos; 

Foi estabelecido um peso por tempo de admissão: 

- Peso 1: Até 1 ano de casa; 
- Peso 2: Mais de 1 ano e menos de 3 anos; 
- Peso 3: Acima de 3 anos e menos de 8 anos; 
- Peso 5: Mais de 8 anos

# Descritivo dos arquivos relevantes

- main:

O arquivo main.py engloba todas as funções utilizadas e faz o uso da classe_funcionarios.py para instaciar os objetos e realizar operações com estes. O fluxograma ilustrado abaixo descreve com bastante detalhe o passo senquancial lógico por tras da função main

- classe_funcionarios:

O arquivo classe_funcionarios.py armazena todos os atributos idealizados para o objeto funcionario e possiveis métodos vinculados a classe

- banco_de_dados_funcionarios.xlsx:

O arquivo em excel banco_de_dados_funcionarios.xlsx é input do programa Distribuição de Lucros com os dados relavantes dos funcionarios da empresa (matricula, nome, area, cargo, salario_bruto, data_de_admissao)

- Planilha_bonus.xls:

O arquivo em excel Planilha_bonus.xls é output do programa Distribuição de Lucros com os dados estipulados para retorno (matricula, nome, valor da participação) 

# Fluxograma do código

- Descrição do funcionamento: ao inicializar o aplictivo "Distribuição de lucros" uma janela estilo prompt de comando será aberta com o nome do programa e um input sendo pedido para o software. Esse input é o total diponibilizado para bonus dos funcionarios. O software, em seguida, irá disponibilizar ainda via prompt de comando informácoes calculadas sobre o total distribuido, total disponibilizado e saldo total disponibilizado. Alem disso, apos ter inputado aquela informação, na pasta onde esta o arquivo executalvel é feito a criação de uma plani;ha em Excel com as informações de retorno do software: mtricula, nome, bonus. O programa realiza um popup com a mensagem de "click ENTER para finalizar o programa" e em seguida caso a tecla ENTER seja precionada o programa fecha.


![blank diagram 1](https://user-images.githubusercontent.com/11545292/52016818-bdef0f80-24cc-11e9-944d-34d19d184ebf.png)


# Distribuição dos lucros (desafio Stone Pagamentos)

![](icon_stone)

Uma empresa fechou o ano de operação com lucro e deseja reparti-lo entre seus funcionários, com o objetivo de ser justa criou uma regra para a distribuição deste montante por: área, tempo de empresa, e faixa salarial (os funcionários que ganham menos teriam sua participação incrementada). Para isso foi solicitado ao time de tecnologia que desenvolva uma API REST que receba um valor máximo para distribuir e distribua o montante para os funcionários já cadastrados com os dados abaixo. Tal distribuição segue determinadas regras descritas a seguir

. Regras Gerais Foi estabelecido um peso por área de atuação: 
Peso 1: Diretoria; 
Peso 2: Contabilidade, 
Financeiro, Tecnologia; 
Peso 3: Serviços Gerais; 
Peso 5: Relacionamento com o Cliente; 

Foi estabelecido um peso por faixa salarial e uma exceção para estagiários: 
Peso 5: Acima de 8 salários mínimos; 
Peso 3: Acima de 5 salários mínimos e menor que 8 salários mínimos; 
Peso 2: Acima de 3 salários mínimos e menor que 5 salários mínimos; 
Peso 1: Todos os estagiários e funcionários que ganham até 3 salários mínimos; 

Foi estabelecido um peso por tempo de admissão: 
Peso 1: Até 1 ano de casa; 
Peso 2: Mais de 1 ano e menos de 3 anos; 
Peso 3: Acima de 3 anos e menos de 8 anos; 
Peso 5: Mais de 8 anos


#fluxo grama do código

![blank diagram](https://user-images.githubusercontent.com/11545292/51984055-7e4f0600-2481-11e9-886f-64fd2d980536.png)

